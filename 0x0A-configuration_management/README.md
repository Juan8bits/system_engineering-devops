# 0x0A Configuration management

First approach to Puppet making scripts that make certain configurations on the local server

## Resources:books:
Read or watch:
* [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
* [Puppet resource type: file](https://puppet.com/docs/puppet/3.8/types/file.html)
* [Puppet’s Declarative Language: Modeling Instead of Scripting](https://puppet.com/blog/puppets-declarative-language-modeling-instead-of-scripting/)
* [Puppet lint](http://puppet-lint.com/)
* [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)
---

### [0. Create a file](./0-create_a_file.pp)
Using Puppet to create a file in /tmp directory with some, permission, owner, group and content.

### [1. Install a package](./1-install_a_package.pp)
Using Puppet to install puppet-lint version 2.1.1.

### [2. Execute a command](./2-execute_a_command.pp)
Using Puppet to create a manifest that kills a process named killmenow.

---

## Author
* **Juan Manuel Ramirez Saa** - [Juan8bits](https://github.com/Juan8bits)
