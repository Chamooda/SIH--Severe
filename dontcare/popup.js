// Inject a button into the web page that calls the fetchData() function when clicked.
const button = document.createElement("button");
button.textContent = "Fetch Data";
button.addEventListener("click", async () => {
  const data = await fetchData();
  // console.log(data);
  // Display the data from the API to the user.
  alert(JSON.stringify(data));
});

// content.js

chrome.tabs.query({ active: true, currentWindow: true }, async (tabs) => {
  var tab = tabs[0];
  urls = tab.url;
  // console.log(urls);
});

async function chrome_tab(tabs) {
  var tabs = chrome.tabs.query({ active: true, currentWindow: true });
  tabs = tabs[0];

  console.log(5);
  console.log(urls);
  // a = urls;
  console.log(34);
}

document.body.appendChild(button);
async function fetchData() {
  var st = urls.replaceAll("/", "  ");
  console.log(st);
  const url = "https://dontcare-atot.onrender.com/urls/" + st;
  const response = await fetch(url);
  console.log(urls);
  const data = await response.json();
  return data;
}
