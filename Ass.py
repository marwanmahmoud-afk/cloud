import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    # Filter out stop words and punctuation
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    return filtered_words

def calculate_word_frequency(words):
    word_freq = Counter(words)
    return word_freq

def main():
    # Read content from the file
    text = read_file("random_paragraphs.txt")

    # Remove stop words using NLTK
    clean_words = remove_stopwords(text)

    # Calculate word frequency
    word_freq = calculate_word_frequency(clean_words)

    # Display word frequency to the console
    for word, freq in word_freq.most_common():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
