# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from xml.etree import ElementTree as ET
import sys
import shutil

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
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
        parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
        srcroot = ET.parse(srcfile, parser)
        tarroot = ET.parse(tarfile, parser)
        if not os.path.exists(tarfile):
            os.makedirs(os.path.dirname(tarfile))
            shutil.copy(srcfile, tarfile)
        else:
            print(srcfile)
            print(tarfile)
            try:

                for str_element in srcroot.iter("string"):
                    attrib = str_element.attrib

                    text = str_element.text
                    tar_element = tarroot.find(".//string[@name='%s']" % attrib.get('name'))
                    if tar_element is None:
                        tar_element = ET.Element("string", str_element.attrib)
                        tar_element.text = text
                        print("create new element %s=" % tar_element.attrib.get("name"), tar_element.text)
                        tarroot.getroot().append(tar_element)
                    else:
                        oldText = tar_element.text
                        if oldText != text:
                            name = tar_element.attrib.get("name")
                            print(name, oldText, text)
                            # print("change %s from %s to %s" % name, oldText, text)
                            tar_element.text = text
                tarroot.write(tarfile, 'UTF-8', True)
            except ET.ParseError:
                failedDir.append(dir)
    print(failedDir)

