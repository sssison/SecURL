var redirectUrl;

console.log('This is a popup!');
document.getElementById("test-req").addEventListener("click", sendTestRequest); //or add method for testing only!

// ? onload, fetch the results of the model
window.onload = async function(e){
    let currTab = await getCurrentTab();
    let tabId = currTab.id;
    console.log('I got tabID: ' + tabId.toString());

    // ! caution: chrome.storage.local.get still runs async even with await keyword
    chrome.storage.local.get("redirectUrls", function(data) {
        const redirectUrls = data.redirectUrls || {};
        console.log('I got redirectUrls');
        console.log(redirectUrls);
        // if (redirectUrls[tabId]!=null && currTab.url.includes(redirectUrls[tabId]["url"])){
        // above condition will fail for REDIRECT LINKS.
        // TODO: if link is different, UPDATE the storage? 
        redirectUrl = redirectUrls[tabId]["url"];
        if (redirectUrls[tabId]!=null && currTab.url.includes(redirectUrls[tabId]["url"])){
            console.log('I also got URL: ' + redirectUrl);
        } else {
            console.log('Error with the redirectUrl');
            console.log(redirectUrls[tabId]);
            console.log("Compare href <" + currTab.url + "> and redirect <" + redirectUrls[tabId]["url"] + ">");
        }
        
        // ? populate the fields
        console.log("populating the fields now...");
        document.getElementById("test-url-span").innerText = redirectUrl;
        console.log(redirectUrls[tabId]);
        document.getElementById("test-response-span").innerText = redirectUrls[tabId]["serverResult"]["message"];
    });

    // onclick of report text, show the modal
    document.querySelector(".report-error-text").addEventListener("click", sendReportPopup);
}

async function sendTestRequest() {
    var startTime, endTime, endTime2;
    startTime = performance.now();

    console.log('This button was clicked!');
    // url = "http://localhost:5000/securl";
    // inp_url: "https://www.google.com"
    var currUrl = await getCurrentTab();
    var isEnhancedSec = await getIsEnhancedSec();
    currUrl = currUrl["url"];
    var serverUrl = "http://10.158.66.12:5000/securl?"
    url = serverUrl + new URLSearchParams({
        inp_url: currUrl,
        is_secure: (isEnhancedSec ? "enabled" : "disabled")
    });
    console.log(url);

    var response_json = null;
    endTime = performance.now();
    await fetch(url, {
        method: 'GET',
    })
        .then(function (data) {
            console.log('Request succeeded with JSON response');
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

    chrome.storage.local.get(
        { blacklist: [] },
        (items) => {
            document.getElementById("test-url-span").innerText = response_json["url"];
            var x = 0;
            var blacklisted = false;
            var urlMessage = "";
            for (var x = 0; x < items.blacklist.length; x++) {
                if (response_json["url"].includes(items.blacklist[x])) {
                    blacklisted = true;
                    break;
                }
            }
            if (blacklisted) {
                urlMessage = "Blacklisted";
            } else {
                urlMessage = response_json["message"];
                // urlMessage = (response_json["safety"] ? `Safe (${response_json["score"]}%)` : `Malicious (${response_json["score"]}%)`);;
            }
            endTime2 = performance.now()
            document.getElementById("test-response-span").innerText = urlMessage;
            document.getElementById("time-span").innerText = (response_json["time"].toFixed(4) + " sec.");
            // document.getElementById("setup-span").innerText = (((endTime - startTime) / 1000).toFixed(4) + " seconds");
            document.getElementById("net-span").innerText = ((((endTime2 - startTime) / 1000) - response_json["time"]).toFixed(4) + " sec.");
            document.getElementById("req-span").innerText = (((endTime2 - startTime) / 1000).toFixed(4) + " sec.");
            // document.getElementById('status').innerText = "I like blacklist: " + items.blacklist.toString();
            // document.getElementById('like').checked = items.likesColor;
            // document.getElementById('blacklist-input').value = items.blacklist.join("\n");
        }
    );
    // document.getElementById("test-response-span").innerText = (response_json["safety"] ? `Safe (${response_json["score"]}%)` : `Malicious (${response_json["score"]}%)`);
    // document.getElementById("test-url-span").innerText = response_json["url"];
    
    // if(response_json!==null){
        //     console.log("Succeeded response body: ");
        //     console.log(response_json["body"]);
        // }
        
        /*
        NOTES:
        ? the returned value of fetch after running response.json() is still a Promise, not JSON
        ? read: https://stackoverflow.com/questions/37555031/why-does-json-return-a-promise-but-not-when-it-passes-through-then
        ? try using async methods instead
        */
       /*
       if trying fetch with URL params... (https://stackoverflow.com/questions/35038857/setting-query-string-using-fetch-get-request)
       fetch('https://example.com?' + new URLSearchParams({
           foo: 'value',
           bar: 2,
        }))
        */
}
    
// copied from Chrome docs: https://developer.chrome.com/docs/extensions/reference/tabs/
async function getCurrentTab() {
    let queryOptions = { active: true, currentWindow: true };
    // let queryOptions = { active: true, lastFocusedWindow: true };
    // `tab` will either be a `tabs.Tab` instance or `undefined`.
    let [tab] = await chrome.tabs.query(queryOptions);
    return tab;
}

async function getIsEnhancedSec() {
    let fetchEnhancedFromLocal = await chrome.storage.local.get({ enhanced_sec: false });
    // returns an object: {enhanced_sec: <true/false>}
    return fetchEnhancedFromLocal["enhanced_sec"];
}

async function sendReportPopup(){
    let currTab = await getCurrentTab();
    let tabId = currTab.id;
    console.log("sendReportPopup triggered with tabId: " + tabId.toString());

    // for now, immediately trigger the feedback report
    // TODO: insert modal or confirmation div to ensure that user clicked correctly
    document.querySelector(".report-error-text").removeEventListener("click",sendReportPopup);

    // TODO: send the request (copied from warning_page.js)
    // TODO sub 1: adjust predicted/correct to benign/malicious depending on the result!
    var serverUrl = "http://10.158.66.12:5000/securl/feedback?"
    var url = serverUrl + new URLSearchParams({
        url: redirectUrl,
        predicted: "Benign",
        correct: "Malicious"
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

    // TODO: trigger notification stating success (send a message)
    const response = chrome.tabs.sendMessage(tabId,{action: "open_notif",source: "popup"});
    // const response = chrome.runtime.sendMessage({action: "open_notif",source: "popup"});
}