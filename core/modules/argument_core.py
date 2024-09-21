import argparse, json

class arguments:
	def __init__(self):
		with open("settings.json", 'r', encoding="utf-8") as r:
			self.SETTINGS = json.load(r)['arguments']

		self.parser = argparse.ArgumentParser(
				prog = self.SETTINGS["ArgumentParser"].get('prog'),
				description = self.SETTINGS["ArgumentParser"].get('description'),
				epilog = self.SETTINGS["ArgumentParser"].get('epilog'),
				usage = self.SETTINGS["ArgumentParser"].get('usage')
			)

	def getArguments(self) -> dict:

		self.parser.add_argument("url", help="Insira sua url bem aqui para baixar o conteúdo!", nargs="+")
		self.parser.add_argument("-m", "--media", choices=["movie", "audio"], help="Qual tipo de mídia deseja baixar? videos ou musicas?", type=str, default='movie')
		self.parser.add_argument("-dp", "--download-path", help="Defina onde o download deve ficar.", type=str, default='download/')
		self.parser.add_argument("-r", "--resolution", default='720', help="Defina a resolução desejada, caso não encontre, baixe a mais próxima.", type=int)
		self.parser.add_argument("-plst", "--playlist", default=True, help="Defina se deve baixar uma playlist inteira em cima de um vídeo único.", action="store_false")

		args = self.parser.parse_args()

		files = []
		urls = []


		for url in args.url:
			if url.endswith(".txt"):
				files.append(url)

			else:
				urls.append(url)

		args.url = (tuple(files), tuple(urls))
		return args

# arguments().getArguments()
# input()