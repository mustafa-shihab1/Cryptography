alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def lettersToBinary(text):
    text = text.replace(" ", "")
    letter_numbers =[]
    for let in text:
        index = alphabet.index(let.lower())
        letter_numbers.append(index)   
    binary_num = []
    for num in letter_numbers:
        bin_val = bin(num)[2:]
        while(len(bin_val)<5):
            bin_val = "0"+bin_val
        binary_num.append(bin_val)
    return binary_num

def textXorKey():
    bin_text = "".join(lettersToBinary(text))
    bin_key = "".join(lettersToBinary(key))
    bin_cipher=""
    for i in range(len(bin_text)):
        if(bin_text[i] == bin_key[i]):
            bin_cipher += "0"
        else:
            bin_cipher += "1"      
    return bin_cipher

def dividBin():
    bin_num = textXorKey()
    min_index=0
    max_index=5
    xor_array=[]
    while(min_index<max_index and max_index<=len(bin_num)):
        xor_array.append(bin_num[min_index:max_index:])
        min_index +=5
        max_index+=5
    return xor_array

def binaryToLetters():
    bin_array= dividBin()
    numbers=[]
    letters=[]
    for el in bin_array:
        numbers.append(int(el,2))
    for num in numbers:
        if(num>=26):
            num -=26
        letters.append(alphabet[num])
    return letters
    
if __name__ == "__main__":
    print("************ Vernam-Cipher ************")
    text = input("Enter your Text: ")
    key = input("Enter the key:")
    if(len(key) == len(text)):
        bin_text = "".join(lettersToBinary(text))
        bin_key = "".join(lettersToBinary(key))
        print("Result: ","".join(binaryToLetters()))
    else:
        print("The Text-length must equal to the Key-length !!")
