def get_accuracy(words, typed_words):
    correct_characters = 0
    for index, character in enumerate(words):
        try:
            if typed_words[index] == character:
                correct_characters += 1
        except:
            pass
    accuracy = round(correct_characters / len(words) * 100, 2)
    return str(accuracy)


# def get_time(starting_time, ending_time):
#     time_spent = round(ending_time - starting_time)
#     return time_spent
#
#
# def get_wpm(starting_time, ending_time, typed_words):
#     time_spent = get_time(starting_time, ending_time)
#
#     wpm = round(((len(typed_words))/5) / (time_spent/60))
#
#     return str(wpm)
