from tkinter import *
from cryptography.fernet import Fernet

# Generate a new encryption key
key = Fernet.generate_key()

# Initialize a new Fernet instance with the key
fernet = Fernet(key)

# Function to encrypt the input text and save it to a file
def encrypt():
    # Get the input text and encode it
    message = entry.get().encode()
    # Encrypt the message using the Fernet instance
    encrypted = fernet.encrypt(message)
    # Update the output label with the encrypted message
    output.config(text=encrypted)
    # Write the encrypted message to a file
    with open("encrypted_message.txt", 'wb') as file:
        file.write(encrypted)
    # Write the key to a file
    with open("key.txt", 'wb') as file:
        file.write(key)

# Function to decrypt the input text using the key saved in the key.txt file
def decrypt():
    # Get the input text and encode it
    message = entry.get().encode()
    
    # Create a dialog box for key input
    key_dialog = Toplevel(root)
    key_dialog.title("Key Verification")
    
    # Create the key input label and entry widget
    Label(key_dialog, text="Enter Key:").grid(row=0, column=0, padx=10, pady=10)
    key_entry = Entry(key_dialog, width=50, show="*")
    key_entry.grid(row=0, column=1, padx=10, pady=10)
    
    # key verification
    def verify_key():

        key = key_entry.get().encode()
        fernet = Fernet(key)
        
        try:
            # Decrypt the message
            decrypted = fernet.decrypt(message)
            # decoded ecrypted message
            output.config(text=decrypted.decode())
        except:
            output.config(text="Error: Unable to decrypt message")
        
        key_dialog.destroy()
    
    # Create the key verification button
    Button(key_dialog, text="Verify Key", command=verify_key).grid(row=1, column=0, columnspan=2, padx=10, pady=10)


# new  window
root = Tk()
root.title("Encryption/Decryption")
root.geometry("500x300")

Label(root, text="Enter Text to Encrypt/Decrypt:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
entry = Entry(root, width=50, font=("Arial", 12))
entry.grid(row=0, column=1, padx=10, pady=10)

# Create the encrypt and decrypt buttons
Button(root, text="Encrypt", command=encrypt, font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
Button(root, text="Decrypt", command=decrypt, font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=10)

# OUTPUT
Label(root, text="Encrypted/Decrypted Text:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
output = Label(root, text="", font=("Arial", 12), wraplength=400, justify=LEFT)
output.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

root.mainloop()