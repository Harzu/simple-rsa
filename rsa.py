import random
import utils

class RSA:
    # Fixed E
    E = 2 ** 16 + 1
    N = None
    D = None
    
    def generateKeys(self):
        p = utils.generatePrime()
        q = utils.generatePrime()

        self.N = p * q
        
        eilerfunc = (p - 1) * (q - 1)
        
        self.D = utils.findModInverse(self.E, eilerfunc)
        pass

    def setPrivateKeysFromPrimes(self, n, d, e):
        self.E = e
        self.D = d
        self.N = n
        pass

    def setPrivateKeysFromHex(self, hexN, hexD, hexE):
        self.N = int(hexN, 16)
        self.E = int(hexE, 16)
        self.D = int(hexD, 16)
        pass

    def setPublicNEFromPrimes(self, n, e):
        self.E = e
        self.N = n
        pass

    def setPublicNEFromHex(self, hexN, hexE):
        self.N = int(hexN, 16)
        self.E = int(hexE, 16)
        pass
    
    def getN(self):
        return hex(self.N)

    def getD(self):
        return hex(self.D)

    def getE(self):
        return hex(self.E)

    def publicEncrypt(self, message):        
        cipher = []
        for byte in message.encode():
            cipher.append(pow(byte, self.E, self.N))

        return cipher

    def privateDecrypt(self, encryptedMessage):
        result = []
        for block in encryptedMessage:
            result.append(pow(block, self.D, self.N))

        return bytearray(result).decode("utf-8")