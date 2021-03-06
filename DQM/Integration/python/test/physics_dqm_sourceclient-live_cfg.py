# $Id: physics_dqm_sourceclient-live_cfg.py,v 1.11 2012/02/13 15:09:30 lilopera Exp $

import FWCore.ParameterSet.Config as cms

process = cms.Process("Physics")

#----------------------------
# Event Source
#-----------------------------

# for live online DQM in P5
process.load("DQM.Integration.test.inputsource_cfi")

# for testing in lxplus
#process.load("DQM.Integration.test.fileinputsource_cfi")

#----------------------------
# DQM Environment
#-----------------------------

process.load("DQMServices.Components.DQMEnvironment_cfi")
process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder = 'Physics'
# for local test
process.dqmSaver.dirName = '.'

# 0=random, 1=physics, 2=calibration, 3=technical
process.hltTriggerTypeFilter = cms.EDFilter("HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32(1)
)

#---- for P5 (online) DB access
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")
# Condition for lxplus
#process.load("DQM.Integration.test.FrontierCondition_GT_Offline_cfi") 

process.load('Configuration/StandardSequences/GeometryIdeal_cff')
process.load('Configuration/StandardSequences/MagneticField_AutoFromDBCurrent_cff')
process.load('DQM/Physics/qcdLowPtDQM_cfi')

#process.dump = cms.EDAnalyzer('EventContentAnalyzer')

process.p = cms.Path(
    process.hltTriggerTypeFilter *
    process.myRecoSeq1  *
    process.myRecoSeq2  *
#    process.dump *
    process.qcdLowPtDQM *
    process.dqmEnv *
    process.dqmSaver
)

process.siPixelDigis.InputLabel = cms.InputTag("rawDataCollector")
#--------------------------------------------------
# Heavy Ion Specific Fed Raw Data Collection Label
#--------------------------------------------------

print "Running with run type = ", process.runType.getRunType()

if (process.runType.getRunType() == process.runType.hi_run):
    process.siPixelDigis.InputLabel = cms.InputTag("rawDataRepacker")
