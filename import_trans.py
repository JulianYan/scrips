# coding:utf-8
from lxml import etree
parser = etree.XMLParser(remove_blank_text=True)
xml1 = etree.parse('MP4-2/Camera/values/strings.xml', parser)  # 读取test.xml文件
xml2 = etree.parse('MP4-2/res/values-test/strings.xml', parser)  # 读取test.xml文件
root1 = xml1.getroot()  # 获取根节点
root2 = xml2.getroot()  # 获取根节点
# 获取属性

items = root1.xpath('//string')
for item in items:
    print(item.tag, item.attrib, item.text)
    formatStr = '//string[@name=\'%s\']' % item.attrib.get('name')
    print(formatStr)
    items = root2.xpath(formatStr)
    if len(items) == 0:
        subElement = etree.Element('string', item.attrib)
        subElement.text = item.text
        root2.append(subElement)
    else:
        item2 = items[0]
        item2.text = item.text

#节点转为tree对象
tree = etree.ElementTree(root2)
tree.write('test.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')

