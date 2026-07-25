while True:
    # Read a string from the user
    text = input('Enter a string or "q" for exit: ')

    if text == "q":
        break
    
    # Check if the input contains only one character
    if len(text) == 1:
        print("The input contains only one character.")
        continue
    
    # Check if the string is a palindrome
    if text == text[::-1]:
        # Create a dictionary with the palindrome an its length
        palindrome_info = {text: len(text)}
        # Create a list containing the individual characters
        character_list = list(text)

        print("Dictionary:", palindrome_info)
        print("Character list:", character_list)

    else:
        print("The input is not a palindrome.")
            
print("Program terminated.")
        
