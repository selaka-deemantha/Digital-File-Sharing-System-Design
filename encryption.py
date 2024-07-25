from Crypto.PublicKey import RSA

def generate_keys(key_size):
    """
    Generate RSA key pair.

    Args:
        key_size: Size of the key in bits.

    Returns:
        Public and private key objects.
    """
    key = RSA.generate(key_size)
    return key.publickey(), key

def encrypt(message, public_key):
    """
    Encrypt message using RSA public key.

    Args:
        message: Message to encrypt (string).
        public_key: RSA public key object.

    Returns:
        Encrypted message (bytes).
    """
    message_bytes = message.encode("utf-8")
    encrypted_message = public_key.encrypt(message_bytes, 32)[0]
    return encrypted_message

def main():
    # Generate RSA key pair
    public_key, private_key = generate_keys(2048)

    # Message to encrypt
    message = "This is a secret message."

    # Encrypt the message
    encrypted_message = encrypt(message, public_key)

    # Print the encrypted message
    print(f"Encrypted message: {encrypted_message}")

if __name__ == "__main__":
    main()

