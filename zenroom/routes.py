from flask import jsonify, request
from zenroom import app
# import pywhatkit
import datetime
import openai


from handlers import home, paths, dialougeflow, login,diary,community,diet

app.config['SECRET_KEY'] = '5ShWn8iqyeYU2imQHtCRT3BlbkFJXvKvaV0i313dBwgigKTdWtj@161107'

openai.api_key = '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'

email= "xyz@gmail.com",
password= "xyz123"


messages = [
    {"role": "system", "content": "You are a kind helpful assistant for assisting people for mental fitnesss and mental health."},
]




global data




@app.route('/runbook', methods=['POST'])
def runbook():
    message = request.form['message']
    command=message
    if 'play' in command:
        words_to_replace = ["play", "music",'song','play the song','hello','hi']
        for word in words_to_replace:
            command = command.replace(word,"")
        response_message="ok,playing the song for you on youtube"
#         pywhatkit.playonyt(command)
        return jsonify(response_message)
        
    elif 'time' in command:
        now = datetime.datetime.now()
        day_name = now.strftime("%A")
        day_num = now.strftime("%d")
        month = now.strftime("%B")
        hour = now.strftime("%H")
        minute = now.strftime("%M")
        response_message = "Today is " + day_name + " " + day_num + " " + month + " and the time is " + hour + ":" + minute
        return jsonify(response_message)
    
    elif 'quit' in command or "end" in command:
        response_message="Thankyou"
        return jsonify(response_message)
    
    else:
        message = command
        if message:
            try:
                if len(message.split()) > 80:
                    raise ValueError("Input contains more than 45 words. Please try again.")
                messages.append({"role": "user", "content": message})
                chat = openai.Completion.create(
                    model="text-davinci-002", prompt=f"{messages[-1]['content']} Assistant: ", max_tokens=1024
                )
            except ValueError as e:
                print(f"Error: {e}")
        reply = chat.choices[0].text
        response_message=f"{reply}"
        messages.append({"role": "assistant", "content": reply}) 
        return jsonify(response_message)

