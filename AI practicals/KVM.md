# Check Virtualization Support

```
egrep -c '(vmx|svm)' /proc/cpuinfo
```

# Install KVM

```
sudo apt update
sudo apt install qemu-kvm libvirt-daemon-system virtinst bridge-utils virt-manager -y
```
or

```
sudo apt-get install qemu-kvm libvirt-bin bridge-utils virt-manager
```

# Packages

| Package      | Purpose               |
| ------------ | --------------------- |
| qemu-kvm     | virtualization engine |
| virt-manager | graphical VM manager  |
| libvirt      | VM management         |
| bridge-utils | networking            |

# Check Installation

```
sudo systemctl status libvirtd
```

# Start Virtual Machine Manager

```
virt-manager
```

# Download ISO File

# Create New Virtual Machine
- Choose Installation Media: Local install media (ISO image)
- Browse ISO File: select downloaded haiku.iso

# Configure RAM & CPU & Create Storage

# Name VM

