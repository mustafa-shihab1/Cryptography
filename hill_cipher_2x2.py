import numpy as np

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

keyOfEncrpt= np.array( [[3 , 25],
                        [24, 17]])

############ (determinant, inverse, adjugate, key_inv) are used for decryption proccess ############
d     = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
d_inv = [1, 9, 21, 15,3, 19, 7, 23, 11, 5, 17, 25]

determinant  = round(np.linalg.det(keyOfEncrpt) % 26)

d_index = d.index(determinant)
d_inverse = d_inv[d_index]

def getAdjugatedMatrix(keyMtrx):
    adguMtrx = keyMtrx.copy()
    adguMtrx[0][0] = keyMtrx[1][1]
    adguMtrx[0][1] = -keyMtrx[0][1]
    adguMtrx[1][0] = -keyMtrx[1][0]
    adguMtrx[1][1] = keyMtrx[0][0]
    return adguMtrx

key_inv = (getAdjugatedMatrix(keyOfEncrpt) * d_inverse) % 26
####################################################################################################

def getDevideedText(text):
    dividedText =[]
    n=2
    text = text.replace(" ", "")
    for i in range(0, len(text), n):
            newText = text[i:(i+n)]
            if i == len(text)-1:
                if i %2 == 0:
                    newText +="K"
            dividedText.append(newText)
    return dividedText
# return => ex: ['MI', 'SS', ...]

def getArrayOfLetters(divText):
    lettersArray =[];
    for elm in divText:
        for let in elm:
            index = alphabet.index(let.lower());
            lettersArray.append(index);
    return lettersArray;
# return => ex: [12, 8] for 'MI'

def multipleMatrices(letArray,key):
    arry =[]
    letAr = np.array(letArray)
    result = np.dot(key,letAr) % 26
    for r in result:
        arry.append(r)
    return arry
# return => mult. of 2 arrays

def getArrayOFText(arry):
    outputTxtArray =[]
    for let in alphabet:
        if arry[0] == alphabet.index(let):
            outputTxtArray.extend(let)
        if arry[1] == alphabet.index(let):
            outputTxtArray.extend(let)
        if arry[0] > arry[1]:
            outputTxtArray.sort(reverse=True)
    return outputTxtArray
# return the output text as an array of letter pairs

def getEncryptedText(cleartext):
    handle_div_txt = getDevideedText(cleartext)
    cipherText = []
    for element in range(0,len(handle_div_txt)):
        currentElement = handle_div_txt[0];    # 'MI'
        handle_div_txt.pop(0);   # remove'MI'
        letArray = getArrayOfLetters(currentElement)
        index=0
        while len(letArray) > 2:
            if index > 1:
                letArray.pop(0)
                index +=1
        resultOfMultiplication = multipleMatrices(letArray,keyOfEncrpt)
        cipherText.extend(getArrayOFText(resultOfMultiplication))
    return cipherText

def getDecryptedText(ciphertext):
    handle_div_txt = getDevideedText(ciphertext)
    clearText = []
    for element in range(0,len(handle_div_txt)):
        currentElement = handle_div_txt[0]   
        handle_div_txt.pop(0)    
        letArray = getArrayOfLetters(currentElement)
        index=0
        while len(letArray) > 2:
            if index > 1:
                letArray.pop(0)
                index +=1
        resultOfMultiplication = multipleMatrices(letArray,key_inv)
        clearText.extend(getArrayOFText(resultOfMultiplication))
    return clearText


if __name__ == "__main__":
    question = input("What proccess you want to do (1 or 2):\n1) Encryption\n2) Decryption\n>> ")

    if question == "1":
        clearText = input("Enter the clear text to encrypt:\n >> ")
        cipherText = getEncryptedText(clearText)
        print("Encrypted Text: ","".join(cipherText).upper())

    elif question == "2":
        cipherText = input("Enter the cipher text to decrypt:\n >> ")
        clearText = getDecryptedText(cipherText);
        print("Decrypted Text: ","".join(clearText).upper())

    else:
        print("plz enter (1) or (2) only !!")