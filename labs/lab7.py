import textstat

print("Enter your text below to receive your text stats.")

data = input()

print(
"Character Count:" + str(textstat.char_count(data, ignore_spaces=True)) + "\n"
"Letter Count:" + str(textstat.letter_count(data, ignore_spaces=True)) + "\n"
"Sentence Count:" + str(textstat.sentence_count(data)) + "\n"
"Syllable Count:" + str(textstat.syllable_count(data)) + "\n"
"Grade Level:" + str(textstat.text_standard(data)) 
)

