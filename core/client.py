import os, json
from modules import *


class runner:
	def __init__(self):

		## Load important file settings
		for files in ["argument", "download", "metadata", "runtime"]:
			try:
				with open(f"settings/{files}_CoreSettings.json", encoding="utf-8") as r:
					match files:
						case "argument":
							self.ARGUMENT_SETTINGS = json.load(r)

						case "download":
							self.DOWNLOAD_SETTINGS = json.load(r)

						case "runtime":
							self.RUNTIME_SETTINGS = json.load(r)

				print(f"{files.upper()} -> File Settings has been loaded!")

			except Exception as exception:

				searchAndRepairKit.profile(exception=exception).solve()
				
				exit()



	def build(self) -> None: ## firtst run checking
		self.ready()

	def ready(self) -> None: ### after build code

		self.ARGUMENTS = argument_core.arguments().getArguments()

		download_engine.download(meta=self.ARGUMENTS).start()



if __name__ == "__main__":
	runner().build()