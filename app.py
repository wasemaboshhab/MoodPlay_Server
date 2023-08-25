from flask import Flask, request, jsonify
from deepface import DeepFace

app = Flask(__name__)


def filter_unnecessary_emotion_and_take_close_one(emotion_dictionary):
    del emotion_dictionary["fear"]
    del emotion_dictionary["disgust"]
    second_close_emotion = max(emotion_dictionary, key=emotion_dictionary.get)
    return second_close_emotion

    # print(second_dominant_emotion)
    # return jsonify(mod=emotion_dictionary[max_key])
    # max_value = emotion_dictionary[max_key]
    # for key, value in emotion_dictionary.items():
    #     print(f"key: {key} , value: {value}")
    # print("Key with highest value:", max_key)
    # print("Highest value:", max_value)


@app.route('/', methods=['POST', 'GET'])
def analyze_mood():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'})

    image_file = request.files['image']

    if image_file.filename == '':
        return jsonify({'error': 'No selected image'})

    # image_path : to save/image.jpg
    image_path = "temp_image.jpg"
    image_file.save(image_path)
    face_analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'])
    face_emotion = face_analysis[0]["dominant_emotion"]
    if face_emotion == 'fear' or face_emotion == 'disgust':
        emotion_dictionary = face_emotion[0]['emotion']
        face_emotion = filter_unnecessary_emotion_and_take_close_one(emotion_dictionary)

    return jsonify(mod=face_emotion)


if __name__ == '__main__':
    app.run()