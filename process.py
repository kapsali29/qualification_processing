from nltk.tokenize import RegexpTokenizer


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


list_of_texts = read_files()
list_of_unigrams = tranform_to_text_to_unigrams(list_of_texts=read_files())
print(list_of_unigrams[78])
