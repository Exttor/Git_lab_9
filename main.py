def sort_sentence(sentence):
    sl = sentence.lower()
    lsl = sl.split(" ")
    lsl.sort(key=len)
    sl = " ".join(lsl).capitalize()
    return sl
