from flask import Flask, request, jsonify
from deepface import DeepFace
import os

app = Flask(__name__)


@app.route('/test')
def test_deep_face_emotions():
    image_path = "images/temp_image.jpg"
    face_analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'])
    face_emotion = face_analysis[0]["dominant_emotion"]
    return jsonify(mod=face_emotion)


@app.route('/analyze', methods=['POST'])
def analyze_mood():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'})

    image_file = request.files['image']

    if image_file.filename == '':
        return jsonify({'error': 'No selected image'})

    # image_path : to save/image.jpg
    image_path = "images"
    image_file.save(image_path)
    face_analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'])
    face_emotion = face_analysis[0]["dominant_emotion"]
    return jsonify(mod=face_emotion)

    # if image_file:
    #     filename = os.path.join(app.config['image'], image_file.filename)
    #     image_file.save(filename)


    # image_path = "images/ronaldo.jpg"  # Temporary image path
    # image_file.save(image_path)


if __name__ == '__main__':
    app.run()
