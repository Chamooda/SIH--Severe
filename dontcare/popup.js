// content.js

// Inject a button into the web page that calls the fetchData() function when clicked.
const button = document.createElement("button");
button.textContent = "Fetch Data";
button.addEventListener("click", async () => {
  const data = await fetchData();

  // Display the data from the API to the user.
  alert(JSON.stringify(data));
});
document.body.appendChild(button);
async function fetchData() {
  const url = "https://dontcare-atot.onrender.com/urls/yash";
  const response = await fetch(url);
  const data = await response.json();
  return data;
}
