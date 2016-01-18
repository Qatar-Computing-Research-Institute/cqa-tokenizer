#!/bin/bash
#Preprocess CQA data
# Francisco Guzman
INPUT=$1

cat $INPUT | perl simplify.perl > $INPUT.clean
cat  $INPUT.clean | python tokenize2.py > $INPUT.tok
perl third-party/truecase-best.perl --model models/cqa-truecaser < $INPUT.tok > $INPUT.tc

