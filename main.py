igbo_to_english = {
    "akwa": "cloth",
    "ụlọ": "house",
    "ụzọ": "road",
    "azụ": "fish",
    "chi": "god",
    "nnọọ": "hello",
    "ezi": "good",
    "anyị": "we",
    "ọtụtụ": "many",
    "nwanne": "sibling",

}

# Example of using the dictionary to translate Igbo words to English
word = "akwa"
if word in igbo_to_english:
    print(f"The English translation of '{word}' is '{igbo_to_english[word]}'.")
else:
    print(f"'{word}' not found in dictionary.")
