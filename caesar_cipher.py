# Constants used for both encryption and decryption
minVal = ord('a')
numLetters = 26

# INPUTS:
# - Text to be encrypted (str) [text]
# - Encryption key (int) [key]
# OUTPUT:
# - Encrypted text (str)
def caesarEncrypt(text, key):
	# Warns when key is 0, because no change will be made to text
	if not key: return '0_key_error'
	lowerText = text.lower()
	output = []
	# Iterates through given text
	for char in lowerText:
		# Ignores non-alpha characters
		if not char.isalpha(): continue
		# Shifts letters up alphabet by <key> chars
		adjNum = ord(char) - minVal
		encrNum = (adjNum + key) % numLetters
		encrChar = chr(encrNum + minVal)
		output.append(encrChar)
	return ''.join(output)

# INPUTS:
# - Text to be encrypted (str) [text]
# - Encryption key (int) [key]
# OUTPUT:
# - Decrypted text (str)
def caesarDecrypt(text, key):
	lowerText = text.lower()
	output = []
	for char in lowerText:
		# Non-alpha characters, if found, are not decrypted
		if not char.isalpha(): decrChar = char
		else:
			# Shifts characters down alphabet by <key> chars
			# to reverse encryption
			adjNum = ord(char) - minVal
			decrNum = (adjNum - key) % numLetters
			decrChar = chr(decrNum + minVal)
		output.append(decrChar)
	return ''.join(output)