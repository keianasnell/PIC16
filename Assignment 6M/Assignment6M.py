from random import randint

def handler(event, context):
    
    outputSpeech = {"type": "PlainText", "text": "hello world"}
    r = {"outputSpeech": outputSpeech, "shouldEndSession": True}
    
    x = None
    y = None
    
    if event["request"]["type"] == "IntentRequest":
        if event["request"]["intent"]["name"] == "AMAZON.HelpIntent":
            outputSpeech["text"] = "This is not the help you're looking for."
    
        elif event["request"]["intent"]["name"] == "SimpleSkill":
            try:
                low = int(event["request"]["intent"]["slots"]["low"]["value"])
                except:
                    low = 0
            try:
                high = int(event["request"]["intent"]["slots"]["high"]["value"])
                except:
                    high = 10
            outputSpeech["text"] = str(randint(low,high))
                
                elif event["request"]["intent"]["name"] == "ResponseIntent":
                    try:
if x is None:
    x = int(event["request"]["intent"]["slots"]['num']['value'])
        elif y is None:
            y = int(event["request"]["intent"]["slots"]['num']['value'])
            except:
                outputSpeech["text"] = "HELLO Sorry, what's the first number?"
                r['shouldEndSession'] = False
        
        try:
            if event["request"]["intent"]["slots"]["operation"]["value"] == "add":
                outputSpeech["text"] = str(x+y)
                if event["request"]["intent"]["slots"]["operation"]["value"] == "multiply":
                    outputSpeech["text"] = x*y
        except:
            outputSpeech["text"] = "Looks like someone made a mistake."
        
        
        elif event["request"]["intent"]["name"] == "OperationIntent":
            if event["request"]["intent"]["slots"]["operation"]["value"] == "add":
                try:
                    x = int(event["request"]["intent"]["slots"]['x']['value'])
                except:
                    outputSpeech["text"] = "Sorry, what was the first number?"
                    r['shouldEndSession'] = False
                try:
                    y = int(event["request"]["intent"]["slots"]['y']['value'])
                except:
                    outputSpeech["text"] = "Sorry, what was the second number?"
                    r['shouldEndSession'] = False
                try:
                    outputSpeech["text"] = str(x+y)
                except:
                    pass
        
            elif event["request"]["intent"]["slots"]["operation"]["value"]=="multiply":
                try:
                    x = int(event["request"]["intent"]["slots"]['x']['value'])
                except:
                    outputSpeech["text"] = "Sorry, what was the first number?"
                    r['shouldEndSession'] = False
                    x = None
                try:
                    y = int(event["request"]["intent"]["slots"]['y']['value'])
                except:
                    outputSpeech["text"] = "Sorry, what was the second number?"
                    r['shouldEndSession'] = False
                    y = None
                
                try:
                    outputSpeech["text"] = str(x*y)
                except:
                    pass

response = {"version": "1.0", "response": r}
    return response
