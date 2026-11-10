"""Sobe as thumbs novas (padrao de 10/11/2026) pela API do YouTube.
Uso: YT_CLIENT_ID=.. YT_CLIENT_SECRET=.. YT_REFRESH_TOKEN=.. python3 set_thumbs.py
Cada thumbnails.set custa 50 de cota."""
import os, json, urllib.request, urllib.parse
D = os.path.dirname(os.path.abspath(__file__))
d = urllib.parse.urlencode({k: os.environ[v] for k, v in [('client_id','YT_CLIENT_ID'),('client_secret','YT_CLIENT_SECRET'),('refresh_token','YT_REFRESH_TOKEN')]} | {'grant_type':'refresh_token'}).encode()
T = json.load(urllib.request.urlopen('https://oauth2.googleapis.com/token', d))['access_token']
ch = json.load(urllib.request.urlopen(urllib.request.Request('https://www.googleapis.com/youtube/v3/channels?part=id&mine=true', headers={'Authorization':'Bearer '+T})))
assert ch['items'][0]['id'] == 'UC2AUKzoy2OjPigH_F9-yssw', 'token nao e do canal da Ruth'
for v, vid in json.load(open(os.path.join(D, 'ids.json'))).items():
    f = os.path.join(D, v + '.jpg')
    if not os.path.exists(f): continue
    r = urllib.request.Request('https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId=' + vid, data=open(f,'rb').read(), headers={'Authorization':'Bearer '+T,'Content-Type':'image/jpeg'}, method='POST')
    try: urllib.request.urlopen(r); print(v, vid, 'OK', flush=True)
    except Exception as e: print(v, vid, 'ERRO', getattr(e,'read',lambda:b'')()[:200], flush=True)
