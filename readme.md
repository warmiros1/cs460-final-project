# CS460 Final Project

## Denial of Service Application

This application is a simple DOS CLI that implements both syn flooding and udp flooding from one's local machine as well as on AWS using Lambda. The project also contains a test site we used in order to test (utilized https://github.com/uiucseclab/460FinalDDoSAttacks to help create the test site). The site was hosted on a Raspberry Pi. We ran the program both locally on our machines and using AWS Lambda - a remote function execution. However, through various testing and tweaking, neither our machines nor Lambda were capable of actually knocking our site offline. We spent our time attempting to make the program more effective rather than implementing different types of DOS attacks.

We are confident that a sufficiently long attack from AWS Lambda would take the test server offline, but that would risk leaving the free tier of AWS usage which we did not want to do. A further step for this project could be to call several lambda functions in parallel to simulate a distributed denial of service (DDOS) attack.

## Program Usage

`Python dos.py --help`
