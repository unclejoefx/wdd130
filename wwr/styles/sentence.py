# Create a list of strings and assign
# the list to a variable named words.
import random
#words = ["boy", "girl", "cat", "dog", "bird", "house"]
#word = random.choice(words)
#given = "Uwa"
#middle = "Joseph"
#surname = "Uwa"

#full_name = f"{given} {middle} {surname}"
#print(word)
def main():
    sentence = make_sentence()
    print(sentence)

def make_sentence():
    # Call the functions here and concatenate their return values
    sentence = get_determiner() + " " + get_noun() + " " + get_verb() + " " + get_prepositional_phrase()
    return sentence

def get_determiner():
    # Your code here
    pass

def get_noun():
    # Your code here
    pass

def get_verb():
    # Your code here
    pass

def get_preposition():
    # Your code here
    pass

def get_prepositional_phrase():
    # Call the functions here and concatenate their return values
    phrase = get_preposition() + " " + get_determiner() + " " + get_noun()
    return phrase

# Call the main function to start the program
main()

