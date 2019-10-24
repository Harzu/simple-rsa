from rsa import RSA

def main():
    privateInstance = RSA()
    privateInstance.generateKeys()

    n, e = privateInstance.getN(), privateInstance.getE()

    publicInstance = RSA()
    publicInstance.setPublicNEFromHex(n, e)

    encryptedMessage = publicInstance.publicEncrypt("Hello world")
    message = privateInstance.privateDecrypt(encryptedMessage)
    
    print(message)
    pass

if __name__ == "__main__":
    main()
    pass