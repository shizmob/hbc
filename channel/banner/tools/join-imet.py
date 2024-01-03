import os, sys, struct

if sys.version_info >= (3, 0):
	def _b(s):
		return bytes(ord(x) for x in s)
else:
	bytes = str
	def _b(s):
		return s

try:
    import md5
    def do_md5(x):
        return md5.new(x).digest()
except ImportError:
    import hashlib
    def do_md5(x):
        return hashlib.md5(x).digest()

output, datafile, iconarc, bannerarc, soundbns, namesfile = sys.argv[1:]

data = open(datafile,"rb").read()

names={}

for i in open(namesfile,"rb"):
	a,b = i.split(_b("="))
	while b[-1:] == _b("\n"):
		b = b[:-1]
	b = b.replace(_b("\\n"),_b("\n"))
	names[a.decode("ascii")] = b.decode("utf-8")

def getsize(x):
	return os.stat(x).st_size

def pad(x,l):
	if len(x) > l:
		raise ValueError("%d > %d",len(x),l)
	n = l-len(x)
	return x + _b("\x00")*n

imet = _b("\x00")*0x40
imet += struct.pack(">4sIIIIII",_b("IMET"),0x600,3,getsize(iconarc),getsize(bannerarc),getsize(soundbns),1)

for i in ["jp", "en", "de", "fr", "sp", "it", "nl", "cn", None, "ko"]:
	try:
		imet += pad(names[i].encode("UTF-16BE"),0x54)
	except KeyError:
		imet += _b("\x00")*0x54
imet += _b("\x00")*(0x600 - len(imet))

imet = imet[:-16] + do_md5(imet)

open(output,"wb").write(imet)

f = open(sys.argv[1],"wb")
f.write(imet)
f.write(data)

fsize = f.tell()

if (fsize % 20) != 0:
	f.write(_b("\x00")*(20-(fsize%20)))

f.close()
