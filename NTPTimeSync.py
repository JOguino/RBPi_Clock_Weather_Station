import ntplib
import time
from time import ctime

class NTPTimeSync:
	def __init__(self):
		self.ntpServer = ntplib.NTPClient()
		self.nt = self.ntpServer.request('pool.ntp.org')

	def getTime(self):
		self.nt = self.ntpServer.request('pool.ntp.org')
		return self.nt.tx_time

if __name__ == '__main__':
	ntpService = NTPTimeSync()
	while True:
		print(ctime(ntpService.getTime()))
		time.sleep(1)