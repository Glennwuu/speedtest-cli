#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Global Config
debug_1 = 0 #speedtest-cli
debug_2 = 0 #ping
verbose = 1
do_not_post = 0


import os, httplib, socket

def log(context):
	'''Print out log text when verbose mode enabled'''
	if verbose == 1:
		print context

def post_data1(sensor_id, data):
	if do_not_post == 1:
		return 200
	d = '{"value": %f}' % data
	h = {"U-ApiKey": API_KEY}
	p = "/v1.0/device/%d/sensor/%d/datapoints" % (device_id, sensor_id)
	conn = httplib.HTTPConnection("api.yeelink.net", timeout=30)
	conn.request("POST", p, d, h)
	response = conn.getresponse()
	return response.status

def post_data(sensor_id, data):
	try:
		r = post_data1(sensor_id, data)
	except (httplib.HTTPException, socket.error) as e:
		log("HTTP Request failed.")
		return 0
	return r
	
# Ping test
log("Starting ping test...")
if debug_2 == 1:
	ping = '''PING apple.https.tel.ccgslb.com.cn (122.228.85.199) 56(84) bytes of data.
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
rtt min/avg/max/mdev = 201.836/1543.078/3281.754/1108.149 ms, pipe 4'''.split('\n')
else:
	ping = os.popen("ping -c 10 itunes.apple.com").read().split("\n")

#log(ping)
loss = float(ping[-3].split(" ")[5].replace("%",""))
(tmin, tavg, tmax, tstddev) = tuple(ping[-2].split(" ")[3].split("/"))
log("Uploading data...")
log("===Packet loss===")
log(post_data(13472, float(loss)))
log("===tmin===")
log(post_data(13473, float(tmin)))
log("===tavg===")
log(post_data(13474, float(tavg)))
log("===tmax===")
log(post_data(13475, float(tmax)))
log("===tstddev===")
log(post_data(13476, float(tstddev)))

#speedtest-cli
log("Testing speed...")

if debug_1 == 1:
	log("===Debug Mode===")
	res = '''Ping: 244.141 ms
Download: 0.94 Mbit/s
Upload: 0.82 Mbit/s
'''
else:
	import os
	res = os.popen("speedtest-cli --simple").read()

log("Speed test finished.")
log(res)
try:
	resu = res.split("\n")
	ping = float(resu[0].split(": ")[1].split(" ")[0])
	down = float(resu[1].split(": ")[1].split(" ")[0]) / 8. * 1024
	up = float(resu[2].split(": ")[1].split(" ")[0]) / 8. * 1024
except e:
	ping = 0
	down = 0
	up = 0

output = '网速测试结果：\n连接时间：%0.3f 毫秒\n下载速度：%0.2f KB/s\n上传速度：%0.2f KB/s' % (ping, down, up)
log(output)
log("Uploading data...")
resp = post_data(13456, ping)
log("===Ping===")
log(resp)
resp = post_data(13458, down)
log("===Download===")
log(resp)
resp = post_data(13459, up)
log("===Upload===")
log(resp)
log("Finished.")


log("All tasks finished.")
