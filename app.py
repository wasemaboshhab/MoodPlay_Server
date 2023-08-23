from flask import Flask, request, jsonify
from deepface import DeepFace

app = Flask(__name__)


@app.route('/test')
def test_deep_face_emotions():
    image_path = "images/temp_image.jpg"
    face_analysis = DeepFace.analyze(img_path=image_path,actions=['emotion'])
    face_emotion = face_analysis[0]["dominant_emotion"]
    return jsonify(mod=face_emotion)


@app.route('/', methods=['POST'])
def analyze_mood():
    if 'image' not in request.files:
        return "No image provided", 400

    image_file = request.files['image']

    if image_file.filename == '':
        return "No selected image", 400

    image_path = "images/ronaldo.jpg"  # Temporary image path
    image_file.save(image_path)

    face_analysis = DeepFace.analyze(img_path=image_path)
    face_emotion = face_analysis[0]["dominant_emotion"]
    print(face_emotion)

    return jsonify({
        "emotion": face_emotion
    })


if __name__ == '__main__':
    app.run()
