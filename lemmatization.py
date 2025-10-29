"""
👨‍💻 Lemmatization Task

Your goal is to:
1️⃣ Read the content of either story1.txt or story2.txt.
2️⃣ Apply regex with re.sub() to remove:
    - HTML tags (e.g. <div>...</div>)
    - URLs
    - Hashtags (#), asterisks (*), excessive punctuation (e.g. !!!, ???)
    - Extra whitespace

3️⃣ Tokenize the cleaned text into words using nltk.word_tokenize.
4️⃣ Remove stopwords using nltk.corpus.stopwords.
5️⃣ Tag each word with its part of speech using nltk.pos_tag.
6️⃣ Map POS tags to WordNet tags so thee lemmatizer can use them.
7️⃣ Apply lemmatization using nltk.stm.WordNetLemmatizer, passing the correct POS.
8️⃣ Print out the list of lemmatized words.

📌 Hints:
- You’ll need a helper function to convert Treebank POS tags to WordNet POS tags.
- Check your intermediate outputs (POS tags, lemmatized results).

Write your code below this string.
"""
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
file = open('story1.txt')
text_from_file = file.read()
file.close()

print('=====================CLEAN_STORY BELOW ========================')
#removed extra `!`
clean_story = re.sub(r'!{2,}', '!', text_from_file)
# print(clean_story)
##removed URL, #, * and emojis
clean_story = re.sub(r'[✅|💻|💡|_|#|*|-]', '', clean_story)
# print(clean_story)
#removed html elements
clean_story = re.sub(r'<.?div>', '', clean_story)
# print(clean_story)
clean_story = re.sub(r'  {2,}', '', clean_story)
# print(clean_story)
clean_story = re.sub(r'\n+', '\n', clean_story)
# print(clean_story)
## removed the other extra `.`
clean_story = re.sub(r'\.{3,}', '.', clean_story)
# print(clean_story)
## removed white space
clean_story = re.sub(r'(!")\s+\.', r'\1.', clean_story)
print(clean_story)




print('===========TOKENIZE STORY TO WORDS===================')

## 3.) tokenize story to words

tok_words = word_tokenize(clean_story)
#code below removes the punctuation marks before doing the stopwords
tok_words = [word.lower() for word in tok_words if word.isalpha()]
print(tok_words)
print('==================LIST OF EXISTING STOPWORDS===================')

## 4.)
#this is establishing what the pre-listed stopwords are
stop_words = set(stopwords.words('english'))
print(stop_words)

print('=============STOP WORDS REMOVED BELOW=============================')
#code below is saying to return the words not listed in stopwords
without_stopwords = [word for word in tok_words if word not in stop_words]

print(without_stopwords)

print('====================POS_TAG BELOW===========================')
## 5.)

tagged_words = pos_tag(without_stopwords)

print(tagged_words)

print('==================MAPPING POS TAGS BELOW===================')
## wordnet POS TAGS == n, v, a, r == noun, verb, adjective, adverb
## 6️⃣ Map POS tags to WordNet tags so the lemmatizer can use them.

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


##7️⃣ Apply lemmatization using nltk.stm.WordNetLemmatizer, passing the correct POS.

lemmatizer = WordNetLemmatizer()

lem_words_pos = [
    lemmatizer.lemmatize(word, get_wordnet_pos(pos_tag))
    for word, pos_tag in tagged_words
]
 
##8️⃣ Print out the list of lemmatized words.

print(lem_words_pos)   
        



