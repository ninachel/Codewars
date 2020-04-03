def spin_words(sentence):
    sentence_array = sentence.split()
    answer = []
    for i in sentence_array:
        if len(i) >= 5:
            answer.append(i[::-1])
        else:
            answer.append(i)
    return ' '.join(answer)
