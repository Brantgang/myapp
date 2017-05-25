from xml.parsers.expat import ParserCreate

class WeatherSaxHander(object):
    def __init__(self):
        self.today={}
        self.weather={}
        self.daycount=1


    def start_element(self,name,attrs):
        self.name = name
        if self.name=='yweather:location':
            self.weather['city']=attrs['city']
            self.weather['country']=attrs['country']
        if 'forecast' in name and self.daycount:
            daykey = 'today' if self.daycount == 1 else 'tomorrow'
            self.weather[daykey] = {'text': attrs['text'], 'low': int(attrs['low']), 'high': int(attrs['high'])}
            self.daycount = 2 if self.daycount == 1 else 0


    def end_element(self,name):
        print(('end_element name is %s' % name))

    def char_data(self,text):
        pass


data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''
weatherhandler=WeatherSaxHander()
parser=ParserCreate()
parser.StartElementHandler=weatherhandler.start_element
parser.EndElementHandler=weatherhandler.end_element
parser.CharacterDataHandler=weatherhandler.char_data
parser.Parse(data)
weather=weatherhandler.weather

assert weather['city'] == 'Beijing', weather['city']
assert weather['country'] == 'China', weather['country']




print(weather)
print('Weather:', str(weather))