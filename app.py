# Import the Flask framework and other necessary modules
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

# Create a Flask web application instance
app = Flask(__name__)
CORS(app) 
# Define the directory where your sticker images are stored
# This assumes your 'stickers' folder is in the same directory as app.py
STICKERS_DIR = 'stickers'

# --- API Endpoint to List All Stickers ---
# This route will respond to GET requests at '/api/stickers'
@app.route('/api/stickers', methods=['GET'])
def list_stickers():
    """
    Returns a JSON list of all available sticker names and their URLs.
    """
    sticker_files = []
    # Check if the stickers directory exists
    if os.path.exists(STICKERS_DIR) and os.path.isdir(STICKERS_DIR):
        # Loop through all files in the stickers directory
        for filename in os.listdir(STICKERS_DIR):
            # Check if the file is an image (you might want more robust checking)
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                # Construct the full URL for the sticker
                # This assumes your API will be accessible at some_domain/api/stickers/sticker_name.png
                # For local testing, it will be http://127.0.0.1:5000/api/stickers/sticker_name.png
                sticker_url = f'/api/stickers/{filename}'
                sticker_files.append({
                    'name': os.path.splitext(filename)[0], # Sticker name without extension
                    'filename': filename,
                    'url': sticker_url
                })
    else:
        # If the directory doesn't exist, return an error message
        return jsonify({"error": "Stickers directory not found."}), 500

    # Return the list of stickers as a JSON response
    return jsonify(sticker_files)

# --- API Endpoint to Serve Individual Stickers ---
# This route will respond to GET requests at '/api/stickers/<filename>'
# The <filename> part is a variable that captures the requested file name
@app.route('/api/stickers/<path:filename>', methods=['GET'])
def get_sticker(filename):
    """
    Serves a specific sticker image file from the STICKERS_DIR.
    """
    # Use send_from_directory to securely serve files from the specified directory
    # This prevents users from accessing files outside the 'stickers' folder
    try:
        return send_from_directory(STICKERS_DIR, filename)
    except FileNotFoundError:
        # If the file is not found, return a 404 error
        return jsonify({"error": "Sticker not found."}), 404

# --- Main entry point to run the Flask application ---
# This ensures the app only runs when the script is executed directly
if __name__ == '__main__':
    # Run the app in debug mode (good for development, shows errors in browser)
    # For production, set debug=False
    app.run(debug=True)
