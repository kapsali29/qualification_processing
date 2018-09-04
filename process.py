from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter
import numpy as np


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


def build_feature_matrix(list_of_bags):
    """
    Using that function you are able to build the feature matrix.

    :param list_of_bags: list of text bows
    :return: feature matrix
    """
    features_list = []
    for bag in list_of_bags:
        features_list += list(bag.keys())
    features = list(set(features_list))
    feature_matrix = np.zeros((len(list_of_bags), len(features)))
    for i in range(0, feature_matrix.shape[0]):
        current_bow = list_of_bags[i]
        for j in range(0, feature_matrix.shape[1]):
            if features[j] in current_bow.keys():
                feature_matrix[i, j] = current_bow[features[j]]
            else:
                feature_matrix[i, j] = 0
    return feature_matrix


def calculate_tfidf(feature_matrix):
    """
    Using that function we are able to calculate the tfidf feature matrix.

    :param feature_matrix: tf feature matrix
    :return: tfidf feature matrix
    """


list_of_texts = read_files()
list_of_unigrams = tranform_to_text_to_unigrams(list_of_texts=read_files())
processed_unigrams = process_unigrams(list_of_unigrams)
list_of_bags = create_bow(processed_unigrams)
build_feature_matrix(list_of_bags)
