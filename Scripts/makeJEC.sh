#!/bin/sh

dbfile=HI_PythiaCUETP8M1_5020GeV_753p1_v13.db

#version=19
comment="Production data and mc jet corrections for 2015 5.02 TeV pp and PbPb run"
since=1

v=13
for base in "offline"; do
    for algo in "AK4" ; do
    for obj in "Calo"; do

    inputtag=JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v${v}_${algo}${obj}_${base}
    outputtag=$inputtag
    
    cat template.txt | sed "s/__INPUT__/$inputtag/g" | sed "s/__OUTPUT__/$outputtag/g" | sed "s/__SINCE__/$since/g" | sed "s/__COMMENT__/$comment/g" > $outputtag.txt
    cp $dbfile $outputtag.db
    
    echo "./upload.py $outputtag.db"

done

done
done


