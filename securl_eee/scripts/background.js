// background.js

// Event listener for extension installation or update
chrome.runtime.onInstalled.addListener(function (details) {
    if (details.reason === "install" || details.reason === "update") {
        // Clear local storage
        chrome.storage.local.clear(function () {
            if (chrome.runtime.lastError) {
                console.error("Error clearing Chrome storage local:", chrome.runtime.lastError);
            } else {
                console.log("Chrome storage local cleared successfully");
            }
        });
    }
});

chrome.webNavigation.onBeforeNavigate.addListener(function (details) {
    // ! accept only HTTP and HTTPS URLs
    if (!details.url || !details.url.startsWith('http')) {
        return;
    }

    // Check if it's the main frame navigation
    console.log("details");
    console.log(details)
    var redirectUrls, blacklists;
    var isMaliciousUrl = false;
    var response_json;

    chrome.storage.local.get(["redirectUrls", "blacklist"], async function (data) {
        redirectUrls = data.redirectUrls || {};
        blacklists = data.blacklist || {};

        // ? access the URL or tab: details.url or  details.tabId

        if (details.frameId === 0 && details.parentFrameId === -1) {
            // Generate a random number between 1 and 10
            const randomNumber = Math.floor(Math.random() * 10) + 1;

            // TODO: check whether the URL is blacklisted (automatically malicious)
            for (var x = 0; x < blacklists.length; x++) {
                if (details.url.includes(blacklists[x])) {
                    isMaliciousUrl = true;
                    break;
                }
            }

            // ! check also whether the URL is malicious or not using the service
            // TODO: (see above). parameters: URL, isSecure (configure this!)
            // ? already done AFTER checking whether URL skipped or not

            //// update the URL of the tabId ???
            //// redirectUrls[details.tabId] = details.url;

            var redirectUrlUpdated;

            if (redirectUrls.hasOwnProperty(details.tabId)) {
                redirectUrlUpdated = JSON.parse(JSON.stringify(redirectUrls[details.tabId]));
                redirectUrlUpdated["url"] = details.url;
            } else {
                redirectUrlUpdated = {
                    "url": details.url,
                    "skipped": false
                };
            }

            // ? check if user already whitelisted the site OR proceeded to link (coming from warning page)
            // ? this is checked by skipped: true
            // already working!

            console.log(`For URL <${details.url}>, skipped=${redirectUrlUpdated["skipped"]} `)
            if (redirectUrlUpdated["skipped"]) {
                isMaliciousUrl = false;
                redirectUrlUpdated["skipped"] = false;
            } else if (!isMaliciousUrl) { // TODO: <efficiency> only check with the model if NOT skipped and NOT in blacklist so far
                response_json = await checkIfMaliciousUrl(details.url, false);
                console.log("called response_json result");
                console.log(response_json);
                isMaliciousUrl = (response_json["message"] !== "Benign" && !(response_json["message"].includes("Benign")));
                redirectUrlUpdated["serverResult"] = response_json;     // store the entire JSON result in serverResult property
                console.log("Checked the URL with the model to get ff. result...");
                console.log(response_json);
            }

            redirectUrls[details.tabId] = JSON.parse(JSON.stringify(redirectUrlUpdated));
            console.log(`For URL <${details.url}>, isMaliciousUrl=${isMaliciousUrl} `)

            redirectUrls[details.tabId] = redirectUrlUpdated;
            chrome.storage.local.set({ "redirectUrls": redirectUrls }, function () {
                // TODO: fix the scenario wherein user proceeds to malicious link. Right now, if from warning page, user enters new URL in address bar, it may not be scanned
                // ? Check the random number and redirect accordingly
                if (isMaliciousUrl) {
                    chrome.tabs.update(details.tabId, { url: `${chrome.runtime.getURL("warning_page/warning_page.html")}` });
                }
            });
        }
    });
});

chrome.tabs.onReplaced.addListener(function (addedTabId, removedTabId) {
    console.log("onReplaced triggered");
    console.log(`added Tab: ${addedTabId} and removed Tab: ${removedTabId}`);
});

// ! Listen for message to trigger the notification banner, if applicable only
chrome.runtime.onMessage.addListener(
    function (request, sender, sendResponse) {
        var urlStatus;
        var msgProps = {};
        var tabId = sender.tab.id;
        console.log(sender.tab);
        console.log(sender.tab ?
            "from a content script:" + sender.tab.url :
            "from the extension");
        if (request.hasOwnProperty("message") && request.message === "tab_ready") {
            console.log("Received signal with message tab_ready");

            // TODO: check if malicious or benign site. Fetch the data and send to content script 
            
            
            chrome.storage.local.get(
                ["redirectUrls"],
                (items) => {  
                    urlStatus = items["redirectUrls"][tabId]["serverResult"]["message"];
                    if (urlStatus !== "Benign" && !(urlStatus.includes("Benign"))) {
                        // indicate a MALICIOUS link! Send a red notification
                        msgProps["style"] = "danger";
                        msgProps["heading"] = "Malicious URL detected!";
                        msgProps["description"] = "SecURL identified this link as a malicious URL! Be wary of any threats and browse safely!"
                    } else { // must be BENIGN
                        msgProps["style"] = "safe";
                        msgProps["heading"] = "This URL is safe!";
                        msgProps["description"] = "SecURL did not identify anything suspicious with the link.";
                    }

                    // ! chrome.storage.local.get is ASYNC! Continue the function within the callback function...
                    // sendResponse({ action: "open_notif", notif: msgProps });
                    chrome.tabs.sendMessage(sender.tab.id, { action: "open_notif", notif: msgProps });
                }
            );
        } else {
            // console.log("Received no greeting but Hi.");
        }
    }
);

async function checkIfMaliciousUrl(currentUrl, isEnhancedSec) {
    var serverUrl = "http://10.158.66.12:5000/securl?";
    var url = serverUrl + new URLSearchParams({
        inp_url: currentUrl,
        is_secure: (isEnhancedSec ? "enabled" : "disabled")
    });
    // console.log(url);

    var response_json = null;
    await fetch(url, {
        method: 'GET',
    })
        .then(function (data) {
            // console.log('Request succeeded with JSON response');
            return data.json(); //call only ONCE (affects data variable)
            // shortcut: // .then(response => response.json())
        })
        .then(function (data_json) {
            response_json = data_json;
            // console.log(response_json);
        })
        .catch(function (error) {
            console.log('Request failed', error);
        });

    return response_json;
}