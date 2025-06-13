from module import alphabet
from module import logo

print(logo)

def caesar(original_text, shift_amount, cipher_direction):
    end_text = ""
    shift_amount = shift_amount % len(alphabet)
    for letter in original_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if cipher_direction == 'encode':
                new_index = index + shift_amount
            elif cipher_direction == 'decode':
                new_index = index - shift_amount
            end_text += alphabet[new_index % 26]
        else:
            end_text += letter
    print(f"Your resulting text is: {end_text}")

should_continue = True
while should_continue:
    direction = input("Choose direction: 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    text = input("Enter the text:\n").lower()
    shift = int(input("Enter shift number:\n"))
    
    caesar(original_text=text, shift_amount=shift, cipher_direction=direction)
    
    result = input("Type 'yes' to continue, or 'no' to quit:\n").lower()
    if result == 'no':
        should_continue = False
        print("Goodbye 🍒")


	
	     
	     		     
	