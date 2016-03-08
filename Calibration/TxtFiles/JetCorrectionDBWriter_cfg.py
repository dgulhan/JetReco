import FWCore.ParameterSet.Config as cms 
process = cms.Process('jecdb') 
process.load('CondCore.DBCommon.CondDBCommon_cfi') 
process.CondDBCommon.connect = 'sqlite_file:HIreco_PythiaCUETP8M1_5020GeV_758p3_v1.db' 
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1)) 
process.source = cms.Source('EmptySource') 
process.PoolDBOutputService = cms.Service('PoolDBOutputService', 
   process.CondDBCommon, 
   toPut = cms.VPSet( 
      cms.PSet(
         record = cms.string('AK1Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AK1Calo'), 
         label  = cms.string('AK1Calo') 
      ),
      cms.PSet(
         record = cms.string('AK2Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AK2Calo'), 
         label  = cms.string('AK2Calo') 
      ),
      cms.PSet(
         record = cms.string('AK3Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AK3Calo'), 
         label  = cms.string('AK3Calo') 
      ),
      cms.PSet(
         record = cms.string('AK4Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AK4Calo'), 
         label  = cms.string('AK4Calo') 
      ),
      cms.PSet(
         record = cms.string('AK5Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AK5Calo'), 
         label  = cms.string('AK5Calo') 
      ),
      cms.PSet(
         record = cms.string('AK6Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AK6Calo'), 
         label  = cms.string('AK6Calo') 
      ),
      cms.PSet(
         record = cms.string('AK1PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AK1PF'), 
         label  = cms.string('AK1PF') 
      ),
      cms.PSet(
         record = cms.string('AK2PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AK2PF'), 
         label  = cms.string('AK2PF') 
      ),
      cms.PSet(
         record = cms.string('AK3PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AK3PF'), 
         label  = cms.string('AK3PF') 
      ),
      cms.PSet(
         record = cms.string('AK4PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AK4PF'), 
         label  = cms.string('AK4PF') 
      ),
      cms.PSet(
         record = cms.string('AK5PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AK5PF'), 
         label  = cms.string('AK5PF') 
      ),
      cms.PSet(
         record = cms.string('AK6PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AK6PF'), 
         label  = cms.string('AK6PF') 
      ),
      cms.PSet(
         record = cms.string('AKPu1Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKPu1Calo'), 
         label  = cms.string('AKPu1Calo') 
      ),
      cms.PSet(
         record = cms.string('AKPu2Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKPu2Calo'), 
         label  = cms.string('AKPu2Calo') 
      ),
      cms.PSet(
         record = cms.string('AKPu3Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKPu3Calo'), 
         label  = cms.string('AKPu3Calo') 
      ),
      cms.PSet(
         record = cms.string('AKPu4Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKPu4Calo'), 
         label  = cms.string('AKPu4Calo') 
      ),
      cms.PSet(
         record = cms.string('AKPu5Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKPu5Calo'), 
         label  = cms.string('AKPu5Calo') 
      ),
      cms.PSet(
         record = cms.string('AKPu6Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKPu6Calo'), 
         label  = cms.string('AKPu6Calo') 
      ),
      cms.PSet(
         record = cms.string('AKPu1PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKPu1PF'), 
         label  = cms.string('AKPu1PF') 
      ),
      cms.PSet(
         record = cms.string('AKPu2PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKPu2PF'), 
         label  = cms.string('AKPu2PF') 
      ),
      cms.PSet(
         record = cms.string('AKPu3PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKPu3PF'), 
         label  = cms.string('AKPu3PF') 
      ),
      cms.PSet(
         record = cms.string('AKPu4PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKPu4PF'), 
         label  = cms.string('AKPu4PF') 
      ),
      cms.PSet(
         record = cms.string('AKPu5PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKPu5PF'), 
         label  = cms.string('AKPu5PF') 
      ),
      cms.PSet(
         record = cms.string('AKPu6PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKPu6PF'), 
         label  = cms.string('AKPu6PF') 
      ),
      cms.PSet(
         record = cms.string('AKVs2Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKVs2Calo'), 
         label  = cms.string('AKVs2Calo') 
      ),
      cms.PSet(
         record = cms.string('AKVs3Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKVs3Calo'), 
         label  = cms.string('AKVs3Calo') 
      ),
      cms.PSet(
         record = cms.string('AKVs4Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKVs4Calo'), 
         label  = cms.string('AKVs4Calo') 
      ),
      cms.PSet(
         record = cms.string('AKVs5Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKVs5Calo'), 
         label  = cms.string('AKVs5Calo') 
      ),
      cms.PSet(
         record = cms.string('AKVs2PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKVs2PF'), 
         label  = cms.string('AKVs2PF') 
      ),
      cms.PSet(
         record = cms.string('AKVs3PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKVs3PF'), 
         label  = cms.string('AKVs3PF') 
      ),
      cms.PSet(
         record = cms.string('AKVs4PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKVs4PF'), 
         label  = cms.string('AKVs4PF') 
      ),
      cms.PSet(
         record = cms.string('AKVs5PF'), 
         tag    = cms.string('JetCorrectorParametersCollection_HIreco_PythiaCUETP8M1_5020GeV_758p3_v1_AKVs5PF'), 
         label  = cms.string('AKVs5PF') 
      )
   ) 
) 

##Jets with no subtraction
process.dbWriterAK1Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK1Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK2Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK2Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK3Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK3Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK4Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK4Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK5Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK5Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK6Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK6Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK1PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK1PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK2PF= cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK2PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK3PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK3PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK4PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK4PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK5PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK5PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK6PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK6PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
##Pu Jets
process.dbWriterAKPu1Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu1Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu2Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu2Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu3Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu3Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu4Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu4Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu5Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu5Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu6Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu6Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu1PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu1PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu2PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu2PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu3PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu3PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu4PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu4PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu5PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu5PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu6PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu6PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
## Vs jets

process.dbWriterAKVs2PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs2PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKVs3PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs3PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKVs4PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs4PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKVs5PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs5PF'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKVs2Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs2Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKVs3Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs3Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKVs4Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs4Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKVs5Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs5Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 

process.p = cms.Path(  
process.dbWriterAK1Calo *
process.dbWriterAK2Calo *
process.dbWriterAK3Calo *
process.dbWriterAK4Calo *
process.dbWriterAK5Calo *
process.dbWriterAK6Calo *
process.dbWriterAK1PF *
process.dbWriterAK2PF *
process.dbWriterAK3PF *
process.dbWriterAK4PF *
process.dbWriterAK5PF *
process.dbWriterAK6PF *
process.dbWriterAKPu1Calo *
process.dbWriterAKPu2Calo *
process.dbWriterAKPu3Calo *
process.dbWriterAKPu4Calo *
process.dbWriterAKPu5Calo *
process.dbWriterAKPu6Calo *
process.dbWriterAKPu1PF *
process.dbWriterAKPu2PF *
process.dbWriterAKPu3PF *
process.dbWriterAKPu4PF *
process.dbWriterAKPu5PF *
process.dbWriterAKPu6PF *
process.dbWriterAKVs2PF *
process.dbWriterAKVs3PF *
process.dbWriterAKVs4PF *
process.dbWriterAKVs5PF *
process.dbWriterAKVs2Calo *
process.dbWriterAKVs3Calo *
process.dbWriterAKVs4Calo *
process.dbWriterAKVs5Calo 
) 
