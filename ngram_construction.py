def construct_trigrams(all_data):
    all_possible_trigrams = []
    for a_sentence in all_data:
        for i in range(0, len(a_sentence) - 2, 1):
            all_possible_trigrams.append(([a_sentence[i], a_sentence[i+1]], a_sentence[i+2]))

    return (all_possible_trigrams)


def construct_pentagram(all_data):
    all_possible_pentagrams = []
    for a_sentence in all_data:
        for i in range(0, len(a_sentence) - 5, 1):
            all_possible_pentagrams.append(((a_sentence[i], a_sentence[i+1], a_sentence[i+2], a_sentence[i+3], a_sentence[i+4]), a_sentence[i+5]))
  
    return all_possible_pentagrams