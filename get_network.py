import psutil
import socket
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM

AF_INET6 = getattr(socket, 'AF_INET6', object())
proto_map = {
    (AF_INET, SOCK_STREAM): 'tcp',
    (AF_INET6, SOCK_STREAM): 'tcp6',
    (AF_INET, SOCK_DGRAM): 'udp',
    (AF_INET6, SOCK_DGRAM): 'udp6',
}

templ = "%-15s %-40s %-20s %-40s %-20s %-20s %-10s %-25s %-10s %-10s %-10s"
print(templ % (
        "Protocol Name", "Local Address", "Local Port", "Remote Address", "Remote Port", "Status", "PID",
        "Program name","fd","family","type"))
print '________________________________________________________________________________________________________________________________________________________________________________________________________________________________'

allData = psutil.net_connections('all')
allProsess = psutil.Process()


for data in allData:
    p = psutil.Process(pid=data[6])

    laddr = data[3]
    lport = '-'
    if laddr.__len__() == 0:
        laddr = '-'
    else:
        laddr = "%s,%s" % laddr
        laddr, lport = laddr.split(",")

    raddr = data[4]
    rport = '-'
    if raddr.__len__() == 0:
        raddr = '-'
    else:
        raddr = "%s,%s" % raddr
        raddr, rport = raddr.split(",")


    print(templ % (
        proto_map[(data[1], data[2])],
        laddr,
        lport,
        raddr,
        rport,
        data[5],
        data[6],
        p.name(),
        data[0],
        data[1],
        data[2]
    ))
