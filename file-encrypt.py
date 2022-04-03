from CustomCipherModule import ColeCipher

def openfile(filename) -> list:
    start = True
    content = ''
    try:
        fd = open(filename, 'r')
        while start:
            line = fd.read()
            if not line:
                start = False
            content += line
        fd.close()
        print("Done reading")
    except IOError:
        print("Error opening file")

    return content

def writefile(filename, ciphertext) -> None:
    try:
        fd = open(filename, 'a')
        fd.write("\n Encrypted Text")
        fd.writelines(ciphertext)
        print("done writing")
        fd.close()
    except IOError:
        print("Error opening file")

   



def main():
    try:
        userinput = input("Enter the name or abolute path to file to be encrypted (Leave blank to use sample file in this project):\n")
        keychoice = 10001
        while keychoice < 0 or keychoice > 10000:
            keychoice = int(input("Enter a key value within 1 to 10000: \n"))

        if not userinput:
            userinput = "sample.txt"

        content = openfile(userinput)
        cipherobj = ColeCipher(content, keychoice)
        cipher = cipherobj.encrypt()
        decrypt = cipherobj.decrypt(cipher)

        if cipher:
            print("Cipher text: \n", cipher)
        
        if decrypt:
            print("Decrypted text \n", decrypt)
    
    except ValueError:
        print("Invalid value encountered for key")

    except IOError:
        print("Error opening file")
    


if __name__ == "__main__":
    main()