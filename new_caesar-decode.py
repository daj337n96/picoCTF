import string

cipher_text = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

# this code unicodes the letter(8bit binary) then splits it into 4bits then into letters
# so we need to reverse it unicode the letter(4bit binary) then add them into 8 bit then into letter
'''def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c)) 
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
		print(enc)
	return enc'''

# ALPHABET.index(c1) returns the index of the letter
def b16_decode(enc):
    plain = ""
    for c1, c2 in zip(enc[0::2], enc[1::2]):
        n1 = "{0:04b}".format(ALPHABET.index(c1))
        n2 = "{0:04b}".format(ALPHABET.index(c2))
        binary = int(n1 + n2, 2)
        plain += chr(binary)
    return plain

# reverse the shift function 
def unshift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]

# i holds the index and c holds the letter
# c will cycle through the key
def decrypt(encoded, key):
    dec = ""
    for i, c in enumerate(encoded):
        dec += unshift(c, key[i % len(key)])
    print(dec)

for key in ALPHABET:
    decrypted = decrypt(cipher_text, key)
    decoded = b16_decode(decrypted)
print(decoded)