from xml.parsers.expat import ParserCreate

class DefaultSaxHander(object):
    def start_element(self,name,attrs):
        print('start_element is: %s,attrs is : %s'%(name,str(attrs)))

    def end_element(self,name):
        print('end_element is :%s'% name)

    def char_data(self,text):
        print('sax : char_data is :%s'% text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
hander = DefaultSaxHander()
parser = ParserCreate()
parser.StartElementHandler=hander.start_element
parser.EndElementHandler = hander.end_element
parser.CharacterDataHandler=hander.char_data
parser.Parse(xml)
