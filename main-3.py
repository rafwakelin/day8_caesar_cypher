from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(user_input, key, dir):
  message = ""
  if dir == "decode":
    key *= -1
  for char in user_input:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + key
      message += alphabet[new_position]
    else:
      message += char
  print(f"Your {dir}d message: {message}")

print(logo)

while True:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26
  
  caesar(user_input=text, key=shift, dir=direction)
  again = input("\nWould you like to run the program again? Yes or No? ").lower()

  if again != 'yes' and again != 'no':
    again = input("\nI don't recognize this entry. Please type 'yes' or 'no'. ")
  if again == 'no':
    print("\n\nThank you for using Caesar Cypher. Hope you enjoyed your experience!")
    break
