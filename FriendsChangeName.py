import os
def CreateR(): # This will create a list of names of episodes that I use as source.
	with open("path.txt") as f:
		R = ['.DS_Store'] # some times the folder has this file so its name gets changed.
		for x in f:
			R.append(x.split('\n')[0])

#Friends.S01E01 - The One where Monica gets a Roommate - 720p.BluRay.x264PAHE.in.mkv

def rename_files():
	path  = "path/Friends S10 720p BluRay x264 PaHe.in"
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
