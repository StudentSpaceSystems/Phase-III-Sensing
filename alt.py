from MS5607 import MS5607
import time
begin_time = str(int(time.time()))
last_err_print = 0
while True:
	with open('/root/phase3/data/alt_' + begin_time,'a') as write_file:
		while True:
			try:
				i = 0
				sensor = MS5607(0x76)
				while True:
					i = (i + 1) % 40
					((altitude, temp), time_sense) = (sensor.get_altitude(1, write_file),time.time())
					altitude /= 32.8084 # convert to feet
					if not i:
						print('[ {} ] ALT: Alt - {:.2f} ft ; Temp - {:.2f} C'.format(time_sense, altitude, temp))
			except:
				last_err = time.time()
				if (last_err - last_err_print > 2):
					print('[ {} ] ALT: Read error'.format(time.time()))
					last_err_print = time.time()

	print('[ {} ] ALT: Write error'.format(time.time()))
	time.sleep(2)
