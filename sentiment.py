from textblob import TextBlob

def Sentimet_Analysis(Sentence):
    Polarity = round(TextBlob(Sentence).sentiment.polarity)
    if Polarity == 0:
        return "Neutral"
    elif Polarity == 1:
        return "Positive"
    elif Polarity == -1:
        return "Negative"
