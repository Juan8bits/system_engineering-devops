# 0x18. Webstack monitoring


## General Objectives:bulb:

* Why is monitoring needed
* What are the 2 main area of monitoring
* What are access logs for a web server (such as Nginx)
* What are error logs for a web server (such as Nginx)

## Task's description:

### 0. Sign up for Datadog and install datadog-agent
* Sign up for a free Datadog account. When signing up, you’ll have the option of selecting statistics from your current stack that Datadog can monitor for you. Once you have an account set up, follow the instructions given on the website to install the Datadog agent.
    * Sign up for Datadog - Please make sure you are using the US website of Datagog (.com)
    * Install datadog-agent on web-01
    * Create an application key
    * Copy-paste in your Intranet user profile (here) your DataDog API key and your DataDog application key.
    * Your server web-01 should be visible in Datadog under the host name XX-web-01
        * You can validate it by using this API
	* If needed, you will need to update the hostname of your server

### 1. Monitor some metrics
* Set up a monitor that checks the number of read requests issued to the device per second.
* Set up a monitor that checks the number of write requests issued to the device per second.

### [2. Setup Datadog](./2-setup_datadog)
* This file contains the answer which has the ```dashboard_id``` on the first line using Datadog's API.

## Author
* **Juan Manuel Ramírez Saa** - [Juan8bits](https://github.com/Juan8bits)
