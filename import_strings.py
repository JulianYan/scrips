# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# usage:
#   need install lxml : pip3 install lxml
#   python import_strings.py <res_path_from> <res_path_to>
# e.g.:
#   python import_strings.py MP4_3/Camera C:\Users\julian.yan\Documents\Gerrit\CameraApp\common\src\main\res
import os
from lxml import etree
import sys
import shutil

if __name__ == '__main__':
    argv = sys.argv
    # print('lens=', len(argv))
    # print('sys.argv=', str(argv))
    srcPath = argv[1]
    tarPath = argv[2]
    dirList = []
    for root, dirs, files in os.walk(srcPath):
        for name in dirs:
            dirList.append(name)
    # print(str(dirList))
    failedDir = []
    for dir in dirList:
        srcfile = os.path.join(srcPath, dir, "strings.xml")
        tarfile = os.path.join(tarPath, dir, "strings.xml")
        print('from=' + srcfile + ',to=' + tarfile)
        if not os.path.exists(tarfile):
            os.makedirs(os.path.dirname(tarfile))
            shutil.copy(srcfile, tarfile)
        else:
            parser = etree.XMLParser(remove_blank_text=True)
            xml1 = etree.parse(srcfile)  # 读取test.xml文件
            xml2 = etree.parse(tarfile)  # 读取test.xml文件
            root1 = xml1.getroot()  # 获取根节点
            root2 = xml2.getroot()  # 获取根节点
            root2.text = None
            items = root1.xpath('//string')
            for item in items:
                print(item.tag, item.attrib, item.text)
                formatStr = '//string[@name=\'%s\']' % item.attrib.get('name')
                print(formatStr)
                items = root2.xpath(formatStr)
                if len(items) == 0:
                    subElement = etree.Element('string', item.attrib)
                    subElement.text = item.text
                    # subElement.tail = '\n'
                    root2.append(subElement)
                else:
                    item2 = items[0]
                    item2.text = item.text
            # 节点转为tree对象
            tree = etree.ElementTree(root2)
            etree.indent(tree, space="    ")
            tree.write(tarfile, pretty_print=True, xml_declaration=True, encoding='utf-8')


