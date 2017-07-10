

def word_count(test_file):

    open_file = open(test_file)

    word_counts = {}

    for line in open_file:
        line = line.rstrip()
        line = line.split(" ")
        for word in line:
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

    open_file.close()

print word_count("test.txt")
#print word_count("twain.txt")
