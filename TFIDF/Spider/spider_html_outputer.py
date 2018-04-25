# coding=utf-8

class HtmlOutputer(object):
	"""docstring for HtmlOutputer"""
	def __init__(self):
		super(HtmlOutputer, self).__init__()
		self.datas = []

	# 添加已经抓取的内容
	def collect_data(self, data):
		if data is None:
			return
		self.datas.append(data)

	# 输出抓取内容，保存在文件中
	def output_html(self):
		num = 0
		for data_item in self.datas:
			file_path = ".\output\output_" + str(num)
			fout = open(file_path + '.txt', 'w', encoding='utf-8')
			# print(data_item)
			data_item['summary'] = data_item['summary'].replace(u'\xa0', u' ')
			fout.write("%s\n%s\n" % (data_item['title'],data_item['summary']))
			num = num + 1
		fout.close()





