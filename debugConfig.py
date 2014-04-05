#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.0.1'
__author__ = 'James Swineson'

class debugString:

    pingResult=[
        # Samlpe results for command "ping -c 10 itunes.apple.com"
        # Debian
        '''PING apple.https.tel.ccgslb.com.cn (122.228.85.199) 56(84) bytes of data.
64 bytes from 122.228.85.199: icmp_req=1 ttl=56 time=201 ms
64 bytes from 122.228.85.199: icmp_req=2 ttl=56 time=3233 ms
64 bytes from 122.228.85.199: icmp_req=3 ttl=56 time=2611 ms
64 bytes from 122.228.85.199: icmp_req=4 ttl=56 time=1796 ms
64 bytes from 122.228.85.199: icmp_req=5 ttl=56 time=839 ms
64 bytes from 122.228.85.199: icmp_req=6 ttl=56 time=434 ms
64 bytes from 122.228.85.199: icmp_req=7 ttl=56 time=1738 ms
64 bytes from 122.228.85.199: icmp_req=8 ttl=56 time=760 ms
64 bytes from 122.228.85.199: icmp_req=9 ttl=56 time=533 ms
64 bytes from 122.228.85.199: icmp_req=10 ttl=56 time=3281 ms

--- apple.https.tel.ccgslb.com.cn ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 61000ms
rtt min/avg/max/mdev = 201.836/1543.078/3281.754/1108.149 ms, pipe 4''',

        # Windows 8.1, Chinese
        '''
正在 Ping apple.https.tel.ccgslb.com.cn [122.228.85.199] 具有 32 字节的数据:
来自 122.228.85.199 的回复: 字节=32 时间=37ms TTL=56
来自 122.228.85.199 的回复: 字节=32 时间=37ms TTL=56
来自 122.228.85.199 的回复: 字节=32 时间=22ms TTL=56
来自 122.228.85.199 的回复: 字节=32 时间=77ms TTL=56

122.228.85.199 的 Ping 统计信息:
    数据包: 已发送 = 4，已接收 = 4，丢失 = 0 (0% 丢失)，
往返行程的估计时间(以毫秒为单位):
    最短 = 22ms，最长 = 77ms，平均 = 43ms
''',
        # Mac OS X 10.9.2
        '''PING apple.https.tel.ccgslb.com.cn (115.239.253.43): 56 data bytes
Request timeout for icmp_seq 0
64 bytes from 115.239.253.43: icmp_seq=1 ttl=56 time=41.724 ms
Request timeout for icmp_seq 2
64 bytes from 115.239.253.43: icmp_seq=3 ttl=56 time=176.227 ms
Request timeout for icmp_seq 4
64 bytes from 115.239.253.43: icmp_seq=5 ttl=56 time=138.641 ms
Request timeout for icmp_seq 6
64 bytes from 115.239.253.43: icmp_seq=7 ttl=56 time=27.647 ms
64 bytes from 115.239.253.43: icmp_seq=8 ttl=56 time=36.250 ms

--- apple.https.tel.ccgslb.com.cn ping statistics ---
10 packets transmitted, 5 packets received, 50.0% packet loss
round-trip min/avg/max/stddev = 27.647/84.098/176.227/61.212 ms'''
    ]

    speedtestResult = [
        # Normal result
        '''Ping: 244.141 ms
Download: 0.94 Mbit/s
Upload: 0.82 Mbit/s''',
        # Empty result
        '''


'''       
        ]
