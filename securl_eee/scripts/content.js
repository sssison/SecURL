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
newBanner.innerText = "This is a div! Try something new here";

document.body.appendChild(newBanner);
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
chrome.storage.local.get(['randomNumber'], function (result) {
    const randomNumber = result.randomNumber;
  
    // // Check the random number and redirect accordingly
    // if (randomNumber <= 5) {
    //   // Redirect to URL1
    //   window.location.href = 'https://example.com/url1';
    // } else {
    //   // Redirect to URL2
    //   window.location.href = 'https://example.com/url2';
    // }
  });