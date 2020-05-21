import re

def read_sentences(file_path):
    all_read_lines = []
    all_final_lines = []
    chapter_title = ['CATELYN', 'JON', 'ARYA', 'EDDARD', "TYRION", "BRAN"]
    punctuation_list = ["\n", ",", '"', ".", "..", "...", "?", ";", "' ", "!", "-"]
    
    print("reading file {}".format(file_path))
    with open(file_path, "r") as f:
        rx = '(\n)*'
        rx_space = "  +"
        all_read_lines = f.read().replace("killlllllllllled", "killed").replace("hissssssssssss", "his")
        
        for title in chapter_title:
            all_read_lines = all_read_lines.replace(title, " ")
        for punc in punctuation_list:
            all_read_lines = all_read_lines.replace(punc, " ")

        all_read_lines = re.sub(rx, "", all_read_lines)
        all_read_lines = re.sub(rx_space, " ", all_read_lines)
        all_read_lines = [all_read_lines.lower()]
        
    for an_element in all_read_lines:
        if an_element != '':
            all_final_lines.append(an_element.strip())
    return all_final_lines

def word_tokenizer(all_sentences):
    tokenized_sentences = []
    for a_sentence in all_sentences:
        tokenized_sentences.append(a_sentence.split(" "))

    final_tokenized_sentences = []
    for a_sentence in tokenized_sentences:
        temp_sent = []
        for a_word in a_sentence:
            if a_word != "":
                temp_sent.append(a_word)
        final_tokenized_sentences.append(temp_sent)

    return final_tokenized_sentences

