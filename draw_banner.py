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

im=Image.new("RGB",(1600,500),(200,190,160)); d=ImageDraw.Draw(im)
for y in range(330):
    t=y/330; c=tuple(int(a+(b-a)*t) for a,b in zip((150,160,168),(250,214,160)))
    d.line([(0,y),(1600,y)],fill=c)
d.rectangle([0,330,1600,500],fill=(208,186,140)); d.rectangle([0,318,1600,334],fill=(110,150,175))
d.line([(1330,350),(1314,240)],fill=(52,48,44),width=4); d.line([(1330,350),(1346,240)],fill=(52,48,44),width=4)
for a in range(0,360,30):
    th=math.radians(a); d.line([(1330,232),(1330+math.cos(th)*38,232+math.sin(th)*38)],fill=(52,48,44),width=3)
d.rectangle([1248,238,1412,282],fill=(250,247,238),outline=(43,40,36),width=3)
t="configdrift-realtime-config-monitor"; d.text((1330,260),t,font=fit(d,t,"MaidenOrange",156,15),fill=(43,40,36),anchor="mm")
def grouse(cx,cy,s):
    d.ellipse([cx-44*s,cy-22*s,cx+36*s,cy+24*s],fill=(122,94,62)); d.ellipse([cx-62*s,cy-42*s,cx-30*s,cy-11*s],fill=(140,112,74))
    r=16*s; d.ellipse([cx-37*s-r,cy-21*s-r*.7,cx-37*s+r,cy-21*s+r*.7],fill=(232,119,32))
for gx in range(120,1150,170): grouse(gx,415+(gx%2)*16,0.8)
d.ellipse([1470,420,1560,452],fill=(170,205,225),outline=(43,40,36))
im.save("banner.png"); print("banner drawn: whole booming ground, board at rider height")
