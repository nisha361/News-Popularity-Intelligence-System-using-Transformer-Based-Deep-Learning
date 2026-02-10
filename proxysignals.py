import numpy as np
from textblob import TextBlob
import textstat

URGENCY_WORDS = [
    "breaking", "urgent", "alert", "shocking",
    "exclusive", "just in", "developing","now", "today"
]

def urgency_score(text, max_hits=3):
    text = text.lower()
    count = sum(word in tect for word in URGENCY_WORDS)
    return min(count / max_hits, 1.0)

def sentiment_intensity(text):
    return abs(TextBlob(text).sentiment.polarity)

def lexical_diversity(text):
    words = text.split()
    if not words:
        return 0
    return len(set(words)) / len(words)

def readability_score(text):
   score = textstat.flesch_reading_ease(text)
    return min(max(score / 100, 0),1)

def length_score(text):
    return min(len(text.split()) / 100, 1.0)

def popularity_score(signals):
    return (
        0.25*signals["urgency"] +
        0.25*signals["sentiment"] +
        0.20*signals["lexical"] +
        0.15*signals["readability"]+
        0.15*signals["length"] 
                      )
