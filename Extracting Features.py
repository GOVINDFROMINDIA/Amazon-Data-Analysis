import nltk
from nltk.tokenize import sent_tokenize

with open('reviews.txt', 'r', encoding='utf-8') as file:
    reviews = file.read()

sentences = sent_tokenize(reviews)

features = []

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tagged_tokens = nltk.pos_tag(words)
    facts = [word for word, tag in tagged_tokens if tag.startswith('NN') or tag.startswith('VB')]
    if facts:
        features.append('• ' + ' '.join(facts))

with open('features.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(features))
