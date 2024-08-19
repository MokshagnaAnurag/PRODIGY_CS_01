caesar_cipher Function:

Parameters:
text: The message to be encrypted or decrypted.
shift: The number of positions to shift each letter.
mode: Either 'encrypt' or 'decrypt', indicating the operation to be performed.
Logic:
Adjust the shift to be within the 0-25 range.
Reverse the shift if decrypting.
Shift each letter of the text while keeping non-alphabetic characters unchanged.
main Function:

Prompts the user for the mode (encrypt/decrypt), message, and shift value.
Validates the inputs and calls the caesar_cipher function.
Displays the result and asks the user if they want to perform another operation.
Program Execution:

The program starts by greeting the user.
It continuously prompts the user until they decide to exit.
