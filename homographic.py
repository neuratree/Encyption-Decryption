import random
import math

eta = 15
eta_high = 2*eta
eta_low = int(math.sqrt(eta))
p_low = pow(2,eta-1)
p_high = pow(2,eta)
r_low = pow(2, eta_low-1)
r_high = pow(2,eta_low)
q_low = pow(2,eta_high-1)
q_high = pow(2,eta_high)

key = []

def decrypt_bit_msg(index,bit_msg):
	return (bit_msg%key[index])%2

def encrypt_bit(bit):
	global key
	p = random.randint(p_low,p_high)
	r = random.randint(r_low,r_high)
	q = random.randint(q_low,q_high)
	encryption_msg = p*q + 2*r + bit
	key.append(p)
	return encryption_msg

def decrypt(message):
	count = 0
	decrypted_msg = ""
	msg_bit_segment = message.split()
	for i in msg_bit_segment:
		decrypted_msg  += str(decrypt_bit_msg(count,int(i)))
		count += 1
	return decrypted_msg

def encrypt(msg_bits):
	global key
	encrypted_msg = ""
	key = []
	for i in msg_bits:
		encrypted_msg += str(encrypt_bit(int(i)))
		encrypted_msg += " "
	return encrypted_msg

def extract_bits(message):
	msg_bits = bin(message)
	return msg_bits[2:]

def binary_to_decimal(message):
	result = 0
	for i in message:
		result = result<<1
		result += int(i)
	return result

def main():
	while 1:
		try:
			message = int(raw_input("What is the message to be encrypted(-1 to exit)?"))
		except ValueError:
			print "Please enter a numeric value\n"
			continue

		if message == -1:
			break
		msg_bits = extract_bits(message)
		encrypted_msg = encrypt(msg_bits)
		print "Encrypted Message is : " + encrypted_msg
		decrypt_msg = decrypt(encrypted_msg)
		print "Decrypted Message is : " + str(binary_to_decimal(decrypt_msg))
		print

if __name__ == "__main__":
	main()
