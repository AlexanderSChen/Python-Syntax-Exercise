def print_upper_words(words, must_start_with):
    # capitalized_words = []
    # for required_start in must_start_with:
    #     for word in words:
    #         if word.startswith(required_start):
    #             print(word.upper())
    for word in words:
        for required_start in must_start_with:
            if word.startswith(required_start):
                print(word.upper())
                # capitalized_words.append(word.upper())
    # capitalized_words.reverse()
    # for capitalized in capitalized_words:
    #     print(capitalized)
    # print(capitalized_words)

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})

