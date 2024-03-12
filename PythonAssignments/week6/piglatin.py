import string

exclude = set(string.punctuation)

sentence = input('Enter a Sentence:  ').lower()

if len(sentence) >= 100:
        print("No sentences longer than 100 characters allowed!")
        raise Exception("No sentences longer than 100 characters allowed!")

words = sentence.split()

for i, word in enumerate(words):
    
        if word[0] in 'aeiou':
                words[i] = words[i] + "ay"
 
        else:
                has_vowel = False

                for j, letter in enumerate(word):

                        if letter in 'aeiou':

                                has_vowel = True
                                words[i] = word[j:] + word[:j] + "ay"
                                break

                if(has_vowel == False):
                        
                        words[i] = words[i]+ "ay"

pig_latin = ' '.join(words)

pig_latin = ''.join(ch for ch in pig_latin if ch not in exclude)

print("Pig Latin:",pig_latin)