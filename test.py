def xor_encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f_input, open(output_file, 'wb') as f_output:
        while True:
            byte = f_input.read(1)
            if not byte:
                break
            encrypted_byte = bytes([byte[0] ^ key])
            f_output.write(encrypted_byte)

def xor_decrypt_file(input_file, output_file, key):
    xor_encrypt_file(input_file, output_file, key)  # Decryption is the same as encryption with the same key

# Example usage for encoding a file
input_file = "plaintext.txt"
encrypted_file = "encrypted.bin"
decrypted_file = "decrypted.txt"
encryption_key = 42  # Choose an integer key

xor_encrypt_file(input_file, encrypted_file, encryption_key)
# Example usage for decoding the encrypted file
xor_decrypt_file(encrypted_file, decrypted_file, encryption_key)