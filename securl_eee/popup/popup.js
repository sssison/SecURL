var redirectUrl;

console.log('This is a popup!');
// document.getElementById("test-req").addEventListener("click", sendTestRequest); //or add method for testing only!

// ? onload, fetch the results of the model
window.onload = async function(e){
    let currTab = await getCurrentTab();
    let isEnhancedSec = await getIsEnhancedSec();
    let tabId = currTab.id;
    let urlStatus = "N/A";
    console.log('I got tabID: ' + tabId.toString());

    // ! caution: chrome.storage.local.get still runs async even with await keyword
    chrome.storage.local.get(["redirectUrls"], function(data) {
        const redirectUrls = data.redirectUrls || {};
        console.log('I got redirectUrls at tabId ' + tabId.toString());
        console.log(redirectUrls);
        // if (redirectUrls[tabId]!=null && currTab.url.includes(redirectUrls[tabId]["url"])){
        // above condition will fail for REDIRECT LINKS.
        // TODO: if link is different, UPDATE the storage? 

        let tabProps = {};
        if (redirectUrls[tabId]!=null){
            tabProps = JSON.parse(JSON.stringify(redirectUrls[tabId]));
            console.log("Starting popup script here with tabProps");
            console.log(tabProps);

            redirectUrl = tabProps["url"];
            
            console.log(`Comparing serverResult and tabProps[url] <${tabProps["url"]}> and currTab[url] <${currTab.url}>`);
            console.log(tabProps["serverResult"]);

            // ! EXPERIMENT: check if server result already ready or not
            if (tabProps["serverResult"]!=null && tabProps["hasResult"]){
                // tabProps["url"]===currTab.url
                urlStatus = tabProps["serverResult"]["message"];
                
                // only for debugging purposes!
                if (currTab.url.includes(redirectUrls[tabId]["url"])){
                    console.log('I also got URL: ' + redirectUrl);
                } else {
                    console.log('Error with the redirectUrl');
                    console.log(redirectUrls[tabId]);
                    console.log("Compare href <" + currTab.url + "> and redirect <" + redirectUrls[tabId]["url"] + ">");
                }
            } else { // server is not done analyzing, or the URL is incorrect!
                urlStatus = "Analyzing";
            }

            
        } else { // TODO: put fallback values here if no redirectUrl values for tab!
            redirectUrl = "<none>";
            urlStatus = "N/A";
        }
        
        // TODO: if results are available, fill in the fields. Otherwise, put a default!

        // ? populate the fields
        console.log("populating the fields now...");
        document.getElementById("test-url-span").innerText = redirectUrl;
        console.log(redirectUrls[tabId]);

        // update the heading: Benign, Malicious (Blacklisted <ignores status benign/malicious>, Malicious, Blank)
        // let urlStatusHeading = urlStatus;
        // if (redirectUrls[tabId] && )
        // if (urlStatusHeading==="Malicious"){
            
        // }
        
        
        // update the image src, located in img folder
        document.querySelector("div.result > img").src = `../img/${(tabProps["flagged"] || urlStatus==="Analyzing") ? "danger" : "secure"}.png`;
        // document.querySelector("div.result > img").src = `../img/${urlStatus!=="Benign" && !(urlStatus.includes("Benign")) ? "danger" : "secure"}.png`;

        // update the security strength
        document.querySelector("span.sec-strength").innerText = (isEnhancedSec ? "Enhanced" : "Basic");

        // update the status description: Benign, Malicious, Blacklisted, Blank Site
        let statusText = "";
        let urlStatusHeading = urlStatus;
        if (tabProps["flagged"]) {
            if (tabProps["purpose"]==="blacklisted"){
                urlStatusHeading = "Blacklisted";
                statusText = "The current website matches your personal blacklist filters. Proceed with caution as this site has been flagged by your settings.";
            } else if (tabProps["purpose"]==="unfetchable"){
                urlStatusHeading = "Empty Site";
                statusText = "The site appears to be empty or the contents cannot be fetched by the server. This could indicate a security risk.";
            } else if (tabProps["purpose"]==="malicious"){
                // added logic depending on content-based security (enhanced) and combination of lexical/content result
                let isSecure = tabProps["serverResult"]["secure"];
                let lexResult = tabProps["serverResult"]["rlex"];
                let contResult = tabProps["serverResult"]["rcont"];
                console.log(`Trying out ${tabProps["serverResult"]["url"]} with lex ${tabProps["serverResult"]["rlex"]} and cont ${tabProps["serverResult"]["rcont"]}`)

                if (isSecure){  // check for malicious-benign, benign-malicious, malicious-malicious
                    if (lexResult!=="Benign"){
                        if (contResult!=="Benign"){
                            urlStatusHeading = "Highly Suspicious Website";
                            statusText = "This website (URL) and its content raise significant security concerns. There's a high risk of encountering malware, scams, or phishing attempts. It is highly advised to return to the previous page.";
                        } else {
                            urlStatusHeading = "Suspicious URL";
                            statusText = "The website you are trying to visit (URL) has some characteristics that raise caution flags. While the content itself may currently appear harmless, there's a chance it could be misleading or contain hidden risks.";
                        }
                    } else { // could only be benign lexical malicoius content
                        urlStatusHeading = "Suspicious Content";
                        statusText = "The website you are trying to visit (URL) has some characteristics that raise caution flags. While the content itself may currently appear harmless, there's a chance it could be misleading or contain hidden risks.";
                    }
                } else {
                    urlStatusHeading = "Suspicious URL";
                    statusText = "The website you are trying to visit (URL) appears legitimate at first glance, but the content you've encountered raises some red flags. Proceed with caution.";
                }


            } else if (true) {
                statusText = "This page has been flagged for unidentified security reasons.";
            } else {
                statusText = "This page has been flagged for unidentified security reasons.";
            }
        } else if (urlStatus==="Analyzing") {
            // TODO: change popup, or adjust status text!
            // ! important edit needed! also check condition for icon
            urlStatusHeading = "Analyzing";
            statusText = "The server is still analyzing the result! Check back later for the results";
        } else {
            urlStatusHeading = "Benign";
            statusText = "No threats were detected in this webpage. You're good to go!";
        }

        document.getElementById("test-response-span").innerText = urlStatusHeading;
        document.querySelector("p.result-description").innerText = statusText;
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
    let msgProps = {
        action: "open_notif",
        source: "popup",
        notif: {
            style: "info",
            heading: "URL Report Success!",
            description: "Successfully sent the report to the server for feedback!"
        }
    }
    const response = chrome.tabs.sendMessage(tabId, msgProps);
    // const response = chrome.runtime.sendMessage({action: "open_notif",source: "popup"});
}