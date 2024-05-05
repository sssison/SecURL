console.log(`SecURL detected URL: ${window.location.toString()}`);

// ** CUSTOM BANNER FOR STATUS
var newBanner = document.createElement("div");
newBanner.style.position = "fixed";
newBanner.style.zIndex = "1000";
newBanner.style.backgroundColor = "aquamarine";
newBanner.style.padding = "20px";
newBanner.style.right = "1vw";
newBanner.style.top = "1vw";
newBanner.style.opacity = "0.7";
newBanner.style.fontSize = "1.25rem";
newBanner.style.fontFamily = "Arial, sans-serif";
newBanner.style.lineHeight = "normal";
newBanner.innerText = "This is a div! Try something new here";

// TODO: if you still want to add a banner to every page, uncomment the line below
// document.body.appendChild(newBanner);
/*
    position: fixed;
    z-index: 1000;
    background-color: aquamarine;
    padding: 20px;
    right: 1vw;
    top: 1vw;
    opacity: 0.5;
*/
// alert(`SecURL detected URL: ${window.location.toString()}`);
// console.log();

// ! ChatGPT suggestion
// content.js
chrome.storage.local.get(['randomNumber','redirectUrls'], function (result) {
    const randomNumber = result.randomNumber;
    console.log("random number:" + randomNumber);
    console.log(result);
    // // Check the random number and redirect accordingly
    // if (randomNumber <= 5) {
    //   // Redirect to URL1
    //   window.location.href = 'https://example.com/url1';
    // } else {
    //   // Redirect to URL2
    //   window.location.href = 'https://example.com/url2';
    // }
  });

document.addEventListener("DOMContentLoaded", function () {
    // get the current Tab ID
    chrome.tabs.getCurrent(function(tab) {
        // tabs[0] will contain information about the currently active tab
        const currentTabId = tab.id;
        console.log("Current tab ID:", currentTabId);
        // Retrieve malicious URL from storage
        chrome.storage.local.get(["redirectUrls"], function (result) {
            const maliciousURL = result.redirectUrls[currentTabId];
            // Populate button with malicious URL
            document.getElementById("proceedButton").addEventListener("click", function () {
                // Redirect user to the detected malicious URL
                window.location.href = maliciousURL;
            });
        });
    });

    // // Event listener for exit button
    // document.getElementById("exitButton").addEventListener("click", function () {
    //     // Close the tab
    //     chrome.tabs.getCurrent(function (tab) {
    //         chrome.tabs.remove(tab.id);
    //     });
    // });
});

// // ! Listen for event that URL was detected as malicious
// chrome.runtime.onMessage.addListener(
//     function(request, sender, sendResponse) {
//         console.log(sender.tab ?
//                     "from a content script:" + sender.tab.url :
//                     "from the extension");
//         if (request.hasOwnProperty("greeting") && request.greeting === "hello"){
//             // sendResponse({farewell: "goodbye"});
//             console.log("Received a malicious URL warning. Hi.");
//         } else {
//             console.log("Received no greeting but Hi.");
            
//         }
//     }
// );