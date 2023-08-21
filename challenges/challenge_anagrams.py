def quicksort_chars(word):
    if len(word) <= 1:
        return word

    pivot = word[len(word) // 2]
    left = "".join([char for char in word if char < pivot])
    middle = "".join([char for char in word if char == pivot])
    right = "".join([char for char in word if char > pivot])

    return quicksort_chars(left) + middle + quicksort_chars(right)


def is_anagram(first_string, second_string):
    string1 = quicksort_chars(first_string.lower())
    string2 = quicksort_chars(second_string.lower())
    if not string1 or not string2:
        return string1, string2, False
    if string1 == string2:
        return string1, string2, True
    else:
        return string1, string2, False
