# Constants used for both encryption and decryption
minVal = ord('a')
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def caesarEncrypt(text, key):
	# Warns when key is 0, because no change will be made to text
	if not key: return '0_key_error'
	lowerText = text.lower()
	output = []
	for char in lowerText:
		if char not in alphabet: continue
		adjNum = ord(char) - minVal
		encrNum = (adjNum + key) % len(alphabet)
		encrChar = chr(encrNum + minVal)
		output.append(encrChar)
	return ''.join(output)

def caesarDecrypt(text, key):
	lowerText = text.lower()
	output = []
	for char in lowerText:
		if char not in alphabet: decrChar = char
		else:
			adjNum = ord(char) - minVal
			decrNum = (adjNum - key) % len(alphabet)
			decrChar = chr(decrNum + minVal)
		output.append(decrChar)
	return ''.join(output)