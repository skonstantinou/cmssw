import os
import FWCore.ParameterSet.Config as cms
from DQMServices.Core.DQMEDHarvester import DQMEDHarvester

process = cms.Process("CONV")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.load("DQMServices.Core.DQMStore_cfi")
process.load("DQMServices.Components.MEtoEDMConverter_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       'file:pi50_1.root',
       'file:pi50_2.root',
       'file:pi50_3.root',
       'file:pi50_4.root',
       'file:pi50_5.root',
       'file:pi50_6.root',
       'file:pi50_7.root',
       'file:pi50_8.root',
       'file:pi50_9.root',
       'file:pi50_10.root',
       'file:pi50_11.root',
       'file:pi50_12.root',
       'file:pi50_13.root',
       'file:pi50_14.root',
       'file:pi50_15.root',
       'file:pi50_16.root',
       'file:pi50_17.root',
       'file:pi50_18.root',
       'file:pi50_19.root',
       'file:pi50_20.root',
       'file:pi50_21.root',
       'file:pi50_22.root',
       'file:pi50_23.root',
       'file:pi50_24.root',
       'file:pi50_25.root',
       'file:pi50_26.root',
       'file:pi50_27.root',
       'file:pi50_28.root',
       'file:pi50_29.root',
       'file:pi50_30.root',
       'file:pi50_31.root',
       'file:pi50_32.root',
       'file:pi50_33.root',
       'file:pi50_34.root',
       'file:pi50_35.root',
       'file:pi50_36.root',
       'file:pi50_37.root',
       'file:pi50_38.root',
       'file:pi50_39.root',
       'file:pi50_40.root',
       'file:pi50_41.root',
       'file:pi50_42.root',
       'file:pi50_43.root',
       'file:pi50_44.root',
       'file:pi50_45.root',
       'file:pi50_46.root',
       'file:pi50_47.root',
       'file:pi50_48.root',
       'file:pi50_49.root',
       'file:pi50_50.root'
      )
)

process.load('Configuration/StandardSequences/EDMtoMEAtRunEnd_cff')
process.dqmSaver.referenceHandling = cms.untracked.string('all')

cmssw_version = os.environ.get('CMSSW_VERSION','CMSSW_X_Y_Z')
Workflow = '/HcalValidation/'+'Harvesting/'+str(cmssw_version)
process.dqmSaver.workflow = Workflow

process.hcaldigisClient = DQMEDHarvester("HcalDigisClient",
     outputFile	= cms.untracked.string('HcalDigisHarvestingME.root'),
     DQMDirName	= cms.string("/") # root directory
)

process.calotowersClient = DQMEDHarvester("CaloTowersClient", 
     outputFile = cms.untracked.string('CaloTowersHarvestingME.root'),
     DQMDirName = cms.string("/") # root directory
)
process.hcalrechitsClient = DQMEDHarvester("HcalRecHitsClient", 
     outputFile = cms.untracked.string('HcalRecHitsHarvestingME.root'),
     DQMDirName = cms.string("/") # root directory
)

process.p = cms.Path(
process.EDMtoME * 
process.calotowersClient * 
process.hcalrechitsClient *
process.hcaldigisClient *
process.dqmSaver)
