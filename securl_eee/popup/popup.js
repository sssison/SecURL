console.log('This is a popup!');

document.getElementById("test-req").addEventListener("click", sendTestRequest); //or add method for testing only!

async function sendTestRequest() {
    console.log('This button was clicked!');
    // url = "http://localhost:5000/securl";
    // inp_url: "https://www.google.com"
    var currUrl = await getCurrentTab();
    currUrl = currUrl["url"];
    url = "http://localhost:5000/securl?" + new URLSearchParams({
            inp_url: currUrl
        });
    console.log(url);
        
    var response_json = null;    
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
            for (var x=0; x<items.blacklist.length; x++){
                if(response_json["url"].includes(items.blacklist[x])){
                    blacklisted = true;
                    break;
                }
            }
            if (blacklisted){
                urlMessage = "This site was blacklisted!";
            } else {
                urlMessage = response_json["message"];
                // urlMessage = (response_json["safety"] ? `Safe (${response_json["score"]}%)` : `Malicious (${response_json["score"]}%)`);;
            }
            document.getElementById("test-response-span").innerText = urlMessage;
            document.getElementById("time-span").innerText = (response_json["time"].toFixed(4) + " seconds");
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