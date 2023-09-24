#!/bin/bash

atlas=`jq -r '.atlas' config.json`
outputDir='./output'
tempFSSubj=${outputDir}/tmpFsDir/output
atlasOutputDir=${outputDir}/${atlas}/

# lh
cmd="mris_convert \
        --annot ${atlasOutputDir}/lh.${atlas}.annot \
    ${tempFSSubj}/surf/lh.white \
    ${atlasOutputDir}/lh.${atlas}.annot.gii \
    "
echo $cmd
# log $cmd >> $OUT
eval $cmd

# rh
cmd="mris_convert \
        --annot ${atlasOutputDir}/rh.${atlas}.annot \
    ${tempFSSubj}/surf/rh.white \
    ${atlasOutputDir}/rh.${atlas}.annot.gii \
    "
echo $cmd
# log $cmd >> $OUT
eval $cmd
