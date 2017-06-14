def words(the_words):
    '''
    Counts the occurrences or characters in a word
    '''
    word_dict = {}
    word_list = the_words.replace('\t', " ").split()

    for w in word_list:
        if w in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            word_dict[int(w)] = word_list.count(w)
        else:
            word_dict[w] = word_list.count(w)
    return word_dict
