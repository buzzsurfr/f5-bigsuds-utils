## **python bigsuds - Profile Certificate Info** ##
*(Also published on [DevCentral](https://devcentral.f5.com/codeshare/python-bigsuds-profile-certificate-info))*
### **Problem this snippet solves:** ###

> This python bigsuds script prints profile certificate information from multiple
> devices specified as arguments.  The script accepts multiple hostnames or IP
> addresses and can be passed from stdin.

### **How to use this snippet:** ###
    #  Single host
    cert-profile.py <username> <hostname>

    #  Multiple hosts
    cert-profile.py <username> <hostname1> <hostname2>

    #  Pass from File (Linux)
    cat bigip-hosts | xargs cert-profile.py <username>

> Script will prompt for password.  

#### **Script** ####
[cert-profile.py](https://github.com/buzzsurfr/f5-bigsuds-utils/blob/master/cert-profile.py)

### Tested on Version: ###
> 11.5
