import os;
import shutil;

# origical code : https://linuxhint.com/schedule_tasks_with_python/

# set the current path as the folder path where the files are located you want to categorize
os.chdir('/home/vidumini/Downloads')

# get list of files in the current path
files = os.listdir(os.getcwd())

for file in files:
	if(not os.path.isdir(file)):
		if('apk' in file):
			if(not os.path.exists('APKs')):
				os.mkdir('APKs')
			shutil.move(file, 'APKs')

		if('torrent' in file):
			if(not os.path.exists('Torrents')):
				os.mkdir('Torrents')
			shutil.move(file, 'Torrents')

		if('jpeg' in file or 'jpg' in file or 'png' in file):
			if(not os.path.exists('Pictures')):
				os.mkdir('Pictures')
			shutil.move(file, 'Pictures')

		if('docx' in file):
			if(not os.path.exists('Docs')):
				os.mkdir('Docs')
			shutil.move(file, 'Docs')

		if('mp3' in file):
			if(not os.path.exists('MP3s')):
				os.mkdir('MP3s')
			shutil.move(file, 'MP3s')

		if('gif' in file):
			if(not os.path.exists('GIFs')):
				os.mkdir('GIFs')
			shutil.move(file, 'GIFs')

		if('PDF' in file or 'pdf' in file):
			if(not os.path.exists('PDFs')):
				os.mkdir('PDFs')
			shutil.move(file, 'PDFs')

		if('zip' in file):
			if(not os.path.exists('Zips')):
				os.mkdir('Zips')
			shutil.move(file, 'Zips')








	