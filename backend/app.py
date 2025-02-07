from flask import Flask, request, jsonify
import numpy as np
from find_bugholes import find_bugholes
import cv2
import base64
from io import BytesIO
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/process_image", methods=["POST"])
def process_image():
    try:
        # Get image and threshold from request
        data = request.json
        image_data = data.get("image")
        threshold = data.get("threshold", 60)

        # Decode base64 image
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes)).convert("L")
        concrete_image = np.array(image)

        # Process the image
        num_bugholes, locations = find_bugholes(concrete_image, threshold)

        return jsonify({"num_bugholes": num_bugholes, "locations": locations})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
