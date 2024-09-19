import yt_dlp

class download:
	def __init__(self, meta):
		self.META = meta
		print(self.META)

	def start(self):
		arguments = {
			'format': 'best',
			'noprogress': False,  # Para ver o progresso
		}

		with yt_dlp.YoutubeDL(arguments) as ydl:
			ydl.download(self.META['url'])






# download({
# 			"url": ["https://www.youtube.com/watch?v=9-LD3a28ePE", "https://www.youtube.com/watch?v=d68ee7fASB8", "https://www.youtube.com/watch?v=2rTSmrc-8bo", "https://www.youtube.com/watch?v=506k3_V4z7o", "https://www.youtube.com/watch?v=IdS4MNAe5mQ", "https://www.youtube.com/watch?v=lir3dzYIhz0"],
# 			"media": ["video"],
# 			"parallel": False,
# 			"download_path": "download/"
# 		}).start()