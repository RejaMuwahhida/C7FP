import requests
import json

def emotion_detector(text_to_analyse):
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    emotions = formatted_response['emotionPredictions']['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    emotion_scores = [anger_score,disgust_score,fear_score,joy_score,sadness_score]
    highest_score = max(emotion_scores)

    return {'anger': anger_score,'disgust': disgust_score,'fear': fear_score,
            'joy': joy_score,'sadness': sadness_score,'dominant_emotion': highest_score }


            {'emotionPredictions': 
              [
                {'emotion': {'anger': 0.0132405795, 'disgust': 0.0020517302, 'fear': 0.009090992, 'joy': 0.9699522, 'sadness': 0.054984167},
                 'target': '', 
                 'emotionMentions': [
                    {'span': {'begin': 0, 'end': 26, 'text': 'I love this new technology'}, 'emotion': {'anger': 0.0132405795, 'disgust': 0.0020517302, 'fear': 0.009090992, 'joy': 0.9699522, 'sadness': 0.054984167}}
                    ]
                }
              ], 
              'producerId': {'name': 'Ensemble Aggregated Emotion Workflow', 'version': '0.0.1'}
            }

            from emotion_detection import emotion_detector

            import requests
import json

def emotion_detector(text_to_analyse):
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    
    emotions = formatted_response['emotionPredictions'][0]
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    emotion_scores = [anger_score,disgust_score,fear_score,joy_score,sadness_score]
    highest_score = max(emotion_scores) 

    return ({
        'anger': anger_score,'disgust': disgust_score,'fear': fear_score,
        'joy': joy_score,'sadness': sadness_score,'dominant_emotion': highest_score
    })


    