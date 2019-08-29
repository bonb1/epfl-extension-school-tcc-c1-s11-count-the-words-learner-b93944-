text_file = open("counttheword.txt")

content = text_file.read()
words = content.strip()
clean = words.split()
number = len(words.split())


print("There are " + str(number) + " words in the text.")

change = content.replace("is", "should be").upper()
print(change)


text_file.close()