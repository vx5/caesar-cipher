# Constants used for both encryption and decryption
min_val = ord('a')
num_letters = 26

# INPUTS:
# - Text to be encrypted (str) [text]
# - Encryption key (int) [key]
# OUTPUT:
# - Encrypted text (str)
def caesar_encrypt(text, key):
	# Warns when key is 0, because no change will be made to text
	if not key: return '0_key_error'
	lower_text = text.lower()
	output = []
	# Iterates through given text
	for char in lower_text:
		# Ignores non-alpha characters
		if not char.isalpha(): continue
		# Shifts letters up alphabet by <key> chars
		adj_num = ord(char) - min_val
		encr_num = (adj_num + key) % num_letters
		encr_char = chr(encr_num + min_val)
		output.append(encr_char)
	return ''.join(output)

# INPUTS:
# - Text to be encrypted (str) [text]
# - Encryption key (int) [key]
# OUTPUT:
# - Decrypted text (str)
def caesar_decrypt(text, key):
	lower_text = text.lower()
	output = []
	for char in lower_text:
		# Non-alpha characters, if found, are not decrypted
		if not char.isalpha(): decr_char = char
		else:
			# Shifts characters down alphabet by <key> chars
			# to reverse encryption
			adj_num = ord(char) - min_val
			decr_num = (adj_num - key) % num_letters
			decr_char = chr(decr_num + min_val)
		output.append(decr_char)
	return ''.join(output)