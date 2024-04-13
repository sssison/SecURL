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
    var redirectUrls;
    var isMaliciousUrl = false;
    chrome.storage.local.get("redirectUrls", function(data) {
        redirectUrls = data.redirectUrls || {};

        // ? access the URL or tab: details.url or  details.tabId
        
        if (details.frameId === 0 && details.parentFrameId === -1){
            // Generate a random number between 1 and 10
            const randomNumber = Math.floor(Math.random() * 10) + 1;
            
            // ! check whether the URL is malicious or not
            // if (randomNumber < 5){
            if (details.url.includes("reddit.com")){
                isMaliciousUrl = true;
            }

            // console.log('Random number set to ' + randomNumber);
            console.log('isMaliciousUrl: ' + isMaliciousUrl);
            // // Store the random number in Chrome storage
            //// chrome.storage.local.set({ randomNumber: randomNumber }, function () {
            //     // Log a message to the console indicating that the random number has been set
            //// });
            
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

            // ! check if user already whitelisted the site OR proceeded to link (coming from warning page)
            // ! this is checked by skipped: true
            
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