import subprocess as sp
import time
begin_time = str(int(time.time()))
while True:
	with open('/root/phase3/data/imu_' + begin_time,'a') as out_file:
		try:
			imu_proc = sp.Popen(['minimu9-ahrs','-b','/dev/i2c-1','--output','euler'], stdout=sp.PIPE)
			i = 0
			with imu_proc.stdout as imu_out:
				while True:
					vals = imu_out.readline().strip().split(' ')
					vals = [v for v in vals if v]
					if len(vals) < 9:
						if not i%200:
							print('[ {} ] IMU: Parse error'.format(time.time()))
						continue
					save_line = ','.join([str(time.time())] + vals) + '\n'
					out_file.write(save_line)
					Ax = float(vals[3])
					Ay = float(vals[4])
					Az = float(vals[5])
					A = (Ax**2 + Ay**2 + Az**2)**0.5
					if not i%100:
						print('[ {} ] IMU: Pitch - {} ; G-force - {:.2f}'
						.format(time.time(),vals[2],A))
					i = (i + 1) % 200
		except:
			print('[ {} ] IMU: Read error'.format(time.time()))
			time.sleep(2)
	print('[ {} ] IMU: Write error'.format(time.time()))
	time.sleep(2)


	
