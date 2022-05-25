def get_accuracy(words, typed_words):
    correct_characters = 0
    for index, character in enumerate(words):
        try:
            if (typed_words[index] == character):
                correct_characters += 1
        except:
            pass
    accuracy = round(correct_characters / len(words) * 100, 2)
    return str(accuracy)
