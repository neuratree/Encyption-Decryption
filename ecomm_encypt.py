import random
from fractions import gcd

public_key  = []
private_key = []
r = 17
s = 7307

def calculate_d(e,phi):
	d = 1
	while 1:
		num=e*d-1
		if num%phi==0:
			break
		d=d+1
	return d

def calculate_e(phi):
	e = 2
        while e < phi:
                if gcd(e, phi) == 1:
                        break
                else:
                        e+=1
	return e

def compute_power_modulus(m,e,n):
	initial = 1
	for i in range(e):
		initial = (m*initial)%n
	return initial

def encrypt(message):
	global public_key
	global private_key
	n = r*s
	phi = (r-1)*(s-1)
	e = calculate_e(phi)
	d = calculate_d(e,phi)
	public_key  = [n,e]
	private_key = [n,d]
	#print message,n,d
	encrypted_msg = compute_power_modulus(message,e,n) 
	return encrypted_msg

def decrypt(encrypted_msg):
	original_msg = compute_power_modulus(encrypted_msg,private_key[1],private_key[0])
	return original_msg

def main():
	while 1:
		message = int(raw_input("What is the message to be encrypted(-1 to exit)?"))
		if message == -1:
			break
		encrypted_msg = encrypt(message)
		print "Encrypted Message is : ", encrypted_msg
		decrypted_msg = decrypt(encrypted_msg)
		print "Decrypted Message is : ", decrypted_msg
	
if __name__ == '__main__':
	main()
