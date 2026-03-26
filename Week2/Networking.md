# Networking Basics (TCP/IP, DNS, HTTP/HTTPS, Load Balancing)

## 1. TCP/IP (Transmission Control Protocol / Internet Protocol)

TCP/IP is the fundamental communication protocol used on the internet. It allows computers and servers to communicate with each other over networks.

### Key Points

* **IP (Internet Protocol)** identifies devices on a network using IP addresses.
* **TCP (Transmission Control Protocol)** ensures reliable data transmission.
* Data is divided into **packets** before being sent over the network.
* TCP guarantees:

  * Data arrives in order
  * No data is lost
  * Errors are corrected

### Example

When you open a website, your computer uses TCP/IP to connect to the server hosting that website.

---

## 2. DNS (Domain Name System)

DNS is like the **phonebook of the internet**. It converts human-readable domain names into IP addresses.

### Example

When you type:

```
google.com
```

DNS converts it into something like:

```
142.250.183.206
```

### How DNS Works

1. User enters a domain name in the browser.
2. Request goes to a DNS resolver.
3. Resolver finds the IP address.
4. Browser connects to the server using that IP.

---

## 3. HTTP and HTTPS

HTTP and HTTPS are protocols used for communication between a web browser and a web server.

### HTTP (Hypertext Transfer Protocol)

* Used to transfer web pages and data.
* Not encrypted.
* Default port: **80**

Example:

```
http://example.com
```

### HTTPS (Hypertext Transfer Protocol Secure)

* Secure version of HTTP.
* Uses **SSL/TLS encryption**.
* Protects user data.
* Default port: **443**

Example:

```
https://example.com
```

### Why HTTPS is Important

* Encrypts data
* Protects passwords and sensitive information
* Improves trust and security

---

## 4. Load Balancing

Load balancing distributes incoming traffic across multiple servers to improve performance and reliability.

### Why Load Balancing is Needed

* Prevents server overload
* Improves system availability
* Handles high traffic
* Provides fault tolerance

### Simple Architecture

User Request → Load Balancer → Multiple Servers

Example:

Server 1
Server 2
Server 3

The load balancer decides which server should handle each request.

### Common Load Balancing Methods

* **Round Robin** – Requests are distributed one by one.
* **Least Connections** – Sends traffic to the server with fewer active connections.
* **IP Hash** – Routes requests based on client IP.

### Example Tools

* Nginx
* AWS Elastic Load Balancer
* HAProxy

---

## Summary

| Concept        | Purpose                                               |
| -------------- | ----------------------------------------------------- |
| TCP/IP         | Enables communication between devices on the internet |
| DNS            | Converts domain names into IP addresses               |
| HTTP/HTTPS     | Transfers data between browser and server             |
| Load Balancing | Distributes traffic across multiple servers           |

---
