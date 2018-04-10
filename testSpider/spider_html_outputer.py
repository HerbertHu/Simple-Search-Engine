# coding=utf-8

class HtmlOutputer(object):
	"""docstring for HtmlOutputer"""
	def __init__(self):
		super(HtmlOutputer, self).__init__()
		self.datas = []

	def collect_data(self, data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):
		num = 1
		for data_item in self.datas:
			file_path = ".\output\output_" + str(num)
			fout = open(file_path + '.txt', 'w', encoding='utf-8')
			# print(data_item)
			data_item['summary'] = data_item['summary'].replace(u'\xa0', u' ')
			fout.write("%s \n%s\n%s\n" % (data_item['url'],data_item['title'],data_item['summary']))
			num = num + 1
		fout.close()





