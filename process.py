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

total_texts = read_files()
print(total_texts[89])

