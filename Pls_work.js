// Define the URL of the API endpoint
const apiUrl = 'http://127.0.0.1:5000/urls/asad'; // Replace with the actual API URL

// Use the fetch function to make the GET request to the API
fetch(apiUrl)
  .then(response => {
    // Check if the response status is OK (200)
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    // Parse the response body as JSON
    return response.json();
  })
  .then(data => {
    // Do something with the JSON data
    console.log(data);

    // You can access specific properties of the JSON data like this:
    // const value = data.propertyName;
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('Fetch error:', error);
  });
