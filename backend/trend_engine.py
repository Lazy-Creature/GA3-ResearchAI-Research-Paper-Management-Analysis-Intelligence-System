from collections import Counter

def emerging_topics(papers):
    all_topics = []
    for p in papers:
        all_topics += p.topics

    counts = Counter(all_topics).most_common(10)
    return [f"{t} ({c} papers)" for t,c in counts]
