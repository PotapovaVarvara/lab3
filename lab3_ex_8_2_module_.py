def get_repeat_count(numbers, numbers_to_search):
    num_dictionary = {numbers_to_search[0]: 0,
                      numbers_to_search[1]: 0,
                      numbers_to_search[2]: 0,
                      numbers_to_search[3]: 0,
                      numbers_to_search[4]: 0}

    for i in range(0, 100):
        if numbers[i] == numbers_to_search[0]:
            num_dictionary[numbers_to_search[0]] = num_dictionary.get(numbers_to_search[0]) + 1
        if numbers[i] == numbers_to_search[1]:
            num_dictionary[numbers_to_search[1]] = num_dictionary.get(numbers_to_search[1]) + 1
        if numbers[i] == numbers_to_search[2]:
            num_dictionary[numbers_to_search[2]] = num_dictionary.get(numbers_to_search[2]) + 1
        if numbers[i] == numbers_to_search[3]:
            num_dictionary[numbers_to_search[3]] = num_dictionary.get(numbers_to_search[3]) + 1
        if numbers[i] == numbers_to_search[4]:
            num_dictionary[numbers_to_search[4]] = num_dictionary.get(numbers_to_search[4]) + 1

    for key, value in num_dictionary.items():
        print("Amount of " + str(key) + " is: " + str(value))
