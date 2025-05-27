## 🚀 Running the Flask Sticker API

### 1. Set Up Your Python Environment

If you don't have Python installed, download it from [python.org](https://www.python.org/).  
Then install Flask:

```bash
pip install flask
```

### 2. Run the API

Navigate to your project folder (e.g., `sticker-API`) and run:

```bash
python app.py
```

You should see something like:

```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: XXX-XXX-XXX
```

This means your API is running locally at:  
👉 **http://127.0.0.1:5000**

---

## 💡 How to Use Your API in a Website

Update your JavaScript to use your local sticker API instead of an external one like Tenor.

```javascript
// Async requesting function
function httpGetAsync(theUrl, callback){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            callback(xmlHttp.responseText);
        }
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

// Callback for your stickers
function myStickersCallback(responsetext){
    var response_objects = JSON.parse(responsetext);
    var stickers = response_objects;

    // Display the first sticker
    if (stickers.length > 0) {
        var baseApiUrl = "http://127.0.0.1:5000"; // Change this if hosted online
        document.getElementById("preview_gif").src = baseApiUrl + stickers[0]["url"];
        document.getElementById("share_gif").src = baseApiUrl + stickers[0]["url"];
    } else {
        console.log("No stickers found!");
    }
}

// Function to call your sticker API
function grab_data(){
    var my_sticker_api_url = "http://127.0.0.1:5000/api/stickers";
    httpGetAsync(my_sticker_api_url, myStickersCallback);
}

// Start the flow
grab_data();
```
