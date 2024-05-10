var redirectUrl;

document.addEventListener("DOMContentLoaded", function () {
    // Retrieve current tab ID
    chrome.tabs.getCurrent(function (tab) {
        const tabId = tab.id;
        // Retrieve redirect URL for the current tab from storage
        chrome.storage.local.get("redirectUrls", function(data) {
            const redirectUrls = data.redirectUrls || {};
            redirectUrl = redirectUrls[tabId]["url"];
            // Populate button with redirect URL
            document.getElementById("proceed-page").addEventListener("click", function() {
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

    // onclick of report text, show the modal
    document.querySelector(".report-error-text").addEventListener("click",openReportModal);

    // onclick of the buttons of the modal, do proper action
    document.getElementById("fb-cancel").addEventListener("click", function(){
        // document.querySelector("#fb-modal-window")
        document.getElementById("fb-modal-window").style.display = "none";
    });
    document.getElementById("fb-confirm").addEventListener("click", function(){        
        // hide the modal
        document.getElementById("fb-modal-window").style.display = "none";

        // TODO: upon confirmation, disable the report button
        document.querySelector(".report-error-text").removeEventListener("click",openReportModal);

        // TODO: send the request
        // currUrl = currUrl["url"];
        var serverUrl = "http://10.158.66.12:5000/securl/feedback?"
        var url = serverUrl + new URLSearchParams({
            url: redirectUrl,
            predicted: "Malicious",
            correct: "Benign"
        });
        console.log(url);

        var response_json = null;
        fetch(url, {
            method: 'GET',
        })
            .then(function (data) {
                console.log('Report succeeded with JSON response');
                return data.json(); //call only ONCE (affects data variable)
                // shortcut: // .then(response => response.json())
            })
            .then(function(data_json){
                response_json = data_json;
                console.log(response_json);
            })
            .catch(function (error) {
                console.log('Request failed', error);
            });

        // animate the notification box
        console.log("DONE!");
        document.querySelector("div.notif-box").style.display = "flex";
        document.querySelector("div.notif-box").style.transition = "right 1s ease, opacity 0.3s linear";
        document.querySelector("div.notif-box").classList.add("notransition");
        document.querySelector("div.notif-box").style.right = `${-document.querySelector("div.notif-box").offsetWidth-20}px`;
        document.querySelector("div.notif-box").style.visibility = `visible`;
        document.querySelector("div.notif-box").style.opacity = `1`;
        setTimeout(function(){
            document.querySelector("div.notif-box").classList.remove("notransition");
            document.querySelector("div.notif-box").style.right = `20px`;
            // document.querySelector("div.notif-box").style.right = `20px`;
        },10);
        setTimeout(function(){
            // document.querySelector("div.notif-box").classList.remove("notransition");
        },50);
        setTimeout(function(){
            document.querySelector("div.notif-box").style.opacity = `0`;
        },3000);
    });
});

document.querySelector("div.notif-box").addEventListener('transitionend', function(event) {
    // alert("CSS Property completed: " + event.propertyName);
    if(event.propertyName==="opacity"){
        console.log("triggered opacity");
        document.querySelector("div.notif-box").style.visibility = `hidden`;
    }
}, false );

function openReportModal(){
    document.getElementById("fb-modal-window").style.display = "flex";
    document.getElementById("fb-modal-url").innerText = redirectUrl;
}