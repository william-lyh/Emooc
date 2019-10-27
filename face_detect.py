import requests
import json
import os

subscription_key = "3dbd88257b0248d0a7cbbaf782b98a64"
assert subscription_key
headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': subscription_key}

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion',
}

def detect_face(img_name):
    """Use Azure to analyze facial expression"""
    image_path = os.path.join('images/' + img_name)
    image_data = open(image_path, 'rb')

    response = requests.post(face_api_url, params=params,
                         headers=headers, data=image_data)
    response_json = response.json()
    
    try:
        emotion_dic = response_json[0]['faceAttributes']['emotion']
    except (IndexError, KeyError):
        '''When no face is detected, catch error'''
        return None

    return emotion_dic

def analyze_image():
    '''Analyze images captured for result'''
    folder_path = os.path.join('images/')
    image_num = len(os.listdir(folder_path))
    image_id = 1
    round = image_num//5
    x_list, y_list = [], []

    for round_count in range(round):
        score_dic = {1: 0, 0.5: 0, 0: 0}
        for count in range(0, 5):
            emotion_dic = detect_face(str(image_id)+'.jpg')
            if emotion_dic is not None:
                score_dic[1] += emotion_dic['disgust'] + emotion_dic['fear'] + emotion_dic['surprise'] + emotion_dic['sadness'] + emotion_dic['neutral']
                score_dic[0.5] += emotion_dic['neutral'] * 1.05
                score_dic[0] += emotion_dic['happiness'] + emotion_dic['contempt']
            image_id += 1
        x_list.append((round_count + 1) * 10 )
        y_list.append(max(score_dic, key=lambda x: score_dic[x]))
    
    return (x_list, y_list)
