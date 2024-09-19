import argparse

class arguments:
	def __init__(self):
		parser = argparse.ArgumentParser(
				prog="YTubeDownloader",
				description="Baixador de vídeos moderno feito em python",
				epilog="Para ver os comandos, digite help!    YtubeDOwnloader.py <url> <format>"
			)

		parser.add_argument("url", help="Insira sua url bem aqui para baixar o conteúdo!", nargs="+")
		parser.add_argument("-m", "--media", choices=['video', "audio"], nargs="+", help="Qual tipo de mídia deseja baixar? videos ou musicas?", type=str)
		parser.add_argument("-p", "--parallel", help="Baixar arquivos em paralelo.", action="store_true", default=False)
		parser.add_argument("-dp", "--download-path", help="Defina onde o download deve ficar.", type=str)

		parse = parser.parse_args()
		print(parse)

		self.URL = parse.url
		self.MEDIA = parse.media
		self.PARALLEL_DOWNLOAD = parse.parallel
		self.PATH = parse.download_path
		print(self.URL)
	def getArguments(self) -> dict:
		return {
			"url": self.URL,
			"media": self.MEDIA,
			"parallel": self.PARALLEL_DOWNLOAD,
			"download_path": self.PATH,
		}





# arguments()
# input()