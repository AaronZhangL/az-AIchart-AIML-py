# -*-coding:utf-8 -*-
'''
需要模块：sys
参数个数：len(sys.argv)
脚本名：    sys.argv[0]
参数1：     sys.argv[1]
参数2：     sys.argv[2]
'''
import sys
#print u"Py Script Name：", sys.argv[0]
print "Py Script Name：", sys.argv[0]
for i in range(1, len(sys.argv)): #这里从1开始
    #print u"Parameter", i, sys.argv[i]
    print "Parameter", i, sys.argv[i]
'''
'''