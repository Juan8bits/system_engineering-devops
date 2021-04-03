ls -lB. SSH

## Resources:books:
Read or watch:
* [What is a (physical) server - text](https://intranet.hbtn.io/rltoken/PXE-o9DWronMp4ETwADOpg)
* [What is a (physical) server - video](https://intranet.hbtn.io/rltoken/IfLc3lxSs4w5xdsFlRDPWw)
* [SSH essentials](https://intranet.hbtn.io/rltoken/qKJi0RXLqaCLkHLCLhiYNA)
* [SSH Config File](https://intranet.hbtn.io/rltoken/DNiFD9w9Gx0mnQk5nXbtjg)
* [Public Key Authentication for SSH](https://intranet.hbtn.io/rltoken/ZBYjVLcJ-ck-CFjndgSDBw)
* [How Secure Shell Works](https://intranet.hbtn.io/rltoken/SW2m2e0KMA2K1dXk_0M0CA)
* [SSH Crash Course](https://intranet.hbtn.io/rltoken/8N-RlUma9lwGfyZp1_C-Wg)

---
## Learning Objectives:bulb:
What you should learn from this project:

* What is a server
* Where servers usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair
* The advantage of using  #!/usr/bin/env bash instead of /bin/bash 

---

### [0 Using a private key](./0-use_a_private_key)
Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.

### [1. Create an SSH key pair](./1-create_ssh_key_pair)
Bash script that creates an RSA key pair.
* Name of the created private key must be holberton.
* Number of bits in the created key to be created 4096.
* Twe created key must be protected by the passphrase betty.

### [2. Client configuration file](./2-ssh_config)
Configuration for a ssh_config file to use the private key ~/.ssh/holberton and refuse to authenticate using a password.

---

## Author
* **Juan Manuel Ramirez Saa** - [Juan8bits](https://github.com/Juan8bits)
