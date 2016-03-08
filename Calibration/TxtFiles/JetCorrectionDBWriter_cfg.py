import FWCore.ParameterSet.Config as cms 
process = cms.Process('jecdb') 
process.load('CondCore.DBCommon.CondDBCommon_cfi') 
process.CondDBCommon.connect = 'sqlite_file:HI_PythiaCUETP8M1_5020GeV_753p1_v13.db' 
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1)) 
process.source = cms.Source('EmptySource') 
process.PoolDBOutputService = cms.Service('PoolDBOutputService', 
   process.CondDBCommon, 
   toPut = cms.VPSet( 
      cms.PSet(
         record = cms.string('AK4Calo'), 
         tag    = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK4Calo'), 
         label  = cms.string('AK4Calo') 
      )
      # cms.PSet(
         # record = cms.string('AK5PF'), 
         # tag    = cms.string('JetCorrectorParametersCollection_Jec11V0_AK5PF'), 
         # label  = cms.string('AK5PF') 
      # )
   ) 
) 

process.dbWriterAK4Calo = cms.EDAnalyzer('JetCorrectorDBWriter', 
   era    = cms.untracked.string('HI_PythiaCUETP8M1_5020GeV_753p1_v13'), 
   algo   = cms.untracked.string('AK4Calo'),
   path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
) 
# process.dbWriterAK5PF = cms.EDAnalyzer('JetCorrectorDBWriter', 
   # era    = cms.untracked.string('Jec11V0'),  
   # algo   = cms.untracked.string('AK5PF'),
   # path   = cms.untracked.string('CondFormats/JetMETObjects/data/'),
# ) 



process.p = cms.Path( 
# process.dbWriterAK5PF 
process.dbWriterAK4Calo
) 
