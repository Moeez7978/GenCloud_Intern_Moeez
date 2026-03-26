# Infrastructure Basics, Virtualization, and Containers

# 1. What is IT Infrastructure?

IT Infrastructure refers to all the hardware, software, networking, and services required to run applications and systems.

### Main Components of Infrastructure

* Servers
* Storage systems
* Networking
* Operating systems
* Databases
* Applications
* Security systems

### Traditional Infrastructure (On-Premise)

In traditional infrastructure, companies manage their own physical servers inside data centers.

Example:

User → Internet → Physical Server → Database → Storage

### Challenges

* High cost
* Hardware maintenance
* Limited scalability
* Requires physical space

---

# 2. Modern Infrastructure (Cloud-Based)

Modern infrastructure is usually hosted in the cloud using providers like AWS, Azure, or Google Cloud.

### Advantages

* Easy to scale
* Cost efficient
* High availability
* Managed services
* Faster deployment

---

# 3. Virtualization

Virtualization is a technology that allows multiple virtual machines to run on a single physical server.

Instead of one server running one operating system, virtualization allows one server to run multiple systems.

### How Virtualization Works

Physical Server → Hypervisor → Virtual Machines

Each virtual machine has:

* Its own operating system
* CPU
* RAM
* Storage

### Hypervisor

A hypervisor is software that manages virtual machines.

Examples:

* VMware
* VirtualBox
* Hyper-V
* KVM

### Benefits of Virtualization

* Better resource utilization
* Reduced hardware cost
* Easy server management
* Isolation between systems
* Faster deployment

---

# 4. Virtual Machines (VMs)

A Virtual Machine is a virtual computer running on a physical server.

### VM Components

* Guest Operating System
* Virtual CPU
* Virtual RAM
* Virtual Disk

### Example

In cloud environments:

* AWS EC2 Instances
* Azure Virtual Machines

---

# 5. Containers (Introduction)

Containers are a lightweight way to run applications with their dependencies.

Unlike virtual machines, containers share the host operating system.

### Container Architecture

Application → Container Engine → Host OS → Physical Server

### Popular Container Tools

* Docker
* Kubernetes
* Podman

---

# 6. Virtual Machines vs Containers

| Feature        | Virtual Machines       | Containers    |
| -------------- | ---------------------- | ------------- |
| OS             | Each VM has its own OS | Share host OS |
| Size           | Large                  | Lightweight   |
| Startup Time   | Slow                   | Very fast     |
| Resource Usage | High                   | Low           |
| Isolation      | Strong                 | Moderate      |

---

# 7. Why Containers are Important in DevOps

Containers are widely used because they:

* Make applications portable
* Simplify deployment
* Improve scalability
* Work well with CI/CD pipelines
* Enable microservices architecture

Example Workflow:

Developer → Build Docker Image → Deploy Container → Run Application

---

# 8. Example: Running a Container

Example Docker command:

```bash
docker run -d -p 80:80 nginx
```

This command:

* Downloads the Nginx image
* Starts a container
* Exposes port 80

---
