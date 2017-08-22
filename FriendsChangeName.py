import os
def CreateR():
	with open("/Users/manojkumar/Documents/F3.txt") as f:
		R = ['.DS_Store']
		for x in f:
			R.append(x.split('\n')[0])

#Friends.S01E01 - The One where Monica gets a Roommate - 720p.BluRay.x264PAHE.in.mkv

def rename_files():
	path  = "/Volumes/Macintosh HD/Friends/Friends S10 720p BluRay x264 PaHe.in"
	file_list = os.listdir(path)
	#print file_list
	#saved_path = os.getcwd()
	#print "Current is "+saved_path
	os.chdir(path)
	#for filename in file_list:
	for f, g in zip(file_list, R):
		if f.startswith('F'):
		    #filename, extension = os.path.splitext(img)   
			filename0 = f.split('720p')[0]
			filename1 = f.split('720p')[1]
			new_name = '{} - {}.mkv'.format(filename0[:-1],g)
			os.rename(f, new_name)	
