from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter


def read_files():
    """
    The following function is used to read the files from the Qualifications folder.
    :return: list of texts
    """
    number_of_files = 97
    list_of_texts = []
    for i in range(0, number_of_files):
        with open('Qualifications/{}.txt'.format(str(i)), encoding="utf-8", errors="ignore") as file:
            lines = file.readlines()
        list_of_texts.append(lines)
    return list_of_texts


def tranform_to_text_to_unigrams(list_of_texts):
    """
    The following function transforms the qualification texts to unigrams.
    :param list_of_texts: list of texts
    :return: list of unigrams
    """
    tokenizer = RegexpTokenizer(r'\w+')
    list_of_unigrams = []
    for text in list_of_texts:
        joined_text = ",".join(text)
        text_unigrams = tokenizer.tokenize(joined_text)
        list_of_unigrams.append(text_unigrams)
    return list_of_unigrams


def process_unigrams(list_of_unigrams):
    """
    Using that function you are able to remove english stopwords and make lowers all words.

    :param list_of_unigrams: list of unigrams
    :return: list of processed unigrams
    """
    processed_unigrams = []
    english_stopwords = set(stopwords.words('english'))
    for text_unigrams in list_of_unigrams:
        processed_unigrams.append(
            [word.lower() for word in text_unigrams if word not in english_stopwords and not word.isdigit()])
    return processed_unigrams


def create_bow(processed_unigrams):
    """
    Using tha function you are able to create bag of words for each text.

    :param processed_unigrams: list of filtered unigrams
    :return: list of bag of words
    """
    list_of_bags = [Counter(unigram) for unigram in processed_unigrams]
    return list_of_bags


list_of_texts = read_files()
list_of_unigrams = tranform_to_text_to_unigrams(list_of_texts=read_files())
processed_unigrams = process_unigrams(list_of_unigrams)
print(list_of_unigrams[78])
print(" ")
print(" ")
print(processed_unigrams[78])
print(" ")
print(" ")
list_of_bags = create_bow(processed_unigrams)
print(list_of_bags[78])
