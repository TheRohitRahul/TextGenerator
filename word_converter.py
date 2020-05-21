def make_word_num_relation_file(tokenized_words):
    single_word_list = []
    for a_sentence in tokenized_words:
        for a_word in a_sentence:
            single_word_list.append(a_word)
    single_word_list = list(set(single_word_list))

    '''
    Removing empty words
    '''
    final_single_word_list = []
    for a_word in single_word_list:
        if a_word != "":
            final_single_word_list.append(a_word)

    word_to_num = {a_word : ind for ind, a_word in enumerate(final_single_word_list)}

    num_to_word = {ind : a_word for ind, a_word in enumerate(final_single_word_list)}

    return word_to_num, num_to_word, len(final_single_word_list)
