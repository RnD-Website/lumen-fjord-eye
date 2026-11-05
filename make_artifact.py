import re
s=open('index.html').read()
s=re.sub(r'<!doctype html>\s*','',s,flags=re.I)
for t in ['<html lang="en">','</html>','<head>','</head>','<body>','</body>']:
    s=s.replace(t,'',1)
s=re.sub(r'<meta charset="utf-8">\s*','',s,count=1)
s=re.sub(r'<meta name="viewport"[^>]*>\s*','',s,count=1)
s=re.sub(r'<title>.*?</title>','<title>Lumen Fjord</title>',s,count=1,flags=re.S)
s=s.replace(":root{\n  --bg:#050505;",":root{\n  color-scheme:dark;\n  --bg:#050505;",1)
open('lumen-fjord.html','w').write(s.lstrip())
