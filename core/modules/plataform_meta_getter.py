import yt_dlp 
import aiohttp, asyncio

class youtube:
	def __init__(self, arguments: dict, mode="direct_mode", guest_mode=True):
		self.ARGUMENTS = arguments

	def GetMeta(self) -> dict:
		loop = asyncio.new_event_loop()
		loop.run_until_complete(self.async_core())

	async def async_core(self):
		tasks = []

		for i in self.ARGUMENTS['url']:
			tasks.append(asyncio.create_task(self._make_request(i)))

		meta = await asyncio.gather(*tasks)


	async def _make_request(self, url):
		print()



youtube(arguments={
			"url": ["https://www.youtube.com/watch?v=9-LD3a28ePE", "https://www.youtube.com/watch?v=CFEBriOa1x0"],
			"media": ["video"],
			"parallel": False,
			"download_path": "download/"
		}).GetMeta()