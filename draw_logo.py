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

im=Image.new("RGB",(900,620),(250,247,238)); d=ImageDraw.Draw(im)
d.ellipse([110,60,790,470],outline=(43,40,36),width=6); d.ellipse([150,95,750,440],fill=(222,204,164))
cx,cy,s=450,250,2.2
d.ellipse([cx-55*s,cy-28*s,cx+45*s,cy+30*s],fill=(122,94,62))
d.polygon([(cx+30*s,cy-10*s),(cx+95*s,cy-42*s),(cx+88*s,cy+2*s)],fill=(96,72,44))
d.ellipse([cx-78*s,cy-52*s,cx-38*s,cy-14*s],fill=(140,112,74))
d.polygon([(cx-52*s,cy-50*s),(cx-44*s,cy-86*s),(cx-36*s,cy-50*s)],fill=(50,42,32))
d.polygon([(cx-66*s,cy-48*s),(cx-62*s,cy-82*s),(cx-52*s,cy-50*s)],fill=(50,42,32))
r=20*s; d.ellipse([cx-46*s-r,cy-26*s-r*.7,cx-46*s+r,cy-26*s+r*.7],fill=(232,119,32),outline=(170,80,10))
d.text((450,520),"configdrift-realtime-config-monitor",font=fit(d,"configdrift-realtime-config-monitor","MaidenOrange",760,44),fill=(43,40,36),anchor="mm")
im.save("logo.png"); print("logo drawn: booming grouse, filled sac, two neck points")
