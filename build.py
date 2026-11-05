import base64,re,os
s=open('src.html').read()
def uri(n): return "data:image/jpeg;base64,"+base64.b64encode(open(f"assets/{n}.jpg","rb").read()).decode()
used={'f4_0','preload'}
for a,b in re.findall(r"'(f\d(?:_\d)?|b\d|c\d\d)','(full\d)'",s): used|={a,b}
imap="const IMG={"+",".join(f"'{n}':'{uri(n)}'" for n in sorted(used))+"};\n"
s=s.replace('src="assets/preload.jpg"','src="'+uri('preload')+'"').replace('<img src="assets/f4_0.jpg" alt="">','<img src="'+uri('f4_0')+'" alt="">')
s=s.replace('src="assets/${n}.jpg"','src="${IMG[n]}"').replace("lbImg.src='assets/'+ITEMS[c.m][4]+'.jpg';","lbImg.src=IMG[ITEMS[c.m][4]];")
s=s.replace("const ITEMS = [",imap+"const ITEMS = [",1)
assert "assets/" not in s
open('index.html','w').write(s);print(os.path.getsize('index.html')/1e6,'MB')
