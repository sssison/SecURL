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
    var isBlacklisted = false;
    var redirectUrlUpdated;
    var isFetchable = true;        // check whether URL's HTML is fetchable or not. Not fetchable --> malicious
    var isSkipped = false;          // confirm that the current site WAS skipped by the user. default: FALSE
    var response_json;
    var enhancedSec;

    chrome.storage.local.get(["redirectUrls", "blacklist", "enhanced_sec"], async function (data) {
        redirectUrls = data.redirectUrls || {};
        blacklists = data.blacklist || {};
        enhancedSec = data.enhanced_sec

        // ? access the URL or tab: details.url or  details.tabId

        if (details.frameId === 0 && details.parentFrameId === -1) {
            // Generate a random number between 1 and 10
            const randomNumber = Math.floor(Math.random() * 10) + 1;

            // -TODO: check whether the URL is blacklisted (automatically malicious)
            // ! for multiple tabs running simultaneously, isBlacklisted may fluctuate between true/false! Double-check...
            for (var x = 0; x < blacklists.length; x++) {
                if (details.url.includes(blacklists[x])) {
                    isBlacklisted = true;
                    isMaliciousUrl = true;
                    break;
                }
            }

            // ! check also whether the URL is malicious or not using the service
            // TODO: (see above). parameters: URL, isSecure (configure this!)
            // ? already done AFTER checking whether URL skipped or not

            //// update the URL of the tabId ???
            //// redirectUrls[details.tabId] = details.url;            

            if (redirectUrls.hasOwnProperty(details.tabId)) {
                redirectUrlUpdated = JSON.parse(JSON.stringify(redirectUrls[details.tabId]));
                // TODO: handle the circular requests here, especially if redirecting to SAME LINK
                console.log(`Compare URLs ${details.url} and ${redirectUrlUpdated["url"]}`);
                if (details.url!==redirectUrlUpdated["url"] && !redirectUrlUpdated["fetched"]){
                    console.log("Running this override");
                    redirectUrlUpdated["skipped"] = false;
                }
                redirectUrlUpdated["url"] = details.url;
                redirectUrlUpdated["hasResult"] = true;
            } else {
                // ? add parameter for serverResult, or property indicating status of URL?
                redirectUrlUpdated = {
                    "url": details.url,
                    "skipped": false,
                    "fetched": true,
                    "purpose": null,
                    "hasResult": false,
                    "flagged": isBlacklisted
                };
            }

            // ! EXPERIMENTAL: update the local storage right away just to update hasResult to false (a.k.a in progress)
            redirectUrlUpdated["hasResult"] = false;
            redirectUrls[details.tabId] = JSON.parse(JSON.stringify(redirectUrlUpdated));
            console.log(`For URL <${details.url}>, isMaliciousUrl=${isMaliciousUrl} `)

            await setInStorage({ "redirectUrls": redirectUrls });
            console.log("Now proceeding with skipping...");

            // ? check if user already whitelisted the site OR proceeded to link (coming from warning page)
            // ? this is checked by skipped: true
            // already working!

            console.log(`For URL <${details.url}>, skipped=${redirectUrlUpdated["skipped"]} `);

            let ignoreNewUrlResult = false;
            
            // ? Cases for a skipped site: you skipped a malicious site ("fetched"==False), you skipped a BLANK site (["fetched"]==True), or you moved to a new site (malicious or benign)
            if (redirectUrlUpdated["skipped"]) { // you only pressed the SKIP button. DO NOT REDIRECT URL!
                isMaliciousUrl = false;
                isSkipped = true;
                // ! TODO: don't set to false right away? in the case of blank URLs
                redirectUrlUpdated["skipped"] = false;
                
                // // ! experimental: update skipped depending on fetchable quality. if NOT fetchable, keep the skip state

                // -TODO: previously UNFETCHABLE. you need to check current URL if fetchable!
                response_json = await checkIfMaliciousUrl(details.url, enhancedSec);
                console.log("response_json fetched following:");
                console.log(response_json);


                if (response_json["fetched"]){
                    isMaliciousUrl = (response_json["message"] !== "Benign" && !(response_json["message"].includes("Benign")));
                    isFetchable = true;
                    redirectUrlUpdated["serverResult"] = JSON.parse(JSON.stringify(response_json));     // store the entire JSON result in serverResult property
                    redirectUrlUpdated["fetched"] = true;
                    if (isMaliciousUrl){    // in case of malicious URL loop, still proceed
                        // isFetchable = false;    // ! temporary! just make the willRedirect condition false
                        ignoreNewUrlResult = true;   // indicate true, meaning that you should NOT redirect to new page still
                    }
                } else { // failed to fetch HTML; assume malicious
                    isMaliciousUrl = true; 
                    isFetchable = false;
                    redirectUrlUpdated["fetched"] = false;
                    // TODO: add another variable to track inability to fetch URL. This should be passed on as data to the warning page!
                    if (!redirectUrlUpdated["fetched"]){
                        redirectUrlUpdated["skipped"] = true;   // ? temporary? means continue to skip
                    }
                }


                // if (!redirectUrlUpdated["fetched"]) {
                    
                // } else { // ? a fetchable URL. still store the results of the server! (analyze malicious URL)
                //     redirectUrlUpdated["skipped"] = false;
                // }
            }

            // ! converted else if (!isMaliciousUrl) to if (!isMaliciousURl):
            else if (!isBlacklisted) { // -TODO: <efficiency> check with the model if NOT skipped and NOT in blacklist so far
                // isMaliciousUrl MAY STILL BE UPDATED! We wait for the evaluation of the model first...                
                console.log("running checkIfMaliciousUrl with parameters <" + details.url + "> and " + enhancedSec);
                
                // TODO: analyze the URL with the model now!
                response_json = await checkIfMaliciousUrl(details.url, enhancedSec);
                if (response_json["fetched"]){
                    console.log("called response_json result");
                    console.log(response_json);

                    isMaliciousUrl = (response_json["message"] !== "Benign" && !(response_json["message"].includes("Benign")));
                    redirectUrlUpdated["serverResult"] = JSON.parse(JSON.stringify(response_json));     // store the entire JSON result in serverResult property
                    redirectUrlUpdated["fetched"] = true;
                    isFetchable = true;
                    
                    console.log("Checked the URL with the model to get ff. result...");
                    console.log(response_json);
                } else { // failed to fetch HTML; assume malicious
                    isMaliciousUrl = true; 
                    isFetchable = false;
                    redirectUrlUpdated["fetched"] = false;
                    // TODO: add another variable to track inability to fetch URL. This should be passed on as data to the warning page!
                }
            }

            // TODO: update extension icon
            // ? assumption: there already is a result
            updateIcon(((isMaliciousUrl || isSkipped || isBlacklisted) ? "malicious" : "benign"));
            
            // TODO: before updating storage AND redirect URL, check if condition passes to redirect URL
            let willRedirect = false;
            if (isMaliciousUrl && (!isSkipped || isFetchable) && !ignoreNewUrlResult) {
                // original condition: (isMaliciousUrl && !isSkipped) && !(isSkipped && !isFetchable)
                willRedirect = true;
                
                // console.log(`Working with isMaliciousUrl <${isMaliciousUrl}>, isSkipped <${isSkipped}>, isFetchable <${isFetchable}>`);
                // chrome.tabs.update(details.tabId, { url: `${chrome.runtime.getURL("warning_page/warning_page.html")}` });
            } else {
                redirectUrlUpdated["purpose"] = null;
            }

            // TODO: add the proper reason for redirecting.
            // ! moved the logic from inside the willRedirect block to outside (after the block)
            if (isBlacklisted){
                redirectUrlUpdated["purpose"] = "blacklisted";
            } else if (!isFetchable){
                redirectUrlUpdated["purpose"] = "unfetchable";
            } else if (isMaliciousUrl){
                redirectUrlUpdated["purpose"] = "malicious";
            } else {
                redirectUrlUpdated["purpose"] = null;
            }

            // update flagged attribute. Good for updating extension icon
            redirectUrlUpdated["flagged"] = isMaliciousUrl || isSkipped || isBlacklisted;
            redirectUrlUpdated["hasResult"] = true;

            console.log("here is my final redirectUrlUpdated");
            console.log(redirectUrlUpdated);
            redirectUrls[details.tabId] = JSON.parse(JSON.stringify(redirectUrlUpdated));
            console.log(`For URL <${details.url}>, isMaliciousUrl=${isMaliciousUrl} `)

            chrome.storage.local.set({ "redirectUrls": redirectUrls }, function () {
                // -TODO: fix the scenario wherein user proceeds to malicious link. Right now, if from warning page, user enters new URL in address bar, it may not be scanned
                // -TODO new: if blank URL (or fetched===false), do NOT update the tab anymore!
                if (willRedirect) {
                    console.log(`Working with isMaliciousUrl <${isMaliciousUrl}>, isSkipped <${isSkipped}>, isFetchable <${isFetchable}>`);
                    chrome.tabs.update(details.tabId, { url: `${chrome.runtime.getURL("warning_page/warning_page.html")}` });
                }
                // ? logic: UPDATE tab when isMaliciousUrl && !isSkipped && (isFetchable?)
                // ? ...or !isFetchable && !isSkipped  
            });
            
        }
    });
});

chrome.tabs.onReplaced.addListener(function (addedTabId, removedTabId) {
    console.log("onReplaced triggered");
    console.log(`added Tab: ${addedTabId} and removed Tab: ${removedTabId}`);
});


// TODO: upon switching tabs or opening the active tab, change the icon depending on malicious status
chrome.tabs.onActivated.addListener(activeInfo => {
    chrome.tabs.get(activeInfo.tabId, tab => {
        // TODO: Check some condition to determine which icon to use
        // const shouldUseIcon1 = tab.url.includes("example.com");
        let siteSafety = "N/A";
        console.log("tab switching...");
        
        chrome.storage.local.get(
            ["redirectUrls"],
            (items) => {
                // console.log('items["redirectUrls"][activeInfo.tabId]');
                // console.log(items["redirectUrls"][activeInfo.tabId]);
                if (items["redirectUrls"]!=null && items["redirectUrls"][activeInfo.tabId]!=null){
                    let tabProps = items["redirectUrls"][activeInfo.tabId];
                    if (tabProps!=null && tabProps["hasResult"]){
                        console.log("tabProps");
                        console.log(tabProps);
                        urlStatus = tabProps["flagged"];
                        siteSafety = (urlStatus ? "malicious" : "benign");

                        // urlStatus = tabProps["serverResult"]["message"];
                        // if (urlStatus !== "Benign" && !(urlStatus.includes("Benign"))) {
                        //     siteSafety = "malicious";
                        // } else { // must be BENIGN
                        //     siteSafety = "benign";
                        // }

                        // ! chrome.storage.local.get is ASYNC! Continue the function within the callback function...
                        // sendResponse({ action: "open_notif", notif: msgProps });
                        // chrome.tabs.sendMessage(sender.tab.id, { action: "open_notif", notif: msgProps });
                    } else { // undefined! wait for the RESULT first!
                        // TODO: no result yet, so take default icon
                        siteSafety = "others";
                    }
                    // TODO: update the icon
                    updateIcon(siteSafety);
                }
            }
        );
    });
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
                    let tabProps = items["redirectUrls"][tabId];
                    if (tabProps!=null && tabProps["serverResult"]!=null){
                        console.log("tabProps");
                        console.log(tabProps);
                        urlStatus = tabProps["serverResult"]["message"];
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
                    } else { // undefined! wait for the RESULT first!
                        // TODO: either force obtain new results here, or wait for task above to finish?
                        // ! Attempt 1: force obtain new results here [WIP]

                    }
                }
            );
        } else {
            // console.log("Received no greeting but Hi.");
        }
    }
);

function getFromStorage(keys) {
    return new Promise((resolve, reject) => {
        chrome.storage.local.get(keys, (result) => {
            if (chrome.runtime.lastError) {
                reject(chrome.runtime.lastError);
            } else {
                resolve(result);
            }
        });
    });
}

function setInStorage(items) {
    return new Promise((resolve, reject) => {
        chrome.storage.local.set(items, () => {
            console.log("Done with setting!!!");
            if (chrome.runtime.lastError) {
                reject(chrome.runtime.lastError);
            } else {
                resolve();
            }
        });
    });
}

function updateIcon(status){
    // Set the icon based on the condition
    let iconPath = "../img/icons/";
    let iconName;
    
    if (status==="benign"){
        iconName = "logo_benign.png";
    } else if (status==="malicious"){
        iconName = "logo_malicious.png";
    } else {
        iconName = "logo.png";
    }

    // Update the icon
    chrome.action.setIcon(
        {
            path: {
                "16": (iconPath + iconName),
                "48": (iconPath + iconName),
                "128": (iconPath + iconName)
            }
        }
    );
}

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