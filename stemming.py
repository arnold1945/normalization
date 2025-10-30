"""
👨‍💻 Stemming Task

Your goal is to:
1️⃣ Read the content of either story1.txt or story2.txt.
2️⃣ Apply regex with re.sub() to remove:
    - HTML tags (e.g. <div>...</div>)
    - URLs
    - Hashtags (#), asterisks (*), excessive punctuation (e.g. !!!, ???)
    - Extra whitespace

3️⃣ Tokenize the cleaned text into words using nltk.word_tokenize.
4️⃣ Remove stopwords using nltk.corpus.stopwords.
5️⃣ Apply stemming using nltk.stem.PorterStemmer to reduce each word to its root form.
6️⃣ Print out the list of stemmed words.

📌 Hints:
- Remember to import the required NLTK modules.
- Think about what patterns to use in your regex for URLs and HTML tags.
- Inspect intermediate results to ensure your cleaning is working!

Write your code below this string.
"""
import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

nltk.download('punkt')      # Tokenizer models returns True
nltk.download('stopwords')  # List of common stopwords returns True
nltk.download('averaged_perceptron_tagger')

file = open('story2.txt')
text_from_file = file.read()
file.close()

print('========2️⃣ Apply regex with re.sub() to remove:====')
## removed 3 dots between Impossible and `!`
clean_story = re.sub(r'(Impossible)\.+\!',r'\1!', text_from_file)
# print(clean_story)
##replaced that 1 & with and
clean_story =re.sub(r'(&)', 'and', clean_story)
# print(clean_story)
## removed `->`
clean_story = re.sub(r'->', '', clean_story)
# print(clean_story)
## removed anything with a % and #
clean_story = re.sub(r'[%#]', '', clean_story)
# print(clean_story)
## removed unnecessary `?` duplicates
clean_story = re.sub(r'\?{2,}','?', clean_story)
# print(clean_story)
## period added after ("Test")
clean_story = re.sub(r'(\))(?=\s|$)', r'\1.', clean_story)
# print(clean_story)
## removeed whitespaces that are indented twice or more
clean_story = re.sub(r'\ {2,}', ' ', clean_story)
# print(clean_story)
## removed whitespace before `Debbuging` using \t for tabs
clean_story = re.sub(r'[ \t]+(?=Debugging)', '', clean_story)
print(clean_story)
## hyperlink removed
clean_story = re.sub(r'(https?://)', r'\1' + chr(0x200b), clean_story)
print(clean_story)
##removed the extra newlines
clean_story = re.sub(r'\n+', '\n', clean_story)
print(clean_story)


