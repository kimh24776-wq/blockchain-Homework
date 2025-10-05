import hashlib

text = input("Enter text to hash: ")
hash_value = hashlib.sha256(text.encode()).hexdigest()
print("Generated SHA-256 Hash:", hash_value)
