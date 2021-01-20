## About
This is simple implementation of p2p chat via tcp protocol.
## Users communicating protocol
SOON
## Encrypting and security
Now I'm using AES 128, maybe I'm improve security later.
## Features
- So secure
- Very anonymously
- Much private
- DESIGNED AND CODED IN RUSSIA(🇷🇺)
## TODO
- Mobile app (Android)
- QT interface (Maybe or not)
- Full node (Now working only single_node)
## Preparing for usage
1. Network Address Translation rules (NAT) You need to redirect ports. Atleast you need opened port.
2. Computure with "while" ip (static ip)
3. Create up to 16 digit key (for AES 128 encrypting)
## Run
### If you have atleast 1 opened port
1. server.py
2. client.py 2
3. client.py 1
### Else
1. server.py
2. single_node.py or node.py
3. client.py 3
4. client.py 1
## About node
Node is retranslator witch have alteast 1 opened port. It will help you if you can't open port or if you use mobile internet. About scripts: node.py using all ports, single_node.py using 1 port.
## License, etc
It is distributing under none license. It is very simple code, you can use it as you wish (modify, distribute).
