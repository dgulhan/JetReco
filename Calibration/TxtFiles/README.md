# Jet energy correction files

Each branch corresponds to a payload in [conddb](https://cms-conddb.cern.ch/cmsDbBrowser/).

Search for branch name, go to tags and click on the matching payload name to get more information. In each branch, txt files are what is used to create db files with the config JetCorrectionDBWriter_cfg.py. The db file, the name of which can be found from the python config is also in the same location. In addition there is a db file and a txt file with matching name starting as "JetCorrectorParametersCollection", these files are used to upload the corrections to conddb, with the uploadConditions.py.

## Setting up CMSSW for db to txt (or txt to db) conversion

Add the necessary packages:

```
cmsrel CMSSW_7_5_8_patch3
cd CMSSW_7_5_8_patch3/src
cmsenv
git cms-init
git cms-addpkg CondFormats/JetMETObjects
git cms-addpkg JetMETCorrections/Modules
cd JetMETCorrections/Modules/test
```


There, JetCorrectionDBWriter_cfg.py is a (pp) example of the Python configuration needed. Following lines have to be customized:
```
process.CondDBCommon.connect = 'sqlite_file:Jec11_V10.db
```

Replace it with the SQLite filename you want to output to.

For the next part, the following format is used to specify the text JEC filenames:

```
path era jetmet_jec_level algo_or_record
```

The ```jetmet_jec_level``` for heavy ion corrections is mostly L2Relative and L3Absolute (it is a ```
JetCorrectorParametersCollection::Level_t``` enum in CMSSW, and if you want to see all possible values, it resides in ```
CondFormats/JetMETObjects/interface/JetCorrectorParameters.h```).

```
cms.PSet(
         record = cms.string('AK5Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_Jec11_V10_AK5Calo'), 
         label  = cms.string('AK5Calo') 
      ),
```

- The string ```tag``` is the output DB tag.
- The string ```label``` is the output DB label (which is not necessarily equal ```record```, and can have suffixes such as "_offline", etc.).

The other two strings are related to the input text filenames:

- The string ```record``` is equal the jet algorithm record part of the filenames.
```
process.dbWriterAK5Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('Jec11_V10'), 
   algo   = cms.untracked.string('AK5Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
)
```

- The string ```algo``` must be equal ```record``` from the part above.

The remaining two strings are the other parts of the input text filenames:
- The string ```era``` is the first part of the text filenames.
- The string ```path``` is the where the files are located.

For the example here, the DB writer will read in the following text format JEC files:
```
CMSSW_7_5_4/src/CondFormats/JetMETObjects/data/Jec11V0_L1FastJet_AK5Calo.txt
CMSSW_7_5_4/src/CondFormats/JetMETObjects/data/Jec11V0_L1Offset_AK5Calo.txt
CMSSW_7_5_4/src/CondFormats/JetMETObjects/data/Jec11V0_L2Relative_AK5Calo.txt
CMSSW_7_5_4/src/CondFormats/JetMETObjects/data/Jec11V0_L3Absolute_AK5Calo.txt
CMSSW_7_5_4/src/CondFormats/JetMETObjects/data/Jec11V0_L5Flavor_AK5Calo.txt
CMSSW_7_5_4/src/CondFormats/JetMETObjects/data/Jec11V0_L7Parton_AK5Calo.txt
```

Finally:
```
process.p = cms.Path( 
process.dbWriterAK1PF*
process.dbWriterAK2PF*
process.dbWriterAK3PF*
process.dbWriterAK4PF*
process.dbWriterAK5PF*
process.dbWriterAK6PF
) 
```

Make sure you keep only the DB writers you specified.

After customization, simply run:
```
cmsRun JetCorrectionDBWriter_cfg.py
```

after which you will get many warnings of not found JEC levels (since you likely will only have !L2Relative and !L3Absolute). But keep an eye on whether the L2 and L3 are read properly.

To reverse the process, you can also connect to the newly created DB file (or any GT, if you want to extract the JEC from a given GT), and extract the text files by ```JetCorrectionDBReader_cfg.py```. This is explained by the JetMET group in [WorkBookJetEnergyCorrections#GetTxtFiles](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#GetTxtFiles).


## Uploading to database

You need to have special rights to upload db files. Once you obtain the rights run:

```
./uploadConditions.py JetCorrectorParametersCollection_<nameofdbfile>.db
```

The JetCorrectorParametersCollection_<nameofdbfile>.txt needs to have the format that's described [here](https://twiki.cern.ch/twiki/bin/viewauth/CMS/DropBox)
Check whether or not the payload is correctly uploaded by going to conddb browser.