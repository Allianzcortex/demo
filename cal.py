#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
整体的思路是这样的：

1. 客服确定可能的家长 ID

2. 如何根据家长 ID 来和孩子的　ID 对应起来

3. 根据家长 ID 来进行有关 A/B Test 的测试，提供什么样的折扣

4. 先做一个理论上的实现，之后再做 Web 上的应用

# more if possible,use sqlite 来更优化展示数据

'''
import os
import sys
import string

from random import randint,choice

from models import Children,Pach

# 高中-小学
# 高中-初中
# 初中-小学

def gen_random_name():
	return ''.join(
		choice(string.ascii_uppercase+string.digits)
								for _ in xrange(4))

def gen_family_data():
	# 生成可能的随机二孩数据，可以用 random.randint() 来进行优化
	user_recommend={}
	for i in xrange(300):
		pach=Pach(name='pach'+str(i))
		pach.expense=randint(1,3)
		pach.AB_flag=randint(1,2)
		if i<200:
			pach.append_kind(['senior','primary'])
		elif i<250:
			pach.append_kind(['senior','junior'])
		else:
			pach.append_kind(['junior','primary'])


def gen_first_child_data(pach):
		gen_name=gen_random_name()
		gen_class=randint(10,12) if pach.kind[0]=='senior' else randint(7,9)
		gen_grade=randint(1,3)
		pach.add_children(Children(name=gen_name,_class=gen_class,grade=gen_grade))

def recommend():
	# 这里应该进行 A/B 测试
	# input:学生的省份，过往的成绩，
	for i in xrange(300):
		if pach.






if __name__=='__main__':

