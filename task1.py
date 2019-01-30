import os
rootdir = '/home'
for dirname, sublist, filelist in os.walk (rootdir):
	print('found directory: %s' % dirname)
	for fname in filelist:
		print('\t%s' % fname)
	

