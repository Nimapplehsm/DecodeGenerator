# db_elements.py

db_elements = [ "src_","src_ProtocolCode", "src_ProtocolClinicalIndication", "src_ProjectNumber", "src_SubprotocolSite",
            "src_SubProtocolDefaultReportingUnit", "src_SubProtocolProjectAgeFlag", "src_InvestigatorNumber",
            "src_InvestigatorCity", "src_InvestigatorCountry", "src_InvestigatorCountryCode",
            "src_InvestigatorDistrCode", "src_InvestigatorFaxNumber", "src_InvestigatorName",
            "src_InvestigatorPhoneNumber", "src_InvestigatorStateOrProvince", "src_InvestigatorStreet",
            "src_InvestigatorZip", "src_PatientNumber", "src_PatientScreeningNumber", "src_PatientBirthDate",
            "src_PatientGender", "src_PatientComponsiteIdentifier", "src_PatientEthnicOrigin",
            "src_PatientInitials", "src_PatientStatus", "src_VisitAccessionNumber", "src_VisitKittype",
            "src_VisitProtocolVisitCode", "src_VisitAgeInDays", "src_VisitAgeInMonths", "src_VisitAgeInYears",
            "src_VisitKitLabel1", "src_VisitKitLabel2", "src_VisitKitTypeDescription", "src_VisitLastChangeDate",
            "src_VisitNumber", "src_VisitOccurredOnDate", "src_VisitSpecimenCollectionDate",
            "src_VisitCompositeIdentifier", "src_VisitWeekNumber", "src_VisitDate", "src_VisitDescription",
            "src_VisitRandomizationNumber", "src_VisitSpecimenReceiptDate", "src_VisitTransmittalNumber",
            "src_VisitTreatmentGroup", "src_VisitTreatmentGroupDesc", "src_VisitIsMicroPending", "src_GroupCode",
            "src_GroupDescription", "src_GroupType", "src_GroupCancelCode", "src_GroupCancelDescription",
            "src_GroupLastReportedDate", "src_ContainerBarcode", "src_ContainerExpectedClass",
            "src_ContainerExpectedCondition", "src_ContainerExpectedConditionDesc",
            "src_ContainerExpectedReturnEnvCondition", "src_ContainerIsReturnBatched",
            "src_ContainerIsReturnMandatory", "src_ContainerIssponsorblinded", "src_ContainerLabel1:",
            "src_ContainerLabel2", "src_ContainerNumber", "src_ContainerOriginatingSystemID",
            "src_ContainerParentNumber", "src_ContainerRackID", "src_ContainerRackPosition",
            "src_ContainerReceiptDate", "src_ContainerShipAddress1", "src_ContainerShipAddress2",
            "src_ContainerShipAddress3", "src_ContainerShipCity", "src_ContainerShipCountry",
            "src_ContainerShipCourier", "src_ContainerShipPostalCode", "src_ContainerShipRefLabContact",
            "src_ContainerShipRefLabDescription", "src_ContainerShipState", "src_ContainerSourceContainerNumber",
            "src_ContainerSpecimenClass", "src_ContainerSpecimenClassDescription", "src_ContainerSpecimenCondition",
            "src_ContainerSpecimenConditionDesc", "src_ContainerSpecimenDispositionDate", "src_ContainerSpecimenFootNote",
            "src_ContainerSpecimenFullLocation", "src_ContainerSpecimenLocationDesc", "src_ContainerSpecimenLocationID",
            "src_ContainerSpecimenPackageID", "src_ContainerSpecimenPackagePosition",
            "src_ContainerSpecimenShipCondition", "src_ContainerSpecimenShipConditionDesc",
            "src_ContainerSpecimenShipDate", "src_ContainerSpecimenShipNumber", "src_ContainerSpecimenShipStatus",
            "src_ContainerSpecimenShipStatusCheckDate", "src_ContainerSpecimenShipTrackingNumber",
            "src_ContainerSpecimenStatus", "src_ContainerSpecimenType", "src_ContainerSpecimenTypeDesc",
            "src_ContainerSpecimenUSPID", "src_ContainerStorageCondition", "src_ContainerStorageConditionDesc",
            "src_ContainerTubeID", "src_ContainerTestTestCode", "src_ContainerType", "src_ContainerTypeDescription",
            "src_LabTestCode", "src_LabTestIsPending", "src_LabTestReportingUnit", "src_LabTestSIUnit",
            "src_LabTestCancelCode", "src_LabTestDescription", "src_LabTestCancelDescription",
            "src_LabTestConventionalUnit", "src_LabTestContainerNumber", "src_LabTestConventionalToSIFactor",
            "src_LabTestConventionalUnitLOINCCode", "src_LabTestHL7Code", "src_LabTestHL7Description",
            "src_LabTestName", "src_LabTestNumberOfResults", "src_LabTestPerformingLabCode",
            "src_LabTestResultedDate", "src_LabTestResultsFiledDate", "src_LabTestSampleConditionCode",
            "src_LabTestSampleConditionDescription", "src_LabTestSIUnitLOINCCode",
            "src_LabTestSIToConventionalFactor", "src_LabTestAmbientStabilityInHours",
            "src_LabTestFrozenStabilityInHours", "src_LabTestRefrigeratedStabilityInHours",
            "src_LabResultValueInConventionalUnits", "src_LabResultValueInSIUnits",
            "src_LabResultValueInReportingUnits", "src_LabResultAlertFlag", "src_LabResultResultComment",
            "src_LabResultResultCommentText", "src_LabResultResultType", "src_LabResultSequenceNumber",
            "src_LabResultResultCode", "src_LabResultDeltaFlag", "src_LabResultExclusionFlag",
            "src_LabResultSponsorFlag", "src_LabResultValueAsEntered", "src_ResultRefRangeDefLowValue",
            "src_ResultRefRangeDefLowAlertValue", "src_ResultRefRangeDefLowPanicValue",
            "src_ResultRefRangeDefLowTelephoneValue", "src_ResultRefRangeDefHighValue",
            "src_ResultRefRangeDefHighAlertValue", "src_ResultRefRangeDefHighPanicValue",
            "src_ResultRefRangeDefHighTelephoneValue", "src_ResultRefRangeDefTextValue", "src_ResultRefRangeDefUnits",
            "src_ResultRefRangeRefRangeEffectiveDate", "src_ResultRefRangeRefRangeFromAge",
            "src_ResultRefRangeRefRangeToAge", "src_ResultRefRangeSIUnits", "src_ResultRefRangeSITextValue",
            "src_ResultRefRangeSILowValue", "src_ResultRefRangeSIHighValue", "src_ResultRefRangeSIHighAlertValue",
            "src_ResultRefRangeSIHighPanicValue", "src_ResultRefRangeSIHighTelephoneValue",
            "src_ResultRefRangeSILowAlertValue", "src_ResultRefRangeSILowPanicValue",
            "src_ResultRefRangeSILowTelephoneValue", "src_ResultRefRangeConvTextValue", "src_ResultRefRangeConvUnits",
            "src_ResultRefRangeConvLowValue", "src_ResultRefRangeConvHighValue", "src_ResultRefRangeConvHighAlertValue",
            "src_ResultRefRangeConvHighPanicValue", "src_ResultRefRangeConvHighTelephoneValue",
            "src_ResultRefRangeConvLowAlertValue", "src_ResultRefRangeConvLowPanicValue",
            "src_ResultRefRangeConvLowTelephoneValue", "src_LabTestBlindDataTransfer", "src_LabTestBlindInvestigator",
            "src_LabTestBlindSponsor", "src_LabTestBlindThirdParty", "src_MicroSpecimenBlindDataTransfer",
            "src_MicroSpecimenBlindInvestigator", "src_MicroSpecimenBlindSponsor", "src_MicroSpecimenBlindThirdParty",
            "src_MicroAddObservationCodeString", "src_MicroAddObservationDescription",
            "src_MicroAddObservationObservation", "src_MicroAddObservationTestCode", "src_MicroAddObservationTestType",
            "src_MicroGramStainCancelCode", "src_MicroGramStainCancelDescription", "src_MicroGramStainDescription",
            "src_MicroGramStainGroupCode", "src_MicroGramStainGroupDescription", "src_MicroGramStainTestCode",
            "src_MicroGramStainFinding", "src_MicroGramStainFindingObservationResultCode",
            "src_MicroGramStainFindingResult", "src_MicroGramStainFindingResultCode",
            "src_MicroGramStainFindingSequenceNumber", "src_MicroOrganismCodeString", "src_MicroOrganismComment",
            "src_MicroOrganismDescription", "src_MicroOrganismGrowthCodeString",
            "src_MicroOrganismGrowthDescription", "src_MicroOrganismGrowthObservation", "src_MicroOrganismGrowthTestCode",
            "src_MicroOrganismName", "src_MicroOrganismSequenceNumber", "src_MicroOrganismTestCode",
            "src_MicroPanelDescription", "src_MicroPanelTestCode", "src_MicroPanelType", "src_MicroPanelResultDrugName",
            "src_MicroPanelResultInterpretation", "src_MicroPanelResult", "src_MicroPanelResultSequenceNumber",
            "src_MicroPanelResultUnits", "src_MicroSpecimenCancelCode", "src_MicroSpecimenCancelDescription",
            "src_MicroSpecimenCodeString", "src_MicroSpecimenDescription", "src_MicroSpecimenName",
            "src_MicroSpecimenResultedDate", "src_MicroSpecimenResultsFiledDate", "src_MicroSpecimenTestCode",
            "src_MicroSpecimenTestCode"
]
