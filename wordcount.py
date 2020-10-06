# put your code here.

# Assign variable to the file and open it
text_file = open("test.txt")

# print(x)


# for line in text_file:
#     line = line.rstrip().split(" ")
#     for word in line:
#         # word = word.split(" ")
#         print(word)
# list1.append(line)
# print(list1)


# text_file = "As I was going to St. Ives I met a man with seven wives Every wife had seven sacks Every sack had seven cats Every cat had seven kits Kits, cats, sacks, wives. How many were going to St. Ives?"
# print(text_file)
# Create a function (with one parameter)
# Create an empty dict variable
# Iterate over the text.txt file
# Assign the key to the value count (+1) if the key exists, if not it'll overwrite
# (adds to the dict each time) (use .get method)

# return empty dict

# Function call:
# function(argument = filename)
def word_count_dict(file):
    word_count = {}
    for line in text_file:
        line = line.rstrip().split(" ")
        for word in line:
            # word = word.split(" ")
            print(word)

            word_count[word] = word_count.get(word, 0) + 1
    # print(word_count)

    print(word_count.keys())
    for key, value in word_count.items():
        print(key, value)


word_count_dict(text_file)

