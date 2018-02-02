#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import MeCab
from datetime import datetime
from joblib import Parallel, delayed
from time import time 
from more_itertools import pairwise


def tokenizer_jp(sentence):
  return MeCab.Tagger("-Owakati -d /home/fujiwalatex/mylex").parse(sentence)

def creaning(sentence):
  sentence = re.sub(r"@([A-Za-z0-9_]+)", "", sentence)
  sentence = re.sub(r'https?:\/\/.*', "", sentence)
  return sentence
def process(line_in, line_out, pattern): 
    #print(f"time={datetime.now().strftime('%Y/%m/%d %H:%M:%S')}")
    line_in = tokenizer_jp(creaning(line_in))
    line_out = tokenizer_jp(creaning(line_out))

    if not re.match(pattern, line_in) and not re.match(pattern, line_out):
        return (line_in, line_out)
        #f_in.write(line_in)
        #f_out.write(line_out)
    return ()
pattern = re.compile(r"^\s*$")

start = time()

with open("tweets.txt","r",encoding="utf-8")as f, open("input.txt","w",encoding="utf-8")as f_in, open("output.txt","w",encoding="utf-8")as f_out:
    result = Parallel(n_jobs=-1, verbose=7)([delayed(process)(line_in, line_out, pattern) for line_in, line_out in zip(f,f)])
    for x in result:
        if len(x) > 0:
            f_in.write(x[0])
            f_out.write(x[1])
print(f"result={time() - start}")
