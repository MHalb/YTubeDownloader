import yt_dlp

class download:
	def __init__(self, meta):
		self.META = meta

	def start(self):
		options = {"concurrent-fragments": 6, "quiet": True, "no-warnings": True, "progress": True, "paths": {"home": self.META.download_path}, "noplaylist": self.META.playlist}
		

		if self.META.media == 'audio':
			options['format'] = "bestaudio[ext=m4a]"

		else:
			options['format'] = f'bestvideo[height<={self.META.resolution}][ext=mp4]+bestaudio'

		FILES = self.META.url[0]
		URLS =  self.META.url[1]

		if URLS:
			with yt_dlp.YoutubeDL(options) as ydl:
				ydl.download(URLS)

		if FILES:
			for filename in FILES:
				try:
					with open(filename, encoding='utf-8') as r:
						with yt_dlp.YoutubeDL(options) as ydl:
							try:
								ydl.download([url for x in r.readlines() if (url := x.strip())])

							except yt_dlp.utils.DownloadError:
								print("não foi possível baixar, pulando para o próximo.")


				except FileNotFoundError:
					print("não existe.")

		


# download({
# 			"url": ["https://www.youtube.com/watch?v=2rTSmrc-8bo", "https://www.youtube.com/watch?v=506k3_V4z7o", "https://www.youtube.com/watch?v=IdS4MNAe5mQ", "https://www.youtube.com/watch?v=lir3dzYIhz0"],
# 			"media": "audio",
# 			"download_path": "download/"
# 		}).start()