
def Cryptography(message):

    from cryptography.fernet import Fernet

    key = Fernet.generate_key()
    F= Fernet(key)
    token= F.encrypt(message.encode())
    text =F.decrypt(token)

    print(token)
    print(text)



