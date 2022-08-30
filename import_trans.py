# coding:utf-8
from lxml import etree
xml1 = etree.parse('MP4-2/res/values/strings.xml')  # 读取test.xml文件
xml2 = etree.parse('MP4-2/res/values/strings.xml')  # 读取test.xml文件
root1 = xml1.getroot()  # 获取根节点
root2 = xml2.getroot()  # 获取根节点
# 获取属性
for node in root1.getchildren():
    print(node.tag)
    print(node.items())

for node in root2.getchildren():
    print(node.tag)
    print(node.items())
