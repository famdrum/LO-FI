from arrays import DynamicArray
import soundcloud
import random

class SoundCloud():
	def __init__(self, text):
		self.text = text
	def make_url(self):
		if not self.text == '':
			#------------------------------------------------
			#Getting Urls
			#------------------------------------------------
		
			# create a client object with your app credentials
			self.client = soundcloud.Client(client_id='A8KCUSQBeghLCoPS9YsucLC4V5B7fmMl')
		
			# find all sounds of buskers licensed under 'creative commons share alike'
			tracks = self.client.get('/tracks', q=self.text)
		
			url = DynamicArray()
			if not tracks == []:
				for i in tracks:
					for key,value in i.fields().items():
						if key == 'uri':
							if value[:4] == 'http':
								url.append(value)
			return url
	def make_playlist(self):
		url = self.make_url()
		if len(url) >= 4:
			playlist = DynamicArray()

			for i in range(4):
				var = random.choice(url)
				playlist.append(var)
				url.remove(var)
		return playlist
	def get_widgets(self):
		#------------------------------------------------
		#Getting Widgets
		#------------------------------------------------

		info = DynamicArray()
		playlist = self.make_playlist()

		# get a tracks oembed data
		for i in playlist:
			embed_info = self.client.get('/oembed', url=str(i))
			info.append(embed_info)

		widgets = DynamicArray()

		for i in info:
			for key, value in i.fields().items():
				if key == 'html':
					widgets.append(value)
		
		final = DynamicArray()
		
		for i in widgets:
			var = i[71:]
			var = var[:-11]
			final.append(var)
		return final
