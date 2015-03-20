>>> import xml.dom.minidom
>>> dom = xml.dom.minidom.parse('C:\Users\Esmidth\Desktop\Tools\Test1.xml')
>>> root=dom.documentElement
>>> print root.toxml()
<ACGServerData>
	<Anime>AIR
		<Name>AIR</Name>
		<Season>1</Season>
			<Episode>12</Episode>
			<Watched>No</Watched>
			<Subtitle>No</Subtitle>	
			<Year>2005</Year>	
			<Resolution>1080P</Resolution>
			<VideoTrack>H264(High 10)</VideoTrack>
			<AudioTrack>AC3</AudioTrack>
	</Anime>
</ACGServerData>
>>> text='Test11'
>>> item=dom.createElement('CaptionT')
>>> text=dom.createTextNode('Test1')
>>> item.appendChild(text)
<DOM Text node "'Test1'">
>>> root.appendChild(item)
<DOM Element: CaptionT at 0x30d2488>
>>> print root.toxml()
<ACGServerData>
	<Anime>AIR
		<Name>AIR</Name>
		<Season>1</Season>
			<Episode>12</Episode>
			<Watched>No</Watched>
			<Subtitle>No</Subtitle>	
			<Year>2005</Year>	
			<Resolution>1080P</Resolution>
			<VideoTrack>H264(High 10)</VideoTrack>
			<AudioTrack>AC3</AudioTrack>
	</Anime>
	<CaptionT>Test1</CaptionT></ACGServerData>
>>> f=file('d:/test.xml', 'w')
>>> import codecs
>>> writer = codecs.lookup('utf-8')[3](f)
>>> dom.writexml(writer, encoding='utf-8')
>>> writer.close()
>>> item2=dom.createElement('Caption2')
>>> text2=dom.createTextNode('Test2')
>>> item2.appendChild(text2)
<DOM Text node "'Test2'">
>>> root.childNodes
[<DOM Text node "u'\n\t'">, <DOM Element: Anime at 0x31f00c8>, <DOM Text node "u'\n'">, <DOM Element: CaptionT at 0x30d2488>]
>>> root.childNodes[1]
<DOM Element: Anime at 0x31f00c8>
>>> root.childNodes[0]
<DOM Text node "u'\n\t'">
>>> root.childNodes[2]
<DOM Text node "u'\n'">
>>> root.toxml()
u'<ACGServerData>\n\t<Anime>AIR\n\t\t<Name>AIR</Name>\n\t\t<Season>1</Season>\n\t\t\t<Episode>12</Episode>\n\t\t\t<Watched>No</Watched>\n\t\t\t<Subtitle>No</Subtitle>\t\n\t\t\t<Year>2005</Year>\t\n\t\t\t<Resolution>1080P</Resolution>\n\t\t\t<VideoTrack>H264(High 10)</VideoTrack>\n\t\t\t<AudioTrack>AC3</AudioTrack>\n\t</Anime>\n<CaptionT>Test1</CaptionT></ACGServerData>'
>>> print root.toxml()
<ACGServerData>
	<Anime>AIR
		<Name>AIR</Name>
		<Season>1</Season>
			<Episode>12</Episode>
			<Watched>No</Watched>
			<Subtitle>No</Subtitle>	
			<Year>2005</Year>	
			<Resolution>1080P</Resolution>
			<VideoTrack>H264(High 10)</VideoTrack>
			<AudioTrack>AC3</AudioTrack>
	</Anime>
	<CaptionT>Test1</CaptionT></ACGServerData>
>>> root.childNodes[1]
<DOM Element: Anime at 0x31f00c8>
>>> root.childNodes[2]
<DOM Text node "u'\n'">
>>> root.childNodes[1].appendChild
<bound method Element.appendChild of <DOM Element: Anime at 0x31f00c8>>
>>> root.childNodes[1].appendChild(item2)
<DOM Element: Caption2 at 0x31f2348>
>>> print root.toxml()
<ACGServerData>
	<Anime>AIR
		<Name>AIR</Name>
		<Season>1</Season>
			<Episode>12</Episode>
			<Watched>No</Watched>
			<Subtitle>No</Subtitle>	
			<Year>2005</Year>	
			<Resolution>1080P</Resolution>
			<VideoTrack>H264(High 10)</VideoTrack>
			<AudioTrack>AC3</AudioTrack>
		<Caption2>Test2</Caption2></Anime>
	<CaptionT>Test1</CaptionT></ACGServerData>
>>> f=file('d:/test.xml', 'w')
>>> writer = codecs.lookup('utf-8')[3](f)
>>> dom.writexml(writer, encoding='utf-8')
>>> writer.close()
>>> print root.childNodes[2]
<DOM Text node "u'\n'">
>>> print root.childNodes[1].childNodes[2]
<DOM Text node "u'\n\t\t'">
>>> print root.childNodes[1].childNodes[1]
<DOM Element: Name at 0x31f0188>
>>> print root.childNodes[1].childNodes[3]
<DOM Element: Season at 0x31f0288>
>>> print root.childNodes[3]
<DOM Element: CaptionT at 0x30d2488>