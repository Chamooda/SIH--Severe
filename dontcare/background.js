// Inject a button into the web page that calls the fetchData() function when clicked.
const button = document.createElement("button");
button.textContent = "Fetch Data";
button.addEventListener("click", async () => {
  try {
    const data = await fetchData();

    // Display the data from the API to the user.
    alert(JSON.stringify(data));
  } catch (error) {
    // Handle the error here.
    console.log(error);
  }
});

// content.js
chrome.tabs.query({ active: true, currentWindow: true }, async (tabs) => {
  var tab = tabs[0];
  urls = tab.url;
  console.log(urls);
});

// async function chrome_tab(tabs) {
//   var tabs = chrome.tabs.query({ active: true, currentWindow: true });
//   tabs = tabs[0];
//   // var urls = tabs.url;
//   console.log(5);
//   console.log(urls);
//   console.log(34);
// }

document.body.appendChild(button);
async function fetchData() {
  const url = "https://dontcare-atot.onrender.com/urls/" + urls;
  const response = await fetch(url);
  const data = await response.json();
  return data;
}

let data = new FormData();
data.append("point", urls);
fetch("https://dontcare-atot.onrender.com/", {
  method: "POST",
  body: data,
}).then((response) => {
  if (response) {
    console.log("yes");
  } else {
    console.log("no");
  }
});
