document.addEventListener("DOMContentLoaded", function () {
    // Retrieve current tab ID
    chrome.tabs.getCurrent(function (tab) {
        const tabId = tab.id;
        // Retrieve redirect URL for the current tab from storage
        chrome.storage.local.get("redirectUrls", function(data) {
            const redirectUrls = data.redirectUrls || {};
            const redirectUrl = redirectUrls[tabId]["url"];
            // Populate button with redirect URL
            document.getElementById("proceed-page").addEventListener("click", function () {
                // Update the *skipped* status of this tab to mark that you can ignore the warning page
                redirectUrls[tabId]["skipped"] = true;
                chrome.storage.local.set({ "redirectUrls": redirectUrls }, function() {
                    // ? Redirect user to the detected redirect URL
                    window.location.href = redirectUrl;
                });

            });
        });
    });

    /*
        ALT WAY TO ACCESS THE ACTIVE TAB (SEEN BY USER)
        ===============================================
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            const tabId = tabs[0].id;
            ...
        });
    */

    // Event listener for exit button
    document.getElementById("return-page").addEventListener("click", function () {
        // Return to previous link... or close the tab
        chrome.tabs.getCurrent(function (tab) {
            // chrome.tabs.remove(tab.id);
            // fallbackUrl = fallbackUrl || '/';
            var prevPage = window.location.href;

            window.history.go(-1);

            setTimeout(function(){ 
                if (window.location.href == prevPage) {
                    chrome.tabs.remove(tab.id);
                }
            }, 200);
            
            // history.back();
        });
    });
});