# 0x17. Web stack debugging #3


## Introduction presented:

* When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)
* Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… It actually powers 26% of the web, so there is a fair chance that you will end up working with it at some point in your career.
* Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.
* The web stack you are debugging today is a Wordpress website running on a LAMP stack.

## Task's description:

### [0. Strace is your friend](./0-strace_is_your_friend.pp)
* Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

## Author
* **Juan Manuel Ramírez Saa** - [Juan8bits](https://github.com/Juan8bits)
