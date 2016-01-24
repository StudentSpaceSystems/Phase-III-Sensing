import time
i = 0
begin_time = str(int(time.time()))
def save_print(file, str):
    print(str)
    file.write(str + '\n')


while True:
    with open('/root/phase3/data/gps_'+begin_time,'a') as write_file:
    	while True:
	    with open('/dev/ttyAMA0','r') as gps_file: 
            	while 'Ben has an arborist':
            	    line = gps_file.readline().strip().split(',')
            	    if len(line) < 2:
	                continue
	    	    if line[0] == '$GPGLL':
		        if not line[1]:
	            	    i = (i + 1) % 5
		    	    if not i:
		                save_print(write_file,'[ {} ] GPS: No Satellite Detected'.format(time.time()))
		    	    continue
		        try:
	            	    lat_mag = float(line[1])
		    	    lon_mag = float(line[3])
		    	    lat_dir = line[2]
		    	    lon_dir = line[4]
		    	    lat_deg = int(lat_mag // 100.0)
		    	    lon_deg = int(lon_mag // 100.0)
		    	    lat_mins = lat_mag % 100.0
		    	    lon_mins = lon_mag % 100.0
		    	    save_print(write_file,"[ {} ] GPS: {} deg, {:.2f} ' {} ; {} deg, {:.2f} ' {}".format(time.time(),lat_deg,lat_mins,lat_dir,lon_deg,lon_mins,lon_dir))
		        except:
		            save_print(write_file,'[ {} ] GPS: Parsing error'.format(time.time()))
    
            save_print(write_file,'[ {} ] GPS: Read Error'.format(time.time()))
            time.sleep(2)
    save_print(write_file,'[ {} ] GPS: Write Error'.format(time.time()))
    time.sleep(2)

   
