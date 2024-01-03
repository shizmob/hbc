import sys, struct

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


data= open(sys.argv[1],"rb").read()

digest = do_md5(data)

hdr = struct.pack(">4sI8x",_b("IMD5"),len(data))

f2 = open(sys.argv[2],"wb")
f2.write(hdr)
f2.write(digest)
f2.write(data)
f2.close()
