import os, json
from modules import *


class runner:
	def __init__(self):
		pass

	def build(self) -> None:

		self.ARGUMENTS = argument_core.arguments().getArguments()

		download_engine.download(meta=self.ARGUMENTS).start()



if __name__ == "__main__":
	runner().build()