#!/usr/bin/env python3
########################################################################
##           Inbound, an agnostic software building system.           ##
##                                                                    ##
##             Written by  Alexander Nicholi <//nich.fi/>             ##
##   Copyright (C) 2024-2025 Aquefir Consulting LLC <//aquefir.co/>   ##
##                    Released under BSD-2-Clause.                    ##
########################################################################

import re

k_match  = re.compile(r'^BITBOUND.*?$', re.MULTILINE)
k_mkpath = 'src/prologue.mk'
k_cpath  = 'src/bitbound.c'

def main(args: list[str]) -> int:
	f = open(k_cpath, 'rb')
	csrc = f.read().decode('utf-8')
	f.close()
	from cminify import convert
	csrc = convert(csrc)
	f = open(k_mkpath, 'rb')
	text = f.read().decode('utf-8')
	f.close()
	# normalise newlines
	text = text.replace('\r\n', '\n')
	text = text.replace('\r', '\n')
	line = 'BITBOUND := $(shell $(ECHO) -e \'\\\\n'
	line += csrc.replace('\\', '\\\\\\\\')[:-1].replace('\n', '\\\\n')
	line += '\' > bitbound.c ; cc -obitbound.tmp bitbound.c'
	line += ' && ./bitbound.tmp && $(RM) bitbound.c && $(RM)'
	line += ' bitbound.tmp)'
	text = k_match.sub(line, text)
	f = open(k_mkpath, 'wb')
	f.write(text.encode('utf-8'))
	f.flush()
	f.close()
	return 0

if __name__ == '__main__':
	from sys import argv, exit
	exit(main(argv))
