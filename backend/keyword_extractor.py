import re
from collections import Counter

STOPWORDS = set("the and is are of to for with on in a an this that as by from it be been was were".split())

def extract_keywords(text, top_k=10):
    words = re.findall(r"[A-Za-z]{4,}", text.lower())
    words = [w for w in words if w not in STOPWORDS]
    return [w for w,_ in Counter(words).most_common(top_k)]
