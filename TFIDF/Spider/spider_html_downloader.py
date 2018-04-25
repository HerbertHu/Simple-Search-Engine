import urllib

class HtmlDownLoader(object):
	"""docstring for HtmlDownLoader"""
	def __init__(self):
		super(HtmlDownLoader, self).__init__()

	# 开始请求网页，得到网页内容
	def download(self, url):
		if url is None:
			return None

		response = urllib.request.urlopen(url)
		# print(response.getcode())
		# print(response.read())

		if(response.getcode() != 200):
			return None
		return response.read()
