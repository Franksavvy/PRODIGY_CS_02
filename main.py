from PIL import Image
import numpy as np

def xor_encrypt_decrypt(image_array, key):
    # XOR encryption/decryption
    key_length = len(key)
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            for k in range(image_array.shape[2]):
                image_array[i, j, k] ^= key[i % key_length]
    return image_array

def process_image(image_path, output_path, key, mode):
    # Load image
    image = Image.open(image_path)
    image_array = np.array(image)

    if mode == 'encrypt':
        key_bytes = [ord(k) for k in key]
        encrypted_array = xor_encrypt_decrypt(image_array, key_bytes)
        encrypted_image = Image.fromarray(encrypted_array)
        encrypted_image.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    elif mode == 'decrypt':
        key_bytes = [ord(k) for k in key]
        decrypted_array = xor_encrypt_decrypt(image_array, key_bytes)
        decrypted_image = Image.fromarray(decrypted_array)
        decrypted_image.save(output_path)
        print(f"Image decrypted and saved as {output_path}")

def main():
    mode = input("Enter 'encrypt' to encrypt an image or 'decrypt' to decrypt an image: ").strip().lower()
    image_path = input("Enter the path of the image file: ")
    output_path = input("Enter the output path for the processed image: ")
    key = input("Enter a key (string): ")

    if mode in ['encrypt', 'decrypt']:
        process_image(image_path, output_path, key, mode)
    else:
        print("Invalid mode selected. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
