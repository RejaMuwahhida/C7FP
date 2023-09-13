from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
       
    ''' This code receives the text from the HTML interface and 
        runs emotion detection  over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    emotions = str(response.pop('dominant_emotion'))
    if response is None:
        return "Invalid input ! Try again."
    else:
        return "For the given statement, the system response is {} The dominant emotion is {}.".format(emotions,dominant_emotion)
   

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
