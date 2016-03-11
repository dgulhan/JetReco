import FWCore.ParameterSet.Config as cms 
process = cms.Process('jecdb') 
process.load('CondCore.DBCommon.CondDBCommon_cfi') 
process.CondDBCommon.connect = 'sqlite_file:HI_PythiaCUETP8M1_5020GeV_753p1_v14.db' 
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1)) 
process.source = cms.Source('EmptySource') 
process.PoolDBOutputService = cms.Service('PoolDBOutputService', 
   process.CondDBCommon, 
   toPut = cms.VPSet( 
      cms.PSet(
         record = cms.string('AK1Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AK1Calo_offline'), 
         label  = cms.string('AK1Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AK2Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AK2Calo_offline'), 
         label  = cms.string('AK2Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AK3Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AK3Calo_offline'), 
         label  = cms.string('AK3Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AK4Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AK4Calo_offline'), 
         label  = cms.string('AK4Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AK5Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AK5Calo_offline'), 
         label  = cms.string('AK5Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AK6Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AK6Calo_offline'), 
         label  = cms.string('AK6Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AK1PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AK1PF_offline'), 
         label  = cms.string('AK1PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AK2PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AK2PF_offline'), 
         label  = cms.string('AK2PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AK3PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AK3PF_offline'), 
         label  = cms.string('AK3PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AK4PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AK4PF_offline'), 
         label  = cms.string('AK4PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AK5PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AK5PF_offline'), 
         label  = cms.string('AK5PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AK6PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AK6PF_offline'), 
         label  = cms.string('AK6PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AKPu1Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKPu1Calo_offline'), 
         label  = cms.string('AKPu1Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AKPu2Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKPu2Calo_offline'), 
         label  = cms.string('AKPu2Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AKPu3Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKPu3Calo_offline'), 
         label  = cms.string('AKPu3Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AKPu4Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKPu4Calo_offline'), 
         label  = cms.string('AKPu4Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AKPu5Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKPu5Calo_offline'), 
         label  = cms.string('AKPu5Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AKPu6Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKPu6Calo_offline'), 
         label  = cms.string('AKPu6Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AKPu1PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKPu1PF_offline'), 
         label  = cms.string('AKPu1PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AKPu2PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKPu2PF_offline'), 
         label  = cms.string('AKPu2PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AKPu3PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKPu3PF_offline'), 
         label  = cms.string('AKPu3PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AKPu4PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKPu4PF_offline'), 
         label  = cms.string('AKPu4PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AKPu5PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKPu5PF_offline'), 
         label  = cms.string('AKPu5PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AKPu6PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKPu6PF_offline'), 
         label  = cms.string('AKPu6PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AKVs2Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKVs2Calo_offline'), 
         label  = cms.string('AKVs2Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AKVs3Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKVs3Calo_offline'), 
         label  = cms.string('AKVs3Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AKVs4Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKVs4Calo_offline'), 
         label  = cms.string('AKVs4Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AKVs5Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKVs5Calo_offline'), 
         label  = cms.string('AKVs5Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AKVs6Calo_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKVs6Calo_offline'), 
         label  = cms.string('AKVs6Calo_offline') 
      ),
      cms.PSet(
         record = cms.string('AKVs1PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKVs1PF_offline'), 
         label  = cms.string('AKVs1PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AKVs2PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKVs2PF_offline'), 
         label  = cms.string('AKVs2PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AKVs3PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKVs3PF_offline'), 
         label  = cms.string('AKVs3PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AKVs4PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKVs4PF_offline'), 
         label  = cms.string('AKVs4PF_offline') 
      ),
      cms.PSet(
         record = cms.string('AKVs5PF_offline'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v14_AKVs5PF_offline'), 
         label  = cms.string('AKVs5PF_offline') 
      )
   ), 
) 

##Jets with no subtraction

process.dbWriterAKVs2Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs2Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKVs3Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs3Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
)
process.dbWriterAKVs4Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs4Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKVs5Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs5Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKVs2PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs2PF_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKVs3PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs3PF_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
)
process.dbWriterAKVs4PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs4PF_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKVs5PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('JEC_pp_PYTHIA_TuneCUETP8M1_5020GeV_HIReco'), 
   algo   = cms.untracked.string('AKVs5PF_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 

process.dbWriterAKPu1Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu1Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu2Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu2Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu3Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu3Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
)
process.dbWriterAKPu4Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu4Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu5Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu5Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu6Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu6Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
)
process.dbWriterAKPu1PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu1PF_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu2PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu2PF_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu3PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu3PF_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
)
process.dbWriterAKPu4PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu4PF_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu5PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu5PF_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAKPu6PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AKPu6PF_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
)

process.dbWriterAK1Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK1Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK2Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK2Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK3Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK3Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
)
process.dbWriterAK4Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK4Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK5Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK5Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK6Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK6Calo_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
)
process.dbWriterAK1PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK1PF_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK2PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK2PF_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK3PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK3PF_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
)
process.dbWriterAK4PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK4PF_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK5PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK5PF_offline'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
process.dbWriterAK6PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK6PF_offline'),
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
process.dbWriterAKVs2Calo *
process.dbWriterAKVs3Calo *
process.dbWriterAKVs4Calo *
process.dbWriterAKVs5Calo *
process.dbWriterAKVs2PF *
process.dbWriterAKVs3PF *
process.dbWriterAKVs4PF *
process.dbWriterAKVs5PF *
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
process.dbWriterAKPu6PF 
) 
