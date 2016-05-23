## **python bigsuds - Device Certificate Info** ##
*(Also published on [DevCentral](https://devcentral.f5.com/codeshare/python-bigsuds-device-certificate-info))*
### **Problem this snippet solves:** ###

> This python bigsuds script prints device certificate information from multiple
> devices specified as arguments.  The script accepts multiple hostnames or IP
> addresses and can be passed from stdin.

### **How to use this snippet:** ###
    #  Single host
    cert-device.py <username> <hostname>

    #  Multiple hosts
    cert-device.py <username> <hostname1> <hostname2>

    #  Pass from File (Linux)
    cat bigip-hosts | xargs cert-device.py <username>

> Script will prompt for password.  

#### **Script** ####
[cert-device.py](https://github.com/buzzsurfr/f5-bigsuds-utils/blob/master/cert-device.py)

### Tested on Version: ###
> 11.5
