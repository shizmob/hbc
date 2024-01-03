
CFLAGS = -O3 -Wall
LIBPNGFLAGS = $(shell pkg-config --cflags --libs libpng || printf "%s" "-I/usr/local/include -L/usr/local/lib -lpng")

CC = $(PREFIX)gcc
STRIP = $(PREFIX)strip

all: mkbns$(EXE) png2tpl$(EXE) lz77$(EXE)

mkbns$(EXE): mkbns.c
	$(CC) $(CFLAGS) -o mkbns mkbns.c -lm

png2tpl$(EXE): png2tpl.c
	$(CC) $(CFLAGS) -o png2tpl png2tpl.c $(LIBPNGFLAGS)

lz77$(EXE): lz77.c
	$(CC) $(CFLAGS) -o lz77 lz77.c

clean:
	rm -f mkbns$(EXE) png2tpl$(EXE) lz77$(EXE)
