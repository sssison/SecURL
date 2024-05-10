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

// window.addEventListener("DOMContentLoaded", async function () {
if (document.readyState !== "loading") {
    initializeContentScript(); // Or setTimeout(onReady, 0); if you want it consistently async
} else {
    document.addEventListener("DOMContentLoaded", initializeContentScript);
}
// document.addEventListener("DOMContentLoaded", initializeContentScript);


async function initializeContentScript() {
    // get the current Tab ID
    // var currentTabId = "12345";

    // chrome.tabs.getCurrent(function(tab) {
    //     // tabs[0] will contain information about the currently active tab
    //     currentTabId = tab.id;
    //     console.log("Current tab ID:", currentTabId);
    //     // Retrieve malicious URL from storage
    //     chrome.storage.local.get(["redirectUrls"], function (result) {
    //         const maliciousURL = result.redirectUrls[currentTabId];
    //         // Populate button with malicious URL
    //         document.getElementById("proceedButton").addEventListener("click", function () {
    //             // Redirect user to the detected malicious URL
    //             window.location.href = maliciousURL;
    //         });
    //     });
    // });

    
    // ? Listen for message to trigger the notification banner, if applicable only\
    // TODO: remove this listener if not necessary
    // ! IMPORTANT: sendResponse doesnt trigger the onMessage listener. Instead, it goes to the *response* variable.
    chrome.runtime.onMessage.addListener(
        function(request, sender, sendResponse) {
            console.log(sender.tab ?
                "from a content script:" + sender.tab.url :
                "from the extension");
            
            console.log(request);
            
            if (request.hasOwnProperty("action") && request.action === "open_notif"){
                // sendResponse({farewell: "goodbye"});
                console.log("Received a signal to trigger the notification. Go!");
                createNotif();
            } else {
                console.log("Received no greeting but Hi.");       
            }
        }
    );
        
    // ! send the message to the background script stating that we're ready to trigger the notification
    const response = await chrome.runtime.sendMessage({message: "tab_ready"});
    console.log("We sent a message! See the response:");
    console.log(response);

    // ! trigger the notification (and other necessary actions) here depending on response of server!
    if (response.hasOwnProperty("action") && response.action === "open_notif"){
        // sendResponse({farewell: "goodbye"});
        console.log("Received a signal to trigger the notification. Go!");
        createNotif();
    } else {
        console.log("Received no greeting but Hi.");
        
    }

    // // Event listener for exit button
    // document.getElementById("exitButton").addEventListener("click", function () {
    //     // Close the tab
    //     chrome.tabs.getCurrent(function (tab) {
    //         chrome.tabs.remove(tab.id);
    //     });
    // });
}

function createNotif(){
    // If notification already exists, delete!
    var notifBox = document.querySelector("div.notif-box");
    if (notifBox){
        notifBox.remove();
    }

    // Create the div element
    var divElement = document.createElement('div');
    divElement.classList.add('notif-box');

    var h2Element = document.createElement('h2');
    h2Element.textContent = 'URL Report Success';
    divElement.appendChild(h2Element);

    var pElement = document.createElement('p');
    pElement.textContent = 'Successfully sent the report to the server for feedback!';
    divElement.appendChild(pElement);

    // Append the div element to the body
    document.body.appendChild(divElement);

    // TODO: animate the notification box
    document.querySelector("div.notif-box").style.display = "flex";
    document.querySelector("div.notif-box").style.transition = "right 1s ease, opacity 0.3s linear";
    document.querySelector("div.notif-box").classList.add("notransition");
    document.querySelector("div.notif-box").style.right = `${-document.querySelector("div.notif-box").offsetWidth-20}px`;
    document.querySelector("div.notif-box").style.visibility = `visible`;
    document.querySelector("div.notif-box").style.opacity = `1`;
    setTimeout(function(){
        document.querySelector("div.notif-box").classList.remove("notransition");
        document.querySelector("div.notif-box").style.right = `20px`;
    },10);
    setTimeout(function(){
        document.querySelector("div.notif-box").style.opacity = `0`;
        // document.querySelector("div.notif-box").remove();
    },3000);
    
}
// setInterval(createNotif,6000);

// createNotif();