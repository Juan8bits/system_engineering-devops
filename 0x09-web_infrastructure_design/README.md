# 0x09. Web infrastructure design

## Resources:books:
Read or watch:
* [What is a database](https://intranet.hbtn.io/rltoken/XLIOfzfuaxPQu39VQ0TLtw)
* [What’s the difference between a web server and an app server?](https://intranet.hbtn.io/rltoken/Nb8B47Y2D8SLqQMOKVoQyQ)
* [DNS record types](https://intranet.hbtn.io/rltoken/oAxMObOTX3Wx4KH_hCNw3g)
* [Single point of failure](https://intranet.hbtn.io/rltoken/wYpewVpIp9PSqqL27RPafg)
* [How to avoid downtime when deploying new code](https://intranet.hbtn.io/rltoken/Mlvynt0OgLQXrxjrC5Wlnw)
* [High availability cluster (active-active/active-passive)](https://intranet.hbtn.io/rltoken/POX3jE0S6TChQHSYQraYeQ)
* [What is HTTPS](https://intranet.hbtn.io/rltoken/N4BwU4wYDNW02kdzMiekFw)
* [What is a firewall](https://intranet.hbtn.io/rltoken/ZFTutaKN4wWzmL4fWhQmeg)

---
## Learning Objectives:bulb:
What you should learn from this project:

* be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
* be able to explain what each component is doing
* be able to explain system redundancy
* Know all the mentioned acronyms: LAMP, SPOF, QPS

---

### [0. Simple Web Stack](./0-simple_web_stack)
* Design a one server web infrastructure that hosts the website that is reachable via www.foobar.com
* Use:
    * 1 server
    * 1 web server (Nginx)
    * 1 application server
    * 1 application files (your code base)
    * 1 database (MySQL)
    * 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

### [1. Distributed Web Infrastructure](./1-distributed_web_infrastructure)
* Design a three server web infrastructure that hosts the website www.foobar.com.
* Use:
    * 2 servers
    * 1 web server (Nginx)
    * 1 application server
    * 1 load-balancer (HAproxy)
    * 1 set of application files (your code base)
    * 1 database (MySQL)

### [2. Secured and Monitored Web Infrastructure](./2-secured_and_monitored_web_infrastructure)
* Design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.
* Use:
    * 3 firewalls
    * 1 SSL certificate to serve www.foobar.com over HTTPS
    * 3 monitoring clients (data collector for Sumologic or other monitoring services)

---

## Author
* **Juan Manuel Ramirez Saa** - [Juan8bits](https://github.com/Juan8bits)
