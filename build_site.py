import json,shutil,os
src='/home/claude/nb5/work/salidas_sismel_dashboard'
d=open(f'{src}/datos/sismel_dashboard_datos.json',encoding='utf-8').read().replace('</','<\\/')
t=open('/home/claude/site/template.html',encoding='utf-8').read()
os.makedirs('/home/claude/site/out/descargas',exist_ok=True)
geo=open('/home/claude/site/geo.json').read()
open('/home/claude/site/out/index.html','w',encoding='utf-8').write(t.replace('/*DATA*/',d).replace('/*GEO*/',geo))
for f in os.listdir(src):
    if f.endswith('.csv'): shutil.copy(f'{src}/{f}','/home/claude/site/out/descargas/'+f)
shutil.copy(f'{src}/datos/sismel_dashboard_datos.json','/home/claude/site/out/sismel_dashboard_datos.json')
print(os.path.getsize('/home/claude/site/out/index.html')/1e6,'MB')
