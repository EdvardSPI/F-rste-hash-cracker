import hashlib

md_hash_to_crack = '2f67742e1c3990db50d0a48077923916'

# Define special characters
special_characters = '!"#$%&/()='  # Add the special characters you want to check here

wordlist = open('norwegian.txt').readlines()

for word in wordlist:
    word = word.strip()

    # Check the word as is (all lowercase)
    result = hashlib.md5(word.encode()).hexdigest()
    if result == md_hash_to_crack:
        print('Found password: ' + word)
        print('Searched through ' + str(len(wordlist)) + ' words')
        break  # Exit the loop if the password is found

    # Now, check the uppercase version of the word
    uppercase_result = hashlib.md5(word.upper().encode()).hexdigest()
    if uppercase_result == md_hash_to_crack:
        print('Found password (uppercase): ' + word)
        print('Searched through ' + str(len(wordlist)) + ' words')
        break  # Exit the loop if the password is found

    # Check variations with the first letter capitalized
    for i in range(len(word)):
        capitalized_word = word[:i] + word[i].upper() + word[i + 1:]
        capitalized_result = hashlib.md5(capitalized_word.encode()).hexdigest()
        if capitalized_result == md_hash_to_crack:
            print('Found password (capitalized): ' + capitalized_word)
            print('Searched through ' + str(len(wordlist)) + ' words')
            break  # Exit the loop if the password is found

    # Check variations with numbers appended (from 0 to 9)
    for num in range(100000):
        word_with_num = word + str(num)
        num_result = hashlib.md5(word_with_num.encode()).hexdigest()
        if num_result == md_hash_to_crack:
            print('Found password (with number): ' + word_with_num)
            print('Searched through ' + str(len(wordlist)) + ' words')
            break  # Exit the loop if the password is found

    # Check variations with special characters appended at different positions
    for char in special_characters:
        for i in range(len(word) + 1):
            word_with_char = word[:i] + char + word[i:]
            char_result = hashlib.md5(word_with_char.encode()).hexdigest()
            if char_result == md_hash_to_crack:
                print('Found password (with special character): ' + word_with_char)
                print('Searched through ' + str(len(wordlist)) + ' words')
                break  # Exit the loop if the password is found



print("done")
