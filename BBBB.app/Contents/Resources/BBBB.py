'''
Biligrab 0.2
Beining@ACICFG
cnbeining[at]gmail.com
MIT licence
'''

import sys
import os
from io import StringIO
import gzip
import urllib.request
import sys
from imp import reload

reload(sys)

def main(vid, p):
    cid = 0
    title = ''
    partname = ''
    biliurl = 'http://api.bilibili.tv/view?type=xml&appkey=876fe0ebd0e67a0f&id=' + str(vid) + '&page=' + str(p)
    videourl = 'http://www.bilibili.tv/video/av'+vid+'/index_'+p+'.html'
    print('Fetching webpage...')
    request = urllib.request.Request(biliurl)
    response = urllib.request.urlopen(request)
    data = response.read()
    data_list = data.split('\n')
    for lines in data_list:
        if 'cid' in lines:
            cid = lines[7:-6]
            print('cid is ' + str(cid))
        if 'partname' in lines:
            partname = lines[12:-11]
            print('partname is ' + str(partname))
        if 'title' in lines:
            title = lines[9:-8]
            print('title is ' + str(title))
    if cid is 0:
        print('Cannot find cid, trying to do it brutely...')
        print('Fetching webpage...')
        request = urllib.request.Request(videourl)
        request.add_header('Accept-encoding', 'gzip')
        response = urllib.request.urlopen(request)
        if response.info().get('Content-Encoding') == 'gzip':
            buf = StringIO( response.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
        data_list = data.split('\n')
        #Todo: read title
        for lines in data_list:
            if 'cid=' in lines:
                cid = lines.split('&')
                cid = cid[0].split('=')
                cid = cid[-1]
                print('cid is ' + str(cid))
                break
    if cid is 0:
        print('Cannot get cid anyway, you fix it, I am off to get some coffee...')
        exit()
    #start to make folders...
    if title is not '':
        folder = title
    else:
        folder = cid
    if partname is not '':
        filename = partname
    elif title is not '':
        filename = title
    else:
        filename = cid
    folder_to_make = os.getcwd() + '/' + folder
    if not os.path.exists(folder_to_make):
        os.makedirs(folder_to_make)
    os.chdir(folder_to_make)
    print('Fetching XML...')
    os.system('curl -o "'+filename+'.xml" --compressed  http://comment.bilibili.tv/'+cid+'.xml')
    #os.system('gzip -d '+cid+'.xml.gz')
    print('The XML file, ' + filename + '.xml should be ready...enjoy!')
    print('Finding video location...')
    #try api
    request = urllib.request.Request('http://interface.bilibili.tv/playurl?cid='+cid, headers={ 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36', 'Cache-Control': 'no-cache', 'Pragma': 'no-cache' })

    response = urllib.request.urlopen(request)
    data = response.read()
    data_list = data.split('\r')
    #print(data_list)
    rawurl = []
    vid_num = 0
    for lines in data_list:
        lines = str(lines)
        if '<url>' in lines:
            if 'youku' in lines:
                url = lines[17:-9]
            elif 'sina' in lines:
                url = lines[16:-9]
            rawurl.append(url)
        if 'backup_url' in lines:
            break
    if rawurl is []:  #hope this never happen
        request = urllib.request.Request('http://www.flvcd.com/parse.php?kw='+videourl)
        request.add_header('Accept-encoding', 'gzip')
        response = urllib.request.urlopen(request)
        data = response.read()
        data_list = data.split('\n')
        for items in data_list:
            if 'name' in items and 'inf' in items and 'input' in items:
                c = items
                rawurl = c[39:-5]
                rawurl = rawurl.split('|')
                break
    #print(rawurl)
    vid_num = len(rawurl)
    #print(rawurl)
    print(str(vid_num) + ' videos to download, fetch yourself a cup of coffee...')
    for i in range(vid_num):
        print('Downloading ' + str(i+1) + ' of ' + str(vid_num) + ' videos...')
        #print('aria2c -llog.txt -c -s16 -x16 -k1M --out '+str(i)+'.flv "'+rawurl[i]+'"')
        os.system('aria2c -larialog.txt -c -s16 -x16 -k1M --out '+str(i)+'.flv "'+rawurl[i]+'"')
    f = open('ff.txt', 'w')
    ff = ''
    os.getcwd()
    for i in range(vid_num):
        ff = ff + 'file \'' + str(os.getcwd()) + '/'+ str(i) + '.flv\'\n'
    ff = ff.encode("utf8")
    f.write(ff)
    f.close()
    print('Concating videos...')
    os.system('ffmpeg -f concat -i ff.txt -c copy "'+filename+'".mp4')
    os.system('rm -r ff.txt')
    for i in range(vid_num):
        os.system('rm -r '+str(i)+'.flv')
    print('Done, enjoy yourself!')
    exit()

vid = str(input('av'))
p = str(input('P'))
main(vid, p)