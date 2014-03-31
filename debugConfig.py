#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.0.1'
__author__ = 'James Swineson'

class debugString:

    pingResult=[
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
'''

    ]