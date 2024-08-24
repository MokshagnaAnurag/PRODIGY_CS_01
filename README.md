caesar_cipher Function:

The Caesar Cipher is a classical encryption technique where each letter in the plaintext is shifted a fixed number of places down or up the alphabet. To create a Python program that can encrypt and decrypt text using the Caesar Cipher, follow these steps:

### Step-by-Step Implementation

1. **Define the Caesar Cipher Encryption and Decryption Functions:**
   - **Encryption**: Shift each letter by a fixed number of positions in the alphabet.
   - **Decryption**: Reverse the shift to retrieve the original message.

2. **Handle User Input**: Allow users to input their message and the shift value for both encryption and decryption.

### Python Code

Here's a complete implementation of the Caesar Cipher with user interaction:

```python
def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypt or decrypt the text using the Caesar Cipher algorithm.

    Args:
    text (str): The text to be encrypted or decrypted.
    shift (int): The number of positions to shift.
    mode (str): 'encrypt' for encryption or 'decrypt' for decryption.

    Returns:
    str: The encrypted or decrypted text.
    """
    result = []
    shift = shift % 26  # Ensure the shift is within 0-25

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # Compute the shifted character
            shifted = chr((ord(char) - start + shift) % 26 + start)
            result.append(shifted)
        else:
            # Non-alphabetic characters are added unchanged
            result.append(char)

    return ''.join(result)

def main():
    print("Caesar Cipher Encryption/Decryption")

    # User input
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (integer): "))
    action = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

    if action not in ['encrypt', 'decrypt']:
        print("Invalid action. Please choose 'encrypt' or 'decrypt'.")
        return

    # Perform encryption or decryption
    result = caesar_cipher(message, shift, mode=action)
    
    print(f"Result: {result}")

if __name__ == '__main__':
    main()
```

### Explanation

1. **`caesar_cipher` Function**:
   - **`text`**: The message to be processed.
   - **`shift`**: The number of positions to shift.
   - **`mode`**: Indicates whether to encrypt or decrypt the message.
   - The function computes the new shifted position for each letter and handles both uppercase and lowercase letters. Non-alphabetic characters remain unchanged.

2. **`main` Function**:
   - Prompts the user to enter the message, shift value, and the action (encrypt or decrypt).
   - Calls the `caesar_cipher` function with the appropriate parameters.
   - Displays the result.

### How to Run

1. Save the code to a file, e.g., `caesar_cipher.py`.
2. Run the script using Python:

   ```bash
   python caesar_cipher.py
   ```

3. Follow the prompts to input your message, shift value, and choose whether to encrypt or decrypt.

