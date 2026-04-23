word = "here"
encoded_word = "".join(format(ord(x), "b") for x in word) # converts the given string into binary 
print(encoded_word)
word_array = []




def SHR(stri):
    global word_array

    stri = stri >> 32

    print(stri)

def ROTR(stri, rot_r, rot_l):
    global word_array

    print(stri)
    temp = (rot_r - rot_l) % len(stri)
    res = stri[temp : ] + stri[ : temp]
    print("The string after rotation is : " + str(res)) 


print(encoded_word)
print(encoded_word.encode())