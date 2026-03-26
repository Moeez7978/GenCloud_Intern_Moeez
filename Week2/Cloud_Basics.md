# Cloud Computing Fundamentals (AWS / Azure Basics)

This document provides a simple and basic introduction to cloud computing and the core services offered by major cloud providers like AWS and Microsoft Azure.

---

## 1. What is Cloud Computing?

Cloud computing is the delivery of computing services such as servers, storage, databases, networking, and software over the internet instead of using local machines or physical infrastructure.

### Key Benefits

* No need to manage physical hardware
* Scalable resources
* Pay only for what you use
* High availability and reliability
* Accessible from anywhere

---

## 2. Types of Cloud Services

Cloud providers offer different service models:

### Infrastructure as a Service (IaaS)

Provides virtual machines, storage, and networking.

Examples:

* AWS EC2
* Azure Virtual Machines

### Platform as a Service (PaaS)

Provides a platform for developers to build and deploy applications without managing infrastructure.

Examples:

* AWS Elastic Beanstalk
* Azure App Service

### Software as a Service (SaaS)

Provides ready-to-use software accessible through the internet.

Examples:

* Google Workspace
* Microsoft 365

---

## 3. Deployment Models

### Public Cloud

Cloud resources are owned and operated by a cloud provider and shared among multiple users.

Example:
AWS, Azure, Google Cloud

### Private Cloud

Cloud infrastructure used by a single organization.

### Hybrid Cloud

Combination of public cloud and private infrastructure.

---

## 4. AWS (Amazon Web Services) Basics

AWS is one of the most widely used cloud platforms.

### Important AWS Services

**EC2 (Elastic Compute Cloud)**

* Virtual servers in the cloud
* Used to host applications and websites

**S3 (Simple Storage Service)**

* Object storage service
* Stores files, backups, and static websites

**VPC (Virtual Private Cloud)**

* Isolated network inside AWS
* Allows you to control IP ranges, subnets, and routing

**IAM (Identity and Access Management)**

* Manages users and permissions
* Controls access to AWS resources

**ELB (Elastic Load Balancer)**

* Distributes traffic across multiple servers

---

## 5. Microsoft Azure Basics

Microsoft Azure is another major cloud platform used by enterprises and developers.

### Important Azure Services

**Azure Virtual Machines**

* Cloud-based virtual servers
* Similar to AWS EC2

**Azure Blob Storage**

* Storage for large amounts of data
* Similar to AWS S3

**Azure Virtual Network (VNet)**

* Private network in Azure
* Similar to AWS VPC

**Azure Active Directory (Azure AD)**

* Identity and access management service

**Azure Load Balancer**

* Distributes incoming traffic to multiple servers

---

## 6. Basic Cloud Architecture

A typical cloud architecture includes:

User → Internet → Load Balancer → Virtual Machines → Database → Storage

This setup ensures scalability, security, and high availability.

---
## Summary

| Concept           | Description                              |
| ----------------- | ---------------------------------------- |
| Cloud Computing   | Delivering IT services over the internet |
| AWS               | Cloud platform by Amazon                 |
| Azure             | Cloud platform by Microsoft              |
| EC2 / VM          | Virtual servers                          |
| S3 / Blob Storage | Data storage                             |
| VPC / VNet        | Cloud networking                         |
| IAM / Azure AD    | Access control                           |

