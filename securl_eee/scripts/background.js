// background.js

// Event listener for extension installation or update
chrome.runtime.onInstalled.addListener(function(details) {
    if (details.reason === "install" || details.reason === "update") {
        // Clear local storage
        chrome.storage.local.clear(function() {
            if (chrome.runtime.lastError) {
                console.error("Error clearing Chrome storage local:", chrome.runtime.lastError);
            } else {
                console.log("Chrome storage local cleared successfully");
            }
        });
    }
});

chrome.webNavigation.onBeforeNavigate.addListener(function (details) {
    // Check if it's the main frame navigation
    console.log("details");
    console.log(details)
    var redirectUrls, blacklists;
    var isMaliciousUrl = false;

    chrome.storage.local.get(["redirectUrls","blacklist"], function(data) {
        redirectUrls = data.redirectUrls || {};
        blacklists = data.blacklist || {};

        // ? access the URL or tab: details.url or  details.tabId
        
        if (details.frameId === 0 && details.parentFrameId === -1){
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
            // TODO: (see above)
            
            // ! update the URL of the tabId
            // redirectUrls[details.tabId] = details.url;
            
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
            if (redirectUrlUpdated["skipped"]){
                isMaliciousUrl = false;
                redirectUrlUpdated["skipped"] = false;
            }
            
            redirectUrls[details.tabId] = JSON.parse(JSON.stringify(redirectUrlUpdated));
            console.log(`For URL <${details.url}>, isMaliciousUrl=${isMaliciousUrl} `)
            
            redirectUrls[details.tabId] = redirectUrlUpdated;
            chrome.storage.local.set({ "redirectUrls": redirectUrls }, function() {
                // TODO: fix the scenario wherein user proceeds to malicious link. Right now, if from warning page, user enters new URL in address bar, it may not be scanned
                // ? Check the random number and redirect accordingly
                if (isMaliciousUrl) {
                    chrome.tabs.update(details.tabId, { url: `${chrome.runtime.getURL("warning_page/warning_page.html")}` });
                }
            });
        }
    });
});

chrome.tabs.onReplaced.addListener(function(addedTabId, removedTabId){
    console.log("onReplaced triggered");
    console.log(`added Tab: ${addedTabId} and removed Tab: ${removedTabId}`);
});