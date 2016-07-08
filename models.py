#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
学生对应的年级 class：

1-6 小学
7-9 初中
10-12 高中

学生对应的成绩 grade:
1 优秀
2 中等
3 一般

学生对应的省份 province: 
select province_name,count(province_name) from ods_dim_student_adds group by province_name

0	西藏自治区	4664
1	青海省	19139
2	宁夏回族自治区	46409
3	海南省	48779
4	云南省	93186
5	贵州省	135480
6	内蒙古自治区	170956
7	甘肃省	171772
8	新疆维吾尔自治区	183227
9	广西壮族自治区	195615
10	吉林省	225965
11	黑龙江省	250594
12	江西省	307958
13	福建省	318464
14	安徽省	459024
15	重庆市	470365
16	辽宁省	618035
17	湖南省	621691
18	河北省	630018
19	山西省	648253
20	湖北省	741019
21	山东省	818793
22	陕西省	873084
23	河南省	903411
24	天津市	938392
25	四川省	1130698
26	浙江省	1372685
27	江苏省	1875444
28	广东省	2842680
29	上海市	3818421
30	北京市	5656996


可以认为人数越多的省，家长更有为高价进行付费的可能性（综合宣传力度与教育水平）

学生对应的性别 gender:
0 未确定
1 男性
2 女性


'''
class Children(object):

	def __init__(self,name,_class,grade=1,province='unsure'):
		self.name=name
		self._class=_class
		self.grade=grade
		if self.province is 'unsure':
			logging(u'提供省份可以提供更加精确的服务')
		self.province=province

'''
对于家长，用一个标志来衡量以往的消费记录 expense 来提供不同的价格推荐

1 高
2 中
3 低

应该有标志位来记录家长的孩子情况 AB_falg
1 一种测试情况
2 另一种测试情况

'''

class Pach(object):

	def __init__(self,name,expense=1):
		self.name=name
		self.expense=expense
		self.children,self.kind=[],[]
		self.AB_flag=1


	@staticmethod
	def add_children(self,Child):
		self.children.append(child)

	@staticmethod
	def add_kind(self,k):
		self.kind.append(k)



