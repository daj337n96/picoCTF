import string

cipher_text = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

# this code unicodes the letter(8bit binary) then splits it into 4bits then into letters
# so we need to reverse it
# unicode the letter(4bit binary) then add them(8bit binary) then into letter
'''def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c)) 
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
		print(enc)
	return enc'''

# ALPHABET.index(c1) returns the index of the letter
# c1 = 0,2,4,6 c2=1,3,5,7
# n1 = 4bit binary of c1 n2 = 4bit binary of c2
def b16_decode(enc):
    plain = ""
    for c1, c2 in zip(enc[0::2], enc[1::2]):
        n1 = "{0:04b}".format(ALPHABET.index(c1))
        n2 = "{0:04b}".format(ALPHABET.index(c2))
        binary = int(n1 + n2, 2) # 8bit base 2
        plain += chr(binary) # alphabet form
    return plain

# reverse the shift function
# k = "key[i % len(key)]" which will cycle through the key
# key 
def unshift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]
    
# i holds the index and c holds the letter of cipher_text
# key will be "a b c d..." so "i % len(key)" is always [0] since len(key)=0
def decrypt(enc, key): 
    dec = ""
    for i, c in enumerate(enc):
        dec += unshift(c, key[i % len(key)])
    #print([i % len(key)])
    return(dec)

for key in ALPHABET: # key = "a b c d..."
    decrypted = decrypt(cipher_text, key)
    decoded = b16_decode(decrypted) # has jibberrish in it 
    #print(decrypted)
    
    # string.printable = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
    # check if text in decoded and in "string.printable"
    # prints that key and the corresponding text
    if all([text in string.printable for text in decoded]):
        print(f"Key: {key}, Plaintext: {decoded}")
        print("picoCTF{" + decoded+"}")
        
