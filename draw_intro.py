"""Individually coded drawing program for this repository and this piece only."""
import math, random
from PIL import Image, ImageDraw, ImageFont
FD="/tmp/fonts17"
def F(n,s): return ImageFont.truetype(f"{FD}/{n}.ttf", s)
def fit(d,t,n,mw,st=60):
    s=st
    while s>10:
        f=F(n,s)
        if d.textlength(t,font=f)<=mw: return f
        s-=2
    return F(n,s)

im=Image.new("RGB",(1600,900),(150,140,130)); d=ImageDraw.Draw(im)
for y in range(560):
    t=y/560; c=tuple(int(a+(b-a)*t) for a,b in zip((120,128,138),(244,178,120)))
    d.line([(0,y),(1600,y)],fill=c)
d.rectangle([0,560,1600,900],fill=(206,182,138)); d.rectangle([0,640,1600,900],fill=(188,160,112))
random.seed(4)
for _ in range(260):
    x,y=random.randrange(1600),random.randrange(640,895); d.ellipse([x,y,x+9,y+4],outline=(150,124,84))
# windmill silhouette, board edge-on (a thin line, nothing readable)
d.line([(1380,580),(1362,470)],fill=(52,48,44),width=4); d.line([(1380,580),(1398,470)],fill=(52,48,44),width=4)
for a in range(0,360,30):
    th=math.radians(a); d.line([(1380,452),(1380+math.cos(th)*44,452+math.sin(th)*44)],fill=(52,48,44),width=3)
def grouse(cx,cy,s,sac=1.0):
    d.ellipse([cx-55*s,cy-28*s,cx+45*s,cy+30*s],fill=(122,94,62))
    d.polygon([(cx+30*s,cy-10*s),(cx+95*s,cy-42*s),(cx+88*s,cy+2*s)],fill=(96,72,44))
    d.ellipse([cx-78*s,cy-52*s,cx-38*s,cy-14*s],fill=(140,112,74))
    d.polygon([(cx-52*s,cy-50*s),(cx-44*s,cy-86*s),(cx-36*s,cy-50*s)],fill=(50,42,32))
    d.polygon([(cx-66*s,cy-48*s),(cx-62*s,cy-82*s),(cx-52*s,cy-50*s)],fill=(50,42,32))
    r=20*s*sac; d.ellipse([cx-46*s-r,cy-26*s-r*.7,cx-46*s+r,cy-26*s+r*.7],fill=(232,119,32))
for gx in range(180,1450,210): grouse(gx,610+(gx%3)*14,0.62,0.8)
grouse(520,770,2.5,1.0)
im.save("intro-banner.png"); print("intro drawn: dawn lek, no lettering")
