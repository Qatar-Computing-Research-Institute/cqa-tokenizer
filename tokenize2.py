#!/usr/bin
# Tokenize text using twokenize
# Francisco Guzman
import sys
sys.path.append('third-party')
import twokenize as tok



for line in sys.stdin:
	tokenized = tok.tokenize(line.decode("utf-8",'ignore'))
	print u" ".join( tokenized).encode("utf-8",'ignore')


