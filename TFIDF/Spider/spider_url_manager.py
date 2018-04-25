class UrlManager(object):
	"""docstring for UrlManager"""
	def __init__(self):
		super(UrlManager, self).__init__()
		# 设置新旧URL集合
		self.new_urls = set()
		self.old_urls = set()

	# 添加新的URL
	def add_new_url(self, url):
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)

	# 判断新URL集合中是否有新的URL
	def add_new_urls(self, urls):
		if urls is None or len(urls) == 0:
			return
		for url in urls:
			self.add_new_url(url)

	# 从集合中得到新URL，放入旧URL集合
	def get_new_url(self):
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url

	# 判断新URL集合是否为空
	def has_new_url(self):
		return len(self.new_urls) != 0
