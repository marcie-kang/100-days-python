Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
stop = False

def caesar(user_choice, original_text, shift_amount):
    encoded_text = ""
        
    for char in original_text:        
        if char not in Alphabet:
            encoded_text += char
            continue
        
        num = Alphabet.index(char)
        final_num = 0

        if user_choice == "encode":
            final_num = num + shift_amount
        elif user_choice == "decode":
            final_num = num - shift_amount
        
        final_num %= len(Alphabet)
        encoded_text += Alphabet[final_num]
        
    print(f"Here is the {user_choice}d result: {encoded_text}")

while not stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    go_on = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()

    if go_on == "no":
        print("Good bye")
        stop = True
