import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

# takes the alphabet in unicode and display in binary. E.g. "C" = 01100011
# first 4 bits convert to base 2 -> display in Alphabet. E.g. first 4bits of "C" = 0110 = 6
# ALPHABET starts from 0 so 6 = "G"
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c)) 
		enc += ALPHABET[int(binary[:4], 2)] 
		enc += ALPHABET[int(binary[4:], 2)]
	return enc


def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

# b16 -> "ABCDEF" = "ebecedeeefeg"
# we can see how each letter becomes shifted by one & + "e" for b16
flag = "ABCDEF"
key = "ABCDEF"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
print(b16)

# i holds the index and c holds the letter
# c will cycle through the key
# unicode what "c" & "key[i % len(key)]" is holding - the unicode of "a"(97)
# the result is added as t1+t2 and mod len(ALPHABET)
# finally it becomes a letter again
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
	print(f"i={i}, c={c}")
	print(i % len(key))
	print(key[i % len(key)])
	#print(len(key))
print(enc)
