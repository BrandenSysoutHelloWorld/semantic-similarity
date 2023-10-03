# Import spaCy Module
import spacy

# Load spaCy _md english core model
nlp = spacy.load('en_core_web_md')

# Cast words to the _md model
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Print Similarities based on the _md model
print(f'Comparing: {word1} with {word2}\n', word1.similarity(word2)) # Compare 'cat' with 'monkey'
print(f'Comparing: {word3} with {word2}\n', word3.similarity(word2)) # Compare 'banana' with 'monkey'
print(f'Comparing: {word3} with {word1}\n', word3.similarity(word1)) # Compare 'banana' with 'cat'

# NOTE - My First Note
note1 = f'''-------------------------------------------------------------------------\nNOTE: 
What I founded interesting about the similarities between cat, monkey and banana ...

    When comparing {word1} and {word2} I notice that the result of their similarities
    is weighted with general facts such as that their both ANIMALS(TRUE) and,    
    whether they are from the same SPECIES(false).

    While the result of {word3} and {word2} shows more of a meaningful similarity/relationship
    the interesting fact lies with that the model refers to the animals common stereotypes such as,
    {word2}s eat {word3}s. This could skew data similarities ...maybe?

    Similarities between {word1} and {word3} is significantly less than when comparing {word2} and {word3} -
    this is evident and supporting my above arguments. Where I can see that a stereotype that cats 
    eat bananas does not exist! Even though the score is low, I question even a similarity between
    {word1}s and {word3}s.'''
print(note1)

print('\n\n-------------------------------------------------------------------------\nMY EXAMPLE:')

# My Own Example
my_example_words = [
    nlp("moderator"),
    nlp("admin"),
    nlp("user"),
    nlp("guest")
]

# Compare the Similiarties between my own example words using spaCy model _md
for compare_word in my_example_words:
    for word in my_example_words:
        print(f'Comparing: {compare_word} with {word}\n', compare_word.similarity(word)) # Print the compared words results

# END-OF-FILE - Branden van Staden