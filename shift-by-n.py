ciphertext = input("Cipher text: ").lower()
    
for i in range(1, 26):
	decodetext = ""
	for c in ciphertext:
		if ord(c) - i < 97:
			decodetext = decodetext + chr(ord(c) - i + 26)
		else:
			decodetext = decodetext + chr(ord(c) - i )
	print("n=" + str(i) + ": " + decodetext)
input("Enter to quit.")