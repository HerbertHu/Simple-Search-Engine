# coding:utf-8
import spider_url_manager, spider_html_downloader, spider_html_parser, spider_html_outputer

class SpiderMain(object):
	def __init__(self):
		# 定义四个模块
		self.urls= spider_url_manager.UrlManager()
		self.downloader = spider_html_downloader.HtmlDownLoader()
		self.parser = spider_html_parser.HtmlParser()
		self.outputer = spider_html_outputer.HtmlOutputer()

	def craw(self, root_url):
		count = 0
		self.urls.add_new_url(root_url)
		# 有新url时进行抓取
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print("craw %d : %s " % (count, new_url))
				html_cont = self.downloader.download(new_url)
				new_urls, new_data = self.parser.parse(new_url, html_cont)
				self.urls.add_new_urls(new_urls)
				# 输出抓取内容
				self.outputer.collect_data(new_data)
				# 设置抓取数量
				if(count == 99):
					break
				count = count + 1

			except Exception as e:
				print("craw failed")
			else:
				pass
			finally:
				pass

		self.outputer.output_html()

if __name__=="__main__":
	# 抓取根目录
	root_url = "http://baike.baidu.com/view/1256.htm"
#root_url = "https://baike.baidu.com/item/%E5%A4%A9%E6%B4%A5%E5%A4%A7%E5%AD%A6"
	obj_spider = SpiderMain()
	# 开始抓取
	obj_spider.craw(root_url)
