/*
? example options script from https://developer.chrome.com/docs/extensions/mv3/options/ 
// Saves options to chrome.storage
const saveOptions = () => {
const color = document.getElementById('color').value;
const likesColor = document.getElementById('like').checked;

chrome.storage.sync.set(
{ favoriteColor: color, likesColor: likesColor },
() => {
// Update status to let user know options were saved.
const status = document.getElementById('status');
status.textContent = 'Options saved.';
setTimeout(() => {
status.textContent = '';
}, 750);
}
);
};

// Restores select box and checkbox state using the preferences
// stored in chrome.storage.
const restoreOptions = () => {
chrome.storage.sync.get(
{ favoriteColor: 'red', likesColor: true },
(items) => {
document.getElementById('color').value = items.favoriteColor;
document.getElementById('like').checked = items.likesColor;
}
);
};

document.addEventListener('DOMContentLoaded', restoreOptions);
document.getElementById('save').addEventListener('click', saveOptions);
*/

const restoreOptions = () => {
  chrome.storage.local.get(
    {blacklist:[],enhanced_sec:false},
    (items) => {
      // document.getElementById('status').innerText = "I like blacklist: " + items.blacklist.toString();
      // document.getElementById('like').checked = items.likesColor;
      console.log(items);
      document.getElementById('blacklist-input').value = items.blacklist.join("\n");
      document.getElementById('enchanced-input').checked = items.enhanced_sec;
    }
  );
};

const saveOptions = () => {
  const blacklistInp = document.getElementById('blacklist-input').value;
  var blacklistInpList = blacklistInp.split("\n");
  blacklistInpList = blacklistInpList.filter(n => n);
  const isEnhancedSec = document.getElementById('enchanced-input').checked;

  chrome.storage.local.set(
    {
      blacklist: blacklistInpList,
      enhanced_sec: isEnhancedSec
    },
    (items) => {
      // Update status to let user know options were saved.
      const status = document.getElementById('status');
      status.innerText = 'Options saved! The list: ' + blacklistInpList.toString() + " with enhanced security " + (isEnhancedSec ? "enabled" : "disabled");
      // status.textContent = 'Options saved.';
      // setTimeout(() => {
      //     status.innerText = '';
      // }, 1000);
    }
  );
};

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
} 

document.addEventListener('DOMContentLoaded', restoreOptions);
document.getElementById('save-options').addEventListener('click', saveOptions);