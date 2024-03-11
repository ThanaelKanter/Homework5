import numpy as np 
def separate_letters(strings):
    separated_strings = []
    for string in strings:
        char_list = list(string)
        separated_strings.append(' '.join(char_list))
    result_array = np.array(separated_strings)
    
    return result_array
array_of_strings = ["I'm", "going", "insane"]
result = separate_letters(array_of_strings)
print(result)