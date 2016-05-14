## **python bigsuds - Reverse Lookup (Pool -> Virtual Server)** ##
*(Also published on [DevCentral](https://devcentral.f5.com/codeshare/python-bigsuds-reverse-lookup-pool-gt-virtual-server))*
### **Problem this snippet solves:** ###

> This python bigsuds script prints the list of pools using a specific pool.

### **How to use this snippet:** ###
    rlookup-pool.py <hostname> <username> <poolname>
> Script will prompt for password.  
> This will only search the Common partition.  This also does not check for
> policies or iRules that may change the value of pool.

#### **Script** ####
[rlookup-pool.py](https://github.com/buzzsurfr/f5-bigsuds-utils/blob/master/rlookup-pool.py)
### Tested on Version: ###
> 11.5
