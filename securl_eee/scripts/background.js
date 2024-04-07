// background.js
chrome.webNavigation.onBeforeNavigate.addListener(function (details) {
    // Check if it's the main frame navigation
    console.log("details");
    console.log(details)
    if (details.frameId === 0 && details.parentFrameId === -1){
        // Generate a random number between 1 and 10
        const randomNumber = Math.floor(Math.random() * 10) + 1;
    
        // Store the random number in Chrome storage
        chrome.storage.local.set({ randomNumber: randomNumber }, function () {
            // Log a message to the console indicating that the random number has been set
            console.log('Random number set to ' + randomNumber);
        });
    
        // Check the random number and redirect accordingly
        if (randomNumber < 5) {
            // ! Redirect to the WARNING page google.com (very instrusive)
            // chrome.tabs.update(details.tabId, { url: `${chrome.runtime.getURL("warning_page/warning_page.html")}` });
        }
    }
});