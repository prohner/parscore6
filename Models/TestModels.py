from google.appengine.ext import db
from google.appengine.ext.db import polymodel
from google.appengine.api import users
from ProjectModels import *
from decimal import *

class TestBaseCounter(db.Model):
	count = db.IntegerProperty()

class TestBase(polymodel.PolyModel):

	respondents = {
		"a" : "Adult",
		"p" : "Parent",
		"c" : "Child",
		"o" : "Other"
	}

	subjects = {
		"f" : "Father",
		"m" : "Mother",
		"p" : "Other"
	}

	AdultPARQControlFatherName		= "Adult PARQ/Control: Father"
	AdultPARQControlMotherName		= "Adult PARQ/Control: Mother"
	ParentPARQControlName			= "Parent PARQ/Control"
	ChildPARQControlFatherName		= "Child PARQ/Control: Father"
	ChildPARQControlMotherName		= "Child PARQ/Control: Mother"
	PARQControlInfantName			= "PARQ/Control Infant"

	AdultPARQControlFatherShortName	= "Adult PARQ/Control: Father (short)"
	AdultPARQControlMotherShortName	= "Adult PARQ/Control: Mother (short)"
	ParentPARQControlShortName		= "Parent PARQ/Control (short)"
	ChildPARQControlFatherShortName	= "Child PARQ/Control: Father (short)"
	ChildPARQControlMotherShortName	= "Child PARQ/Control: Mother (short)"
	TeacherPARQControlShortName		= "Teacher PARQ/Control (short)"

	ChildPARQFatherName				= "Child PARQ: Father"
	ChildPARQMotherName				= "Child PARQ: Mother"
	AdultPARQFatherName				= "Adult PARQ: Father"
	AdultPARQMotherName				= "Adult PARQ: Mother"
	ParentPARQName					= "Parent PARQ"
	IARQName						= "Intimate Adult Relationship Questionnaire"

	ChildPARQFatherShortName		= "Child PARQ: Father (short)"
	ChildPARQMotherShortName		= "Child PARQ: Mother (short)"
	AdultPARQFatherShortName		= "Adult PARQ: Father (short)"
	AdultPARQMotherShortName		= "Adult PARQ: Mother (short)"
	ParentPARQShortName				= "Parent PARQ (short)"
	IARQShortName					= "Intimate Adult Relationship Questionnaire (short)"

	ChildPAQName					= "Child PAQ"
	AdultPAQName					= "Adult PAQ"
	IPARCQName						= "Intimate Partner Acceptance-Rejection/Control Questionnaire"
	IPAQName						= "Intimate Partner Attachment Questionnaire"
	TESCName						= "Teacher's Evaluation of Student's Conduct"
	IRAQName						= "Interpersonal Relationship Anxiety Questionnaire"
	ESARQName						= "Elder Sibling Acceptance-Rejection/Control Questionnaire"
	SUQName							= "Substance Use Questionnaire"
	YouthThreePQName			    = "Parental Power-Prestige Questionnaire: Youth"
	AdultThreePQName			    = "Parental Power-Prestige Questionnaire: Adult"
	PECCName						= "Parent's Evaluation of Child's Conduct"

	YouthPPQMotherName				= "Youth PPQ: Mother"
	YouthPPQFatherName				= "Youth PPQ: Father"
	AdultPPQMotherName				= "Adult PPQ: Mother"
	AdultPPQFatherName				= "Adult PPQ: Father"
	ParentPPQName					= "Parent PPQ"
	ILARQName						= "In-Law Acceptance-Rejection Questionnaire"

	BestFriendARQName				= "Best Friend ARQ"
	BestFriendARQShortName			= "Best Friend ARQ (short)"

	# 2016-12-11 Added new tests
	EarlyChildhoodBFARQName			= "Early Childhood BFARQ"
	ECARQShortFatherName			= "ECARQ (short form): Father"
	ECARQShortMotherName			= "ECARQ (short form): Mother"
	GenderInequalityName			= "Gender Inequality Scale"
	ILARQControlName				= "ILARQ/Control"
	IPARLSName						= "IPARLS"
	IRSSName						= "IRSS"
	ILARQFatherInLawName			= "ILAR-CQ Father-In-Law"
	ILARQMotherInLawName			= "ILAR-CQ Mother-In-Law"
	SARQName						= "Supervisor Acceptance-Rejection Questionnaire"
	MARQCName						= "Manager Acceptance-Rejection Questionnaire/Control"

	# 2018-04-19 Added new tests
	OARQName						= "Organizational ARQ"
	OARQShortName					= "Organizational ARQ (short)"
	OARQControlName					= "Organizational ARQ/Control"
	OARQControlShortName			= "Organizational ARQ/Control (short)"

	# =================================
	# Fully spelled out versions of names
	AdultPARQControlFatherNameLong		= "Adult Parental Acceptance Rejection Questionnaire/Control: Father"
	AdultPARQControlMotherNameLong		= "Adult Parental Acceptance Rejection Questionnaire/Control: Mother"
	ParentPARQControlNameLong			= "Parent Parental Acceptance Rejection Questionnaire/Control"
	ChildPARQControlFatherNameLong		= "Child Parental Acceptance Rejection Questionnaire/Control: Father"
	ChildPARQControlMotherNameLong		= "Child Parental Acceptance Rejection Questionnaire/Control: Mother"
	PARQControlInfantNameLong			= "Parental Acceptance Rejection Questionnaire/Control Infant"

	AdultPARQControlFatherShortNameLong	= "Adult Parental Acceptance Rejection Questionnaire/Control: Father (short)"
	AdultPARQControlMotherShortNameLong	= "Adult Parental Acceptance Rejection Questionnaire/Control: Mother (short)"
	ParentPARQControlShortNameLong		= "Parent Parental Acceptance Rejection Questionnaire/Control (short)"
	ChildPARQControlFatherShortNameLong	= "Child Parental Acceptance Rejection Questionnaire/Control: Father (short)"
	ChildPARQControlMotherShortNameLong	= "Child Parental Acceptance Rejection Questionnaire/Control: Mother (short)"
	TeacherPARQControlShortNameLong		= "Teacher Parental Acceptance Rejection Questionnaire/Control (short)"

	ChildPARQFatherNameLong				= "Child Parental Acceptance Rejection Questionnaire: Father"
	ChildPARQMotherNameLong				= "Child Parental Acceptance Rejection Questionnaire: Mother"
	AdultPARQFatherNameLong				= "Adult Parental Acceptance Rejection Questionnaire: Father"
	AdultPARQMotherNameLong				= "Adult Parental Acceptance Rejection Questionnaire: Mother"
	ParentPARQNameLong					= "Parent Parental Acceptance Rejection Questionnaire"
	IARQNameLong						= "Intimate Adult Relationship Questionnaire"

	ChildPARQFatherShortNameLong		= "Child Parental Acceptance Rejection Questionnaire: Father (short)"
	ChildPARQMotherShortNameLong		= "Child Parental Acceptance Rejection Questionnaire: Mother (short)"
	AdultPARQFatherShortNameLong		= "Adult Parental Acceptance Rejection Questionnaire: Father (short)"
	AdultPARQMotherShortNameLong		= "Adult Parental Acceptance Rejection Questionnaire: Mother (short)"
	ParentPARQShortNameLong				= "Parent Parental Acceptance Rejection Questionnaire (short)"
	IARQShortNameLong					= "Intimate Adult Relationship Questionnaire (short)"

	ChildPAQNameLong					= "Child Parental Acceptance Questionnaire"
	AdultPAQNameLong					= "Adult Parental Acceptance Questionnaire"
	IPARCQNameLong						= "Intimate Partner Acceptance-Rejection/Control Questionnaire"
	IPAQNameLong						= "Intimate Partner Attachment Questionnaire"
	TESCNameLong						= "Teacher Evaluation of Student Conduct"
	IRAQNameLong						= "Interpersonal Relationship Anxiety Questionnaire"
	ESARQNameLong						= "Elder Sibling Acceptance-Rejection/Control Questionnaire"
	SUQNameLong							= "Substance Use Questionnaire"
	YouthThreePQNameLong			    = "Parental Power-Prestige Questionnaire: Youth"
	AdultThreePQNameLong			    = "Parental Power-Prestige Questionnaire: Adult"
	PECCNameLong						= "Parent Evaluation of Child Conduct"

	YouthPPQMotherNameLong				= "Youth Parental Punishment Questionnaire: Mother"
	YouthPPQFatherNameLong				= "Youth Parental Punishment Questionnaire: Father"
	AdultPPQMotherNameLong				= "Adult Parental Punishment Questionnaire: Mother"
	AdultPPQFatherNameLong				= "Adult Parental Punishment Questionnaire: Father"
	ParentPPQNameLong					= "Parent Parental Punishment Questionnaire"
	ILARQNameLong						= "In-Law Acceptance-Rejection Questionnaire"
	MARQCNameLong						= "Manager Acceptance-Rejection Questionnaire/Control"

	BestFriendARQNameLong				= "Best Friend Acceptance Rejection Questionnaire"
	BestFriendARQShortNameLong			= "Best Friend Acceptance Rejection Questionnaire (short)"

	# 2016-12-11 Added new tests
	EarlyChildhoodBFARQNameLong			= "Early Childhood BFARQ Questionnaire"
	ECARQShortFatherNameLong			= "ECARQ (short form): Father Questionnaire"
	ECARQShortMotherNameLong			= "ECARQ (short form): Mother Questionnaire"
	GenderInequalityNameLong			= "Gender Inequality Scale Questionnaire"
	ILARQControlNameLong				= "In-Law Acceptance Rejection Questionnaire/Control"
	IPARLSNameLong						= "Intimate Partner Acceptance-Rejection Loneliness Scale Questionnaire"
	IRSSNameLong						= "Interpersonal Rejection Sensitivity Scale"
	ILARQFatherInLawNameLong			= "In-Law Acceptance-Rejection/Control Questionnaire: Father-In-Law Questionnaire"
	ILARQMotherInLawNameLong			= "In-Law Acceptance-Rejection/Control Questionnaire: Mother-In-Law Questionnaire"
	SARQNameLong						= "Supervisor Acceptance-Rejection Questionnaire"

	# 2018-04-19 Added new tests
	OARQNameLong					= "Organizational Acceptance-Rejection Questionnaire"
	OARQShortNameLong				= "Organizational Acceptance-Rejection Questionnaire (short)"
	OARQControlNameLong				= "Organizational Acceptance-Rejection/Control Questionnaire"
	OARQControlShortNameLong		= "Organizational Acceptance-Rejection/Control Questionnaire (short)"

	# =================================
	# Not yet done
	# =================================

	@staticmethod
	def get_project_test_list():
		return [TestBase.ESARQName,
				"T:In-Law Acceptance-Rejection Questionnaire",
				TestBase.ILARQName,
				"END:",
				TestBase.IRAQName,
				TestBase.IARQName,
				TestBase.IARQShortName,
				TestBase.IPARCQName,
				TestBase.IPAQName,
				"T:PARQ Standard form",
				TestBase.AdultPARQFatherName,
				TestBase.AdultPARQMotherName,
				TestBase.ChildPARQFatherName,
				TestBase.ChildPARQMotherName,
				"T:PARQ Short form",
				TestBase.AdultPARQFatherShortName,
				TestBase.AdultPARQMotherShortName,
				TestBase.ChildPARQFatherShortName,
				TestBase.ChildPARQMotherShortName,
				"T:PARQ/Control Standard form",
				TestBase.AdultPARQControlFatherName,
				TestBase.AdultPARQControlMotherName,
				TestBase.ChildPARQControlFatherName,
				TestBase.ChildPARQControlMotherName,
				"T:PARQ/Control Short form",
				TestBase.AdultPARQControlFatherShortName,
				TestBase.AdultPARQControlMotherShortName,
				TestBase.ChildPARQControlFatherShortName,
				TestBase.ChildPARQControlMotherShortName,
				"T:Parental Power-Prestige Questionnaire",
				TestBase.YouthThreePQName,
				TestBase.AdultThreePQName,
				"END:",
				TestBase.PECCName,
				"T:Personality Assessment Questionnaire",
				TestBase.AdultPAQName,
				TestBase.ChildPAQName,
				"T:Physical Punishment Questionnaire",
				TestBase.AdultPPQFatherName,
				TestBase.AdultPPQMotherName,
				TestBase.ParentPPQName,
				TestBase.YouthPPQFatherName,
				TestBase.YouthPPQMotherName,
				"END:",
				TestBase.SUQName,
				TestBase.TESCName
				]

	@staticmethod
	def get_test(test_name, key):
		t = None
		if test_name == TestBase.AdultPARQControlFatherName:
			if key:
				t = AdultPARQControlFather.get(key)
			else:
				t = AdultPARQControlFather(test_name = TestBase.AdultPARQControlFatherName)
		elif test_name == TestBase.AdultPARQControlMotherName:
			if key:
				t = AdultPARQControlMother.get(key)
			else:
				t = AdultPARQControlMother(test_name = TestBase.AdultPARQControlMotherName)
		elif test_name == TestBase.ParentPARQControlName:
			if key:
				t = ParentPARQControl.get(key)
			else:
				t = ParentPARQControl(test_name = TestBase.ParentPARQControlName)
		elif test_name == TestBase.ChildPARQControlFatherName:
			if key:
				t = ChildPARQControlFather.get(key)
			else:
				t = ChildPARQControlFather(test_name = TestBase.ChildPARQControlFatherName)
		elif test_name == TestBase.ChildPARQControlMotherName:
			if key:
				t = ChildPARQControlMother.get(key)
			else:
				t = ChildPARQControlMother(test_name = TestBase.ChildPARQControlMotherName)
		elif test_name == TestBase.PARQControlInfantName:
			if key:
				t = PARQControlInfant.get(key)
			else:
				t = PARQControlInfant(test_name = TestBase.PARQControlInfantName)
		elif test_name == TestBase.AdultPARQControlFatherShortName:
			if key:
				t = AdultPARQControlFatherShort.get(key)
			else:
				t = AdultPARQControlFatherShort(test_name = TestBase.AdultPARQControlFatherShortName)
		elif test_name == TestBase.AdultPARQControlMotherShortName:
			if key:
				t = AdultPARQControlMotherShort.get(key)
			else:
				t = AdultPARQControlMotherShort(test_name = TestBase.AdultPARQControlMotherShortName)
		elif test_name == TestBase.ParentPARQControlShortName:
			if key:
				t = ParentPARQControlShort.get(key)
			else:
				t = ParentPARQControlShort(test_name = TestBase.ParentPARQControlShortName)
		elif test_name == TestBase.ChildPARQControlFatherShortName:
			if key:
				t = ChildPARQControlFatherShort.get(key)
			else:
				t = ChildPARQControlFatherShort(test_name = TestBase.ChildPARQControlFatherShortName)
		elif test_name == TestBase.ChildPARQControlMotherShortName:
			if key:
				t = ChildPARQControlMotherShort.get(key)
			else:
				t = ChildPARQControlMotherShort(test_name = TestBase.ChildPARQControlMotherShortName)
		elif test_name == TestBase.TeacherPARQControlShortName:
			if key:
				t = TeacherPARQControlShort.get(key)
			else:
				t = TeacherPARQControlShort(test_name = TestBase.TeacherPARQControlShortName)
		elif test_name == TestBase.ChildPARQFatherName:
			if key:
				t = ChildPARQFather.get(key)
			else:
				t = ChildPARQFather(test_name = TestBase.ChildPARQFatherName)
		elif test_name == TestBase.ChildPARQMotherName:
			if key:
				t = ChildPARQMother.get(key)
			else:
				t = ChildPARQMother(test_name = TestBase.ChildPARQMotherName)
		elif test_name == TestBase.AdultPARQFatherName:
			if key:
				t = AdultPARQFather.get(key)
			else:
				t = AdultPARQFather(test_name = TestBase.AdultPARQFatherName)
		elif test_name == TestBase.AdultPARQMotherName:
			if key:
				t = AdultPARQMother.get(key)
			else:
				t = AdultPARQMother(test_name = TestBase.AdultPARQMotherName)
		elif test_name == TestBase.ParentPARQName:
			if key:
				t = ParentPARQ.get(key)
			else:
				t = ParentPARQ(test_name = TestBase.ParentPARQName)
		elif test_name == TestBase.ChildPARQFatherShortName:
			if key:
				t = ChildPARQFatherShort.get(key)
			else:
				t = ChildPARQFatherShort(test_name = TestBase.ChildPARQFatherShortName)
		elif test_name == TestBase.ChildPARQMotherShortName:
			if key:
				t = ChildPARQMotherShort.get(key)
			else:
				t = ChildPARQMotherShort(test_name = TestBase.ChildPARQMotherShortName)
		elif test_name == TestBase.AdultPARQFatherShortName:
			if key:
				t = AdultPARQFatherShort.get(key)
			else:
				t = AdultPARQFatherShort(test_name = TestBase.AdultPARQFatherShortName)
		elif test_name == TestBase.AdultPARQMotherShortName:
			if key:
				t = AdultPARQMotherShort.get(key)
			else:
				t = AdultPARQMotherShort(test_name = TestBase.AdultPARQMotherShortName)
		elif test_name == TestBase.ParentPARQShortName:
			if key:
				t = ParentPARQShort.get(key)
			else:
				t = ParentPARQShort(test_name = TestBase.ParentPARQShortName)
		elif test_name == TestBase.ChildPAQName:
			if key:
				t = ChildPAQ.get(key)
			else:
				t = ChildPAQ(test_name = TestBase.ChildPAQName)
		elif test_name == TestBase.AdultPAQName:
			if key:
				t = AdultPAQ.get(key)
			else:
				t = AdultPAQ(test_name = TestBase.AdultPAQName)
		elif test_name == TestBase.IPARCQName:
			if key:
				t = IPARCQ.get(key)
			else:
				t = IPARCQ(test_name = TestBase.IPARCQName)
		elif test_name == TestBase.IPAQName:
			if key:
				t = IPAQ.get(key)
			else:
				t = IPAQ(test_name = TestBase.IPAQName)
		elif test_name == TestBase.TESCName:
			if key:
				t = TESC.get(key)
			else:
				t = TESC(test_name = TestBase.TESCName)
		elif test_name == TestBase.IARQName:
			if key:
				t = IARQ.get(key)
			else:
				t = IARQ(test_name = TestBase.IARQName)
		elif test_name == TestBase.IARQShortName:
			if key:
				t = IARQShort.get(key)
			else:
				t = IARQShort(test_name = TestBase.IARQShortName)
		elif test_name == TestBase.IRAQName:
			if key:
				t = IRAQ.get(key)
			else:
				t = IRAQ(test_name = TestBase.IRAQName)
		elif test_name == TestBase.ESARQName:
			if key:
				t = ESARQ.get(key)
			else:
				t = ESARQ(test_name = TestBase.ESARQName)
		elif test_name == TestBase.SUQName:
			if key:
				t = SUQ.get(key)
			else:
				t = SUQ(test_name = TestBase.SUQName)
		elif test_name == TestBase.YouthThreePQName:
			if key:
				t = YouthThreePQ.get(key)
			else:
				t = YouthThreePQ(test_name = TestBase.YouthThreePQName)
		elif test_name == TestBase.AdultThreePQName:
			if key:
				t = AdultThreePQ.get(key)
			else:
				t = AdultThreePQ(test_name = TestBase.AdultThreePQName)
		elif test_name == TestBase.PECCName:
			if key:
				t = PECC.get(key)
			else:
				t = PECC(test_name = TestBase.PECCName)
		elif test_name == TestBase.YouthPPQMotherName:
			if key:
				t = YouthPPQMother.get(key)
			else:
				t = YouthPPQMother(test_name = TestBase.YouthPPQMotherName)
		elif test_name == TestBase.YouthPPQFatherName:
			if key:
				t = YouthPPQFather.get(key)
			else:
				t = YouthPPQFather(test_name = TestBase.YouthPPQFatherName)
		elif test_name == TestBase.AdultPPQMotherName:
			if key:
				t = AdultPPQMother.get(key)
			else:
				t = AdultPPQMother(test_name = TestBase.AdultPPQMotherName)
		elif test_name == TestBase.AdultPPQFatherName:
			if key:
				t = AdultPPQFather.get(key)
			else:
				t = AdultPPQFather(test_name = TestBase.AdultPPQFatherName)
		elif test_name == TestBase.ParentPPQName:
			if key:
				t = ParentPPQ.get(key)
			else:
				t = ParentPPQ(test_name = TestBase.ParentPPQName)
		elif test_name == TestBase.ILARQName:
			if key:
				t = ILARQ.get(key)
			else:
				t = ILARQ(test_name = TestBase.ILARQName)
		elif test_name == TestBase.BestFriendARQName:
			if key:
				t = BestFriendARQ.get(key)
			else:
				t = BestFriendARQ(test_name = TestBase.BestFriendARQName)
		elif test_name == TestBase.BestFriendARQShortName:
			if key:
				t = BestFriendARQShort.get(key)
			else:
				t = BestFriendARQShort(test_name = TestBase.BestFriendARQShortName)
		elif test_name == TestBase.EarlyChildhoodBFARQName:
			if key:
				t = EarlyChildhoodBFARQShort.get(key)
			else:
				t = EarlyChildhoodBFARQShort(test_name = TestBase.EarlyChildhoodBFARQName)
		elif test_name == TestBase.ECARQShortFatherName:
			if key:
				t = ECARQShortFather.get(key)
			else:
				t = ECARQShortFather(test_name = TestBase.ECARQShortFatherName)
		elif test_name == TestBase.ECARQShortMotherName:
			if key:
				t = ECARQShortMother.get(key)
			else:
				t = ECARQShortMother(test_name = TestBase.ECARQShortMotherName)
		elif test_name == TestBase.ILARQFatherInLawName:
			if key:
				t = AdultPARQControlFatherInLawShort.get(key)
			else:
				t = AdultPARQControlFatherInLawShort(test_name = TestBase.ILARQFatherInLawName)
		elif test_name == TestBase.ILARQMotherInLawName:
			if key:
				t = AdultPARQControlMotherInLawShort.get(key)
			else:
				t = AdultPARQControlMotherInLawShort(test_name = TestBase.ILARQMotherInLawName)
		elif test_name == TestBase.GenderInequalityName:
			if key:
				t = GenderInequality.get(key)
			else:
				t = GenderInequality(test_name = TestBase.GenderInequalityName)
		elif test_name == TestBase.ILARQControlName:
			if key:
				t = ILARQControl.get(key)
			else:
				t = ILARQControl(test_name = TestBase.ILARQControlName)
		elif test_name == TestBase.IPARLSName:
			if key:
				t = IPARLS.get(key)
			else:
				t = IPARLS(test_name = TestBase.IPARLSName)
		elif test_name == TestBase.IRSSName:
			if key:
				t = IRSS.get(key)
			else:
				t = IRSS(test_name = TestBase.IRSSName)
		elif test_name == TestBase.SARQName:
			if key:
				t = SARQ.get(key)
			else:
				t = SARQ(test_name = TestBase.SARQName)
		elif test_name == TestBase.OARQControlName:
			if key:
				t = OARQControl.get(key)
			else:
				t = OARQControl(test_name = TestBase.OARQControlName)
		elif test_name == TestBase.OARQControlShortName:
			if key:
				t = OARQControlShort.get(key)
			else:
				t = OARQControlShort(test_name = TestBase.OARQControlShortName)
		elif test_name == TestBase.OARQName:
			if key:
				t = OARQ.get(key)
			else:
				t = OARQ(test_name = TestBase.OARQName)
		elif test_name == TestBase.OARQShortName:
			if key:
				t = OARQShort.get(key)
			else:
				t = OARQShort(test_name = TestBase.OARQShortName)

		if not key:
			t.sets()

		return t

	def as_number(self, i):
		if i == None:
			return 0
		else:
			return i

	def get_scores_matrix(self):
		return [	[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1],
					[-1,	-1,	-1,	-1,	-1,	-1,	-1]]

	def get_reverses_matrix(self):
		return [[0,	0,	0,	0,	0,	0,	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0,	0,	0,	0,	0],
				[0,	0,	0,	0,	0,	0,	0],
				[0,	0,	0,	0,	0,	0,	0],
				[0,	0,	0,	0,	0,	0,	0],
				[0,	0,	0,	0,	0,	0,	0]]

	def get_item_score(self, row, column, matrix, cannot_be_reversed):
		reverses = self.get_reverses_matrix()
		sum = 0

		if matrix[row][column] == "" or matrix[row][column] == " " or matrix[row][column] == None:
			item = 0
		else:
			item = int(matrix[row][column])

		if reverses[row][column] == 0 or cannot_be_reversed:
			sum = item
		else:
			if item > 0:
				sum = 5 - item
		return sum

	def get_dimension_score(self, column, matrix, max_zeroes, dimension_name):
		answered_count		= 0
		answered_total 		= 0
		score_type 			= "" #"Complete" #, "Includes Avgs.", "Incomplete"]))
		rows 				= len(matrix)
		msg 				= ""
		number_of_zeroes 	= 0
		average				= -1
		reverses 			= self.get_reverses_matrix()

		for row in range(0, rows):
			item_score = self.get_item_score(row, column, matrix, False)
			#if column == 1:
			#	msg += "%d == %d<br>" % (row, item_score)

			if item_score > 0:
				answered_count += 1
				answered_total += item_score
			else:
				if matrix[row][column] >= 0:
					number_of_zeroes += 1

		if number_of_zeroes > max_zeroes:
			msg 		+= "More than %(max_zeroes)d %(verb)s blank on the %(dimension)s scale." % { 'max_zeroes' : max_zeroes, 'verb' : 'are' if max_zeroes > 1 else 'is' , 'dimension' : dimension_name }
			#score_type	= "Incomplete"
		elif number_of_zeroes > 0:
			score_type	= "Includes Avgs."
			average		= int((float(answered_total) / float(answered_count)) + .5)
			msg			+= "%s: ttl=%d, cnt=%d, avg=%d." % (dimension_name, answered_total, answered_count, average)

			for row in range(0, rows):
				if int(matrix[row][column]) == 0:
					if reverses[row][column] == 1 and column == 0:
						matrix[row][column] = 5 - average
					else:
						matrix[row][column] = average
					#msg			+= "assigned %d at row=%d, col=%d (rev=%d)" % (matrix[row][column], row, column, reverses[row][column])

		sum	= 0
		for row in range(0, rows):
			item_score = self.get_item_score(row, column, matrix, False)
			if item_score >= 0:
				sum += item_score


		return sum, msg, score_type, number_of_zeroes, average

	def get_score(self):
		dbg = 0
		sum = 0
		msg = ""
		matrix = self.get_scores_matrix()
		rows = len(matrix)
		cols = len(matrix[0])

		dimension1_number_of_zeroes	= 0
		dimension2_number_of_zeroes	= 0
		dimension3_number_of_zeroes	= 0
		dimension4_number_of_zeroes	= 0
		dimension5_number_of_zeroes	= 0
		dimension6_number_of_zeroes	= 0
		dimension7_number_of_zeroes	= 0

		if cols >= 1:
			dimension_sum, new_msg, score_type, dimension1_number_of_zeroes, dim_avg = self.get_dimension_score(0, matrix, self.dimension1_max_unanswered_items, self.dimension1_name)
			self.dimension1_score_type	= score_type
			self.dimension1_score		= dimension_sum
			self.dimension1_average		= dim_avg
			msg 						+= new_msg
			if len(score_type) > 0:
				msg						+= self.dimension1_name + " " + score_type + "."
			if self.dimension1_is_control == False:
				sum 					+= dimension_sum

		if cols >= 2:
			dimension_sum, new_msg, score_type, dimension2_number_of_zeroes, dim_avg = self.get_dimension_score(1, matrix, self.dimension2_max_unanswered_items, self.dimension2_name)
			self.dimension2_score_type	= score_type
			self.dimension2_score		= dimension_sum
			self.dimension2_average		= dim_avg
			msg 						+= new_msg
			if len(score_type) > 0:
				msg 					+= self.dimension2_name + " " + score_type + "."
			if self.dimension2_is_control == False:
				sum 					+= dimension_sum

		if cols >= 3:
			dimension_sum, new_msg, score_type, dimension3_number_of_zeroes, dim_avg = self.get_dimension_score(2, matrix, self.dimension3_max_unanswered_items, self.dimension3_name)
			self.dimension3_score_type	= score_type
			self.dimension3_score		= dimension_sum
			self.dimension3_average		= dim_avg
			msg 						+= new_msg
			if len(score_type) > 0:
				msg 					+= self.dimension3_name + " " + score_type + "."
			if self.dimension3_is_control == False:
				sum 					+= dimension_sum

		if cols >= 4:
			dimension_sum, new_msg, score_type, dimension4_number_of_zeroes, dim_avg = self.get_dimension_score(3, matrix, self.dimension4_max_unanswered_items, self.dimension4_name)
			self.dimension4_score_type	= score_type
			self.dimension4_score		= dimension_sum
			self.dimension4_average		= dim_avg
			msg 						+= new_msg
			if len(score_type) > 0:
				msg 					+= self.dimension4_name + " " + score_type + "."
			if self.dimension4_is_control == False:
				sum 					+= dimension_sum

		if cols >= 5:
			dimension_sum, new_msg, score_type, dimension5_number_of_zeroes, dim_avg = self.get_dimension_score(4, matrix, self.dimension5_max_unanswered_items, self.dimension5_name)
			self.dimension5_score_type	= score_type
			self.dimension5_score		= dimension_sum
			self.dimension5_average		= dim_avg
			msg 						+= new_msg
			if len(score_type) > 0:
				msg						+= self.dimension5_name + " " + score_type + "."
			if self.dimension5_is_control == False:
				sum 					+= dimension_sum

		if cols >= 6:
			dimension_sum, new_msg, score_type, dimension6_number_of_zeroes, dim_avg = self.get_dimension_score(5, matrix, self.dimension6_max_unanswered_items, self.dimension6_name)
			self.dimension6_score_type	= score_type
			self.dimension6_score		= dimension_sum
			self.dimension6_average		= dim_avg
			msg 						+= new_msg
			if len(score_type) > 0:
				msg						+= self.dimension6_name + " " + score_type + "."
			if self.dimension6_is_control == False:
				sum 					+= dimension_sum

		if cols >= 7:
			dimension_sum, new_msg, score_type, dimension7_number_of_zeroes, dim_avg = self.get_dimension_score(6, matrix, self.dimension7_max_unanswered_items, self.dimension7_name)
			self.dimension7_score_type	= score_type
			self.dimension7_score		= dimension_sum
			self.dimension7_average		= dim_avg
			msg 						+= new_msg
			if len(score_type) > 0:
				msg						+= self.dimension7_name + " " + score_type + "."
			if self.dimension7_is_control == False:
				sum 					+= dimension_sum

		if dimension1_number_of_zeroes + dimension2_number_of_zeroes + dimension3_number_of_zeroes + dimension4_number_of_zeroes + dimension5_number_of_zeroes + dimension6_number_of_zeroes + dimension7_number_of_zeroes > self.max_unanswered_items:
			msg += "More than %d items %s blank on the questionnaire." % (self.max_unanswered_items, "are" if self.max_unanswered_items > 1 else "is")

		#msg += "Final score: %(score)d" % {'score':sum}
		self.score_messages = msg
		self.score = sum
		return sum

	def validate(self):
		msgs = None

		tests = TestBase.all()
		tests.filter("test_owner =", users.get_current_user())
		tests.filter("test_name =", self.test_name)
		tests.filter("test_id =", self.test_id)
		tests.filter("score >", 0)
		#tests.filter("key <>", self.key)
		if tests.count() > 1:
			msgs = """You have already used the id %s for a %s so this cannot be saved.""" % (self.test_id, self.test_name)

		return msgs

	def get_test_id_number(self):
		new_id = 1

		tests = TestBase.all()
		tests.filter("test_owner =", users.get_current_user())
		tests.filter("test_name =", self.test_name)
		tests.order("-test_id")
		for test in tests:
			if test.score > 0 and test.test_id.isdigit():
				new_id = int(self.as_number(test.test_id)) + 1
				break

		#new_id = "p_o =(%s), n=(%s)" % (users.get_current_user(), self.test_name)

		return new_id

	test_owner				= db.UserProperty()
	test_count_id			= db.IntegerProperty()
	test_id					= db.StringProperty()#required=True)
	question_count			= db.IntegerProperty()
	test_name				= db.StringProperty(required=True)
	score_messages			= db.TextProperty()
	date_added				= db.DateTimeProperty(auto_now_add=True)
	date_updated			= db.DateTimeProperty(auto_now=True)
	project					= db.ReferenceProperty(Project)
	subproject				= db.ReferenceProperty(SubProject)
	subject					= db.StringProperty(choices=set(["Mother", "Father", "Other", "Infant"]))
	respondent				= db.StringProperty(choices=set(["Adult", "Parent", "Child", "Teacher", "Youth"]))
	relationship			= db.StringProperty(choices=set(["Mother", "Father", "Other", "Infant", "Mother-in-Law", "Father-in-Law"]))
	question_labels 		= []
	show_relationship_dropdown	= False
	form_validation_function	= "validateTestForm"
	item_validation_function	= "checkEnteredValue"


	dimension1_name			= db.StringProperty()
	dimension2_name			= db.StringProperty()
	dimension3_name			= db.StringProperty()
	dimension4_name			= db.StringProperty()
	dimension5_name			= db.StringProperty()
	dimension6_name			= db.StringProperty()
	dimension7_name			= db.StringProperty()

	dimension1_score_type	= db.StringProperty(choices=set(["Complete", "Includes Avgs.", "Incomplete"]))
	dimension2_score_type	= db.StringProperty(choices=set(["Complete", "Includes Avgs.", "Incomplete"]))
	dimension3_score_type	= db.StringProperty(choices=set(["Complete", "Includes Avgs.", "Incomplete"]))
	dimension4_score_type	= db.StringProperty(choices=set(["Complete", "Includes Avgs.", "Incomplete"]))
	dimension5_score_type	= db.StringProperty(choices=set(["Complete", "Includes Avgs.", "Incomplete"]))
	dimension6_score_type	= db.StringProperty(choices=set(["Complete", "Includes Avgs.", "Incomplete"]))
	dimension7_score_type	= db.StringProperty(choices=set(["Complete", "Includes Avgs.", "Incomplete"]))

	dimension1_score		= db.IntegerProperty()
	dimension2_score		= db.IntegerProperty()
	dimension3_score		= db.IntegerProperty()
	dimension4_score		= db.IntegerProperty()
	dimension5_score		= db.IntegerProperty()
	dimension6_score		= db.IntegerProperty()
	dimension7_score		= db.IntegerProperty()
	score					= db.IntegerProperty()

	dimension1_average		= db.IntegerProperty()
	dimension2_average		= db.IntegerProperty()
	dimension3_average		= db.IntegerProperty()
	dimension4_average		= db.IntegerProperty()
	dimension5_average		= db.IntegerProperty()
	dimension6_average		= db.IntegerProperty()
	dimension7_average		= db.IntegerProperty()

	max_unanswered_items			= 0
	dimension1_max_unanswered_items	= 0
	dimension2_max_unanswered_items	= 0
	dimension3_max_unanswered_items	= 0
	dimension4_max_unanswered_items	= 0
	dimension5_max_unanswered_items	= 0
	dimension6_max_unanswered_items	= 0
	dimension7_max_unanswered_items	= 0

	dimension1_is_control	= False
	dimension2_is_control	= False
	dimension3_is_control	= False
	dimension4_is_control	= False
	dimension5_is_control	= False
	dimension6_is_control	= False
	dimension7_is_control	= False

	q1 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4", "5", "6"]))
	q2 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4", "5"]))
	q3 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4", "5"]))
	q4 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4", "5"]))
	q5 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4", "5"]))
	q6 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4", "5"]))
	q7 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4", "5"]))
	q8 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4", "5"]))
	q9 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4", "5"]))
	q10 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4", "5"]))
	q11 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q12 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q13 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q14 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q15 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q16 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q17 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q18 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q19 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q20 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q21 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q22 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q23 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q24 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q25 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q26 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q27 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q28 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q29 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q30 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q31 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q32 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q33 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q34 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q35 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q36 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q37 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q38 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q39 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q40 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q41 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q42 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q43 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q44 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q45 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q46 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q47 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q48 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q49 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q50 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q51 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q52 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q53 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q54 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q55 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q56 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q57 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q58 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q59 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q60 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q61 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q62 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q63 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q64 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q65 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q66 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q67 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q68 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q69 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q70 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q71 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q72 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))
	q73 = db.StringProperty()#choices=set(["0", "1", "2", "3", "4"]))

	def test_as_html_table(self, can_edit_test):
		scores_matrix = self.get_scores_matrix()
		reverses_matrix = self.get_reverses_matrix()
		h = ""
		h += """
				<tr>
					<td class="test_column_label" colspan=3>%s</td>
					<td class="test_column_spacer">&nbsp;</td>
					<td class="test_column_label" colspan=3>%s</td>
					<td class="test_column_spacer">&nbsp;</td>
					<td class="test_column_label" colspan=3>%s</td>
					<td class="test_column_spacer">&nbsp;</td>
					<td class="test_column_label" colspan=3>%s</td>
					<td class="test_column_spacer">&nbsp;</td>
					<td class="test_column_label" colspan=3>%s</td>
					<td class="test_column_spacer">&nbsp;</td>
					<td class="test_column_label" colspan=3>%s</td>
					<td class="test_column_spacer">&nbsp;</td>
					<td class="test_column_label" colspan=3>%s</td>
				</tr>
				""" % (	self.dimension1_name if self.dimension1_name != None else "&nbsp;",
						self.dimension2_name if self.dimension2_name != None else "&nbsp;",
						self.dimension3_name if self.dimension3_name != None else "&nbsp;",
						self.dimension4_name if self.dimension4_name != None else "&nbsp;",
						self.dimension5_name if self.dimension5_name != None else "&nbsp;",
						self.dimension6_name if self.dimension6_name != None else "",
						self.dimension7_name if self.dimension7_name != None else "")

		question_count = 0
		row_count = len(scores_matrix)
		column_count = len(scores_matrix[0])
		can_edit = (users.get_current_user() == self.test_owner) and can_edit_test

		for row in range(0, row_count):
			h += "<tr>"
			for col in range(0, column_count):
				if scores_matrix[row][col] != -1:
					question_count += 1
					if can_edit:
						s = """<input size=2 maxlength=1 name="q%d" id="q%d" value="%s" onblur="%s(this, %d)">""" % (question_count, question_count, scores_matrix[row][col] if scores_matrix[row][col] != None and scores_matrix[row][col] != "0" else "", self.item_validation_function, question_count)
					else:
						s = "%s" % scores_matrix[row][col]
					h += """
						<td class="test_label_cell">%d</td><td class="test_reverse_cell">%s</td><td class="test_data_cell">%s</td>
						""" % (question_count,
								"&nbsp;" if reverses_matrix[row][col] == 0 or col == 0 else "*",
								s)
				else:
					h += "<td colspan=3>&nbsp;</td>"
				h += "<td class=""test_column_spacer"">&nbsp;</td>"
			h += "</tr>"

		return h

	def score_messages_as_html(self):
		return self.score_messages.replace(".", ".<br />")

	def get_item_score_from_form(self, request, q_id):
		v = request.get(q_id)
		if v == '':
			v = "0"
		return v

	def store_form(self, request):
		self.test_id = request.get("test_id")
		self.q1 = self.get_item_score_from_form(request, "q1")
		self.q2 = self.get_item_score_from_form(request, "q2")
		self.q3 = self.get_item_score_from_form(request, "q3")
		self.q4 = self.get_item_score_from_form(request, "q4")
		self.q5 = self.get_item_score_from_form(request, "q5")
		self.q6 = self.get_item_score_from_form(request, "q6")
		self.q7 = self.get_item_score_from_form(request, "q7")
		self.q8 = self.get_item_score_from_form(request, "q8")
		self.q9 = self.get_item_score_from_form(request, "q9")
		self.q10 = self.get_item_score_from_form(request, "q10")
		self.q11 = self.get_item_score_from_form(request, "q11")
		self.q12 = self.get_item_score_from_form(request, "q12")
		self.q13 = self.get_item_score_from_form(request, "q13")
		self.q14 = self.get_item_score_from_form(request, "q14")
		self.q15 = self.get_item_score_from_form(request, "q15")
		self.q16 = self.get_item_score_from_form(request, "q16")
		self.q17 = self.get_item_score_from_form(request, "q17")
		self.q18 = self.get_item_score_from_form(request, "q18")
		self.q19 = self.get_item_score_from_form(request, "q19")
		self.q20 = self.get_item_score_from_form(request, "q20")
		self.q21 = self.get_item_score_from_form(request, "q21")
		self.q22 = self.get_item_score_from_form(request, "q22")
		self.q23 = self.get_item_score_from_form(request, "q23")
		self.q24 = self.get_item_score_from_form(request, "q24")
		self.q25 = self.get_item_score_from_form(request, "q25")
		self.q26 = self.get_item_score_from_form(request, "q26")
		self.q27 = self.get_item_score_from_form(request, "q27")
		self.q28 = self.get_item_score_from_form(request, "q28")
		self.q29 = self.get_item_score_from_form(request, "q29")
		self.q30 = self.get_item_score_from_form(request, "q30")
		self.q31 = self.get_item_score_from_form(request, "q31")
		self.q32 = self.get_item_score_from_form(request, "q32")
		self.q33 = self.get_item_score_from_form(request, "q33")
		self.q34 = self.get_item_score_from_form(request, "q34")
		self.q35 = self.get_item_score_from_form(request, "q35")
		self.q36 = self.get_item_score_from_form(request, "q36")
		self.q37 = self.get_item_score_from_form(request, "q37")
		self.q38 = self.get_item_score_from_form(request, "q38")
		self.q39 = self.get_item_score_from_form(request, "q39")
		self.q40 = self.get_item_score_from_form(request, "q40")
		self.q41 = self.get_item_score_from_form(request, "q41")
		self.q42 = self.get_item_score_from_form(request, "q42")
		self.q43 = self.get_item_score_from_form(request, "q43")
		self.q44 = self.get_item_score_from_form(request, "q44")
		self.q45 = self.get_item_score_from_form(request, "q45")
		self.q46 = self.get_item_score_from_form(request, "q46")
		self.q47 = self.get_item_score_from_form(request, "q47")
		self.q48 = self.get_item_score_from_form(request, "q48")
		self.q49 = self.get_item_score_from_form(request, "q49")
		self.q50 = self.get_item_score_from_form(request, "q50")
		self.q51 = self.get_item_score_from_form(request, "q51")
		self.q52 = self.get_item_score_from_form(request, "q52")
		self.q53 = self.get_item_score_from_form(request, "q53")
		self.q54 = self.get_item_score_from_form(request, "q54")
		self.q55 = self.get_item_score_from_form(request, "q55")
		self.q56 = self.get_item_score_from_form(request, "q56")
		self.q57 = self.get_item_score_from_form(request, "q57")
		self.q58 = self.get_item_score_from_form(request, "q58")
		self.q59 = self.get_item_score_from_form(request, "q59")
		self.q60 = self.get_item_score_from_form(request, "q60")
		self.q61 = self.get_item_score_from_form(request, "q61")
		self.q62 = self.get_item_score_from_form(request, "q62")
		self.q63 = self.get_item_score_from_form(request, "q63")
		self.q64 = self.get_item_score_from_form(request, "q64")
		self.q65 = self.get_item_score_from_form(request, "q65")
		self.q66 = self.get_item_score_from_form(request, "q66")
		self.q67 = self.get_item_score_from_form(request, "q67")
		self.q68 = self.get_item_score_from_form(request, "q68")
		self.q69 = self.get_item_score_from_form(request, "q69")
		self.q70 = self.get_item_score_from_form(request, "q70")
		self.q71 = self.get_item_score_from_form(request, "q71")
		self.q72 = self.get_item_score_from_form(request, "q72")
		self.q73 = self.get_item_score_from_form(request, "q73")

class PARQControl(TestBase):
	dimension1_name					= "Warmth/Affection"
	dimension2_name					= "Hostility/Aggression"
	dimension3_name					= "Indifference/Neglect"
	dimension4_name					= "Undifferentiated Rejection"
	dimension5_name					= "Control"
	max_unanswered_items			= 7
	dimension1_max_unanswered_items	= 3
	dimension2_max_unanswered_items	= 2
	dimension3_max_unanswered_items	= 2
	dimension4_max_unanswered_items	= 2
	dimension5_max_unanswered_items	= 2
	dimension5_is_control			= True



	def get_scores_matrix(self):
		return [	[self.q1,	self.q2,	self.q3,	self.q4,	self.q5 ],
					[self.q6,	self.q7,	self.q8, 	-1,			self.q9 ],
					[self.q10,	self.q11,	self.q12, 	self.q13,	self.q14],
					[self.q15,	self.q16,	self.q17, 	-1,			self.q18],
					[self.q19,	self.q20,	self.q21, 	self.q22,	self.q23],
					[self.q24,	self.q25,	self.q26, 	-1,			self.q27],
					[self.q28,	self.q29,	self.q30, 	self.q31,	self.q32],
					[self.q33,	self.q34,	self.q35, 	-1,			self.q36],
					[self.q37,	self.q38,	self.q39, 	self.q40,	self.q41],
					[self.q42,	self.q43,	self.q44, 	-1,			self.q45],
					[self.q46,	self.q47,	self.q48, 	self.q49,	self.q50],
					[self.q51,	self.q52,	self.q53, 	-1,			self.q54],
					[self.q55,	self.q56,	self.q57, 	self.q58,	self.q59],
					[self.q60,	self.q61,	self.q62, 	-1,			-1],
					[self.q63,	self.q64,	self.q65, 	self.q66,	-1],
					[self.q67,	-1,			-1, 		-1,			-1],
					[self.q68,	-1,			-1, 		self.q69,	-1],
					[self.q70,	-1,			-1, 		-1,			-1],
					[self.q71,	-1,			-1, 		self.q72,	-1],
					[self.q73,	-1,			-1, 		-1,			-1]]

	def get_reverses_matrix(self):
		return [[1,	0,	0,	0,	0],
				[1,	0,	1, 	0,	0],
				[1,	0,	0, 	0,	0],
				[1,	0,	1, 	0,	0],
				[1,	0,	0, 	0,	1],
				[1,	0,	1, 	0,	0],
				[1,	0,	0, 	0,	1],
				[1,	0,	1, 	0,	0],
				[1,	0,	0, 	0,	1],
				[1,	0,	1, 	0,	0],
				[1,	0,	0, 	0,	0],
				[1,	0,	1, 	0,	1],
				[1,	0,	0, 	0,	0],
				[1,	0,	1, 	0,	0],
				[1,	0,	0, 	0,	0],
				[1,	0,	0,	0,	0],
				[1,	0,	0,	0,	0],
				[1,	0,	0,	0,	0],
				[1,	0,	0,	0,	0],
				[1,	0,	0,	0,	0]]

	def get_download_header(self):
		header = "id Warmth Host indiff unrejn Control TotlPARQ "
		prefix = "??"
		suffix = ""
		question_count = 73

		if self.respondent == "Adult":
			prefix = "APC"
		elif self.respondent == "Child":
			prefix = "CPC"
		elif self.respondent == "Parent":
			prefix = "PPC"

		if self.subject == "Father":
			suffix = "F"
		elif self.subject == "Mother":
			suffix = "M"
		elif self.subject == "Infant":
			suffix = "I"
			question_count = 63

		for q in range(1, question_count + 1):
			header += " %s%d%s" % (prefix, q, suffix)

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		if self.test_name == TestBase.ParentPARQControlName:
			relationship = self.relationship + " "
		else:
			relationship = ""

		line = "%s %s%d %d %d %d %d %d" % (self.test_id, relationship, self.as_number(self.dimension1_score), self.as_number(self.dimension2_score), self.as_number(self.dimension3_score), self.as_number(self.dimension4_score), self.as_number(self.dimension5_score), self.as_number(self.score))

		matrix	= self.get_scores_matrix()
		rows	= len(matrix)
		for row in range(0, rows):
			for col in range(0, 5):
				item_score = self.get_item_score(row, col, matrix, False)
				if item_score >= 0:
					line += " %d" % item_score

		line += "\n"
		return line

class AdultPARQControlFather(PARQControl):
	def sets(self):
		self.relationship	= "Father"
		self.respondent		= "Adult"
		self.subject		= "Father"

class AdultPARQControlMother(PARQControl):
	def sets(self):
		self.relationship	= "Mother"
		self.respondent		= "Adult"
		self.subject		= "Mother"

class ParentPARQControl(PARQControl):
	def sets(self):
		self.relationship	= "Other"
		self.respondent		= "Parent"
		self.subject		= "Other"
		self.show_relationship_dropdown	= True

class ChildPARQControlFather(PARQControl):
	def sets(self):
		self.relationship	= "Father"
		self.respondent		= "Child"
		self.subject		= "Father"

class ChildPARQControlMother(PARQControl):
	def sets(self):
		self.relationship	= "Mother"
		self.respondent		= "Child"
		self.subject		= "Mother"

class ILARQControl(PARQControl):
	def sets(self):
		self.relationship	= "Other"
		self.respondent		= "Adult"
		self.subject		= "Other"

class MARQC(PARQControl):
	def sets(self):
		self.relationship	= "Other"
		self.respondent		= "Adult"
		self.subject		= "Other"

class OARQControl(PARQControl):
	def sets(self):
		self.relationship	= "Other"
		self.respondent		= "Adult"
		self.subject		= "Other"

class PARQControlInfant(TestBase):
	dimension1_name					= "Warmth/Affection"
	dimension2_name					= "Hostility/Aggression"
	dimension3_name					= "Indifference/Neglect"
	dimension4_name					= "Undifferentiated Rejection"
	dimension5_name					= "Control"
	max_unanswered_items			= 6
	dimension1_max_unanswered_items	= 3
	dimension2_max_unanswered_items	= 2
	dimension3_max_unanswered_items	= 2
	dimension4_max_unanswered_items	= 2
	dimension5_max_unanswered_items	= 1
	dimension5_is_control			= True

	def sets(self):
		self.relationship				= "Infant"
		self.respondent					= "Parent"
		self.subject					= "Infant"

	def get_scores_matrix(self):
		return [	[self.q1,	-1,			-1,			-1,			-1],
					[self.q2,	self.q3,	-1, 		-1,			-1],
					[self.q4,	self.q5,	self.q6,	self.q7,	self.q8],
					[self.q9,	self.q10,	self.q11,	self.q12,	-1],
					[self.q13,	self.q14,	self.q15,	self.q16,	self.q17],
					[self.q18,	self.q19,	self.q20,	self.q21,	-1],
					[self.q22,	self.q23,	self.q24,	self.q25,	self.q26],
					[self.q27,	self.q28,	self.q29,	self.q30,	self.q31],
					[self.q32,	self.q33,	self.q34,	self.q35,	-1],
					[self.q36,	self.q37,	self.q38,	self.q39,	self.q40],
					[self.q41,	self.q42,	self.q43,	self.q44,	self.q45],
					[self.q46,	self.q47,	self.q48,	self.q49,	-1],
					[self.q50,	self.q51,	self.q52,	-1,			self.q53],
					[self.q54,	self.q55,	self.q56,	-1,			self.q57],
					[self.q58,	self.q59,	self.q60,	-1,			-1],
					[self.q61,	self.q62,	-1,			-1,			-1],
					[self.q63,	-1,			-1,			-1,			-1]]

	def get_reverses_matrix(self):
		return [[1,	0,	0,	0,	0],
				[1,	0,	0, 	0,	0],
				[1,	0,	0, 	0,	0],
				[1,	0,	1, 	0,	0],
				[1,	0,	0, 	0,	0],
				[1,	0,	1, 	0,	0],
				[1,	0,	0, 	1,	0],
				[1,	0,	1, 	0,	1],
				[1,	0,	0, 	0,	0],
				[1,	0,	1, 	1, 	0],
				[1,	0,	0, 	0,	0],
				[1,	0,	1, 	0, 	0],
				[1,	0,	0, 	0, 	1],
				[1,	0,	1, 	0, 	0],
				[1,	0,	0,	0,	0],
				[1,	0,	0,	0,	0],
				[1,	0,	0,	0,	0]]

	def get_download_header(self):
		header = "id Relation Warmth Host indiff unrejn Control TotlPARQ "
		prefix = "??"
		suffix = ""
		question_count = 63

		prefix = "PPC"
		suffix = "I"

		for q in range(1, question_count + 1):
			header += " %s%d%s" % (prefix, q, suffix)

		return header

	def get_download_testname(self):
		return "PARENT (Mother/Father) PARQ/Control: Infant version"

	def get_download_line(self):
		line = "%s %s %d %d %d %d %d %d" % (self.test_id, self.respondent, self.dimension1_score, self.dimension2_score, self.dimension3_score, self.dimension4_score, self.dimension5_score, self.score)

		matrix	= self.get_scores_matrix()
		rows	= len(matrix)
		for row in range(0, rows):
			for col in range(0, 5):
				item_score = self.get_item_score(row, col, matrix, False)
				if item_score >= 0:
					line += " %d" % item_score

		line += "\n"
		return line

class PARQControlShort(TestBase):
	dimension1_name					= "Warmth/Affection"
	dimension2_name					= "Hostility/Aggression"
	dimension3_name					= "Indifference/Neglect"
	dimension4_name					= "Undifferentiated Rejection"
	dimension5_name					= "Control"
	max_unanswered_items			= 3
	dimension1_max_unanswered_items	= 1
	dimension2_max_unanswered_items	= 1
	dimension3_max_unanswered_items	= 1
	dimension4_max_unanswered_items	= 1
	dimension5_max_unanswered_items	= 1
	dimension5_is_control			= True

	def get_scores_matrix(self):
		return [	[self.q1,	-1,			self.q2,	-1,			self.q3],
					[self.q4,	self.q5, 	-1,			self.q6,	self.q7],
					[-1,		self.q8,	self.q9,	self.q10,	-1],
					[self.q11,	self.q12,	self.q13,	-1,			self.q14],
					[self.q15,	-1,			self.q16,	-1, 		-1],
					[-1,		self.q17,	self.q18,	self.q19,	self.q20],
					[self.q21,	self.q22,	-1,			-1,			-1],
					[self.q23,	self.q24,	-1,			self.q25,	self.q26],
					[self.q27,	-1,			self.q28,	-1, 		-1],
					[self.q29,	-1,			-1,			-1, 		-1]]

	def get_reverses_matrix(self):
		return [[1,	0,	0,	0,	0,	0,	0],
				[1,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[1,	0,	0, 	0,	0, 	0, 	0],
				[1,	0,	1, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	1, 	0, 	0],
				[1,	0,	0, 	0,	0, 	0, 	0],
				[1,	0,	0, 	0,	0, 	0, 	0],
				[1,	0,	0, 	0,	0, 	0, 	0],
				[1,	0,	0, 	0,	0, 	0, 	0]]

	def get_download_header(self):
		header = "id Warmth Host indiff unrejn Control TotlPARQ "
		prefix = "??"
		suffix = ""
		question_count = 29

		prefix = "PPC"
		suffix = "I"
		if self.respondent == "Adult":
			prefix = "APC"
		elif self.respondent == "Child":
			prefix = "CPC"
		elif self.respondent == "Parent":
			prefix = "PPC"
			suffix = "SF"
		elif self.respondent == "Teacher":
			prefix = "TPC"
			suffix = "SF"

		if self.subject == "Father":
			suffix = "FSF"
		elif self.subject == "Mother":
			suffix = "MSF"

		for q in range(1, question_count + 1):
			header += " %s%d%s" % (prefix, q, suffix)

		return header

	def get_download_testname(self):
		if self.test_name == TestBase.AdultPARQControlFatherShortName:
			return "Adult PARQ/Control: Father (Short Form)"
		elif self.test_name == TestBase.AdultPARQControlMotherShortName:
			return "Adult PARQ/Control: Mother (Short Form)"
		elif self.test_name == TestBase.ChildPARQControlFatherShortName:
			return "Child PARQ/Control: Father (Short Form)"
		elif self.test_name == TestBase.ChildPARQControlMotherShortName:
			return "Child PARQ/Control: Mother (Short Form)"
		elif self.test_name == TestBase.TeacherPARQControlShortName:
			return "Teacher PARQ/Control (Short Form)"
		elif self.test_name == TestBase.ParentPARQControlShortName:
			return "Parent PARQ/Control (Short Form)"

		return "Undefined"

	def get_download_line(self):
		line = "%s %d %d %d %d %d %d" % (self.test_id, self.as_number(self.dimension1_score), self.as_number(self.dimension2_score), self.as_number(self.dimension3_score), self.as_number(self.dimension4_score), self.as_number(self.dimension5_score), self.as_number(self.score))

		matrix	= self.get_scores_matrix()
		rows	= len(matrix)
		for row in range(0, rows):
			for col in range(0, 5):
				item_score = self.get_item_score(row, col, matrix, False)
				if item_score >= 0:
					line += " %d" % item_score

		line += "\n"
		return line

class SARQ(TestBase):
	dimension1_name					= "Warmth/Affection"
	dimension2_name					= "Hostility/Aggression"
	dimension3_name					= "Indifference/Neglect"
	dimension4_name					= "Undifferentiated Rejection"
	dimension5_name					= "Control"
	max_unanswered_items			= 3
	dimension1_max_unanswered_items	= 1
	dimension2_max_unanswered_items	= 1
	dimension3_max_unanswered_items	= 1
	dimension4_max_unanswered_items	= 1
	dimension5_max_unanswered_items	= 1
	dimension5_is_control			= True

	def sets(self):
		self.relationship	= "Other"
		self.respondent		= "Adult"
		self.subject		= "Other"

	def get_scores_matrix(self):
		return [	[self.q1,	-1,			self.q2,	-1,			self.q3],
					[self.q4,	self.q5, 	-1,			self.q6,	self.q7],
					[-1,		self.q8,	self.q9,	self.q10,	-1],
					[self.q11,	self.q12,	self.q13,	-1,			self.q14],
					[self.q15,	-1,			self.q16,	-1, 		-1],
					[-1,		self.q17,	self.q18,	self.q19,	self.q20],
					[self.q21,	self.q22,	-1,			-1,			-1],
					[self.q23,	self.q24,	-1,			self.q25,	self.q26],
					[self.q27,	-1,			self.q28,	-1, 		-1],
					[self.q29,	-1,			-1,			-1, 		-1]]

	def get_reverses_matrix(self):
		return [[1,	0,	0,	0,	0,	0,	0],
				[1,	0,	0, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	0, 	0, 	0],
				[1,	0,	0, 	0,	0, 	0, 	0],
				[1,	0,	1, 	0,	0, 	0, 	0],
				[0,	0,	0, 	0,	1, 	0, 	0],
				[1,	0,	0, 	0,	0, 	0, 	0],
				[1,	0,	0, 	0,	0, 	0, 	0],
				[1,	0,	0, 	0,	0, 	0, 	0],
				[1,	0,	0, 	0,	0, 	0, 	0]]

	def get_download_header(self):
		header = "id Warmth Host indiff unrejn Control TotlPARQ "
		prefix = "??"
		suffix = ""
		question_count = 29

		prefix = "PPC"
		suffix = "I"
		if self.respondent == "Adult":
			prefix = "APC"
		elif self.respondent == "Child":
			prefix = "CPC"
		elif self.respondent == "Parent":
			prefix = "PPC"
			suffix = "SF"
		elif self.respondent == "Teacher":
			prefix = "TPC"
			suffix = "SF"

		if self.subject == "Father":
			suffix = "FSF"
		elif self.subject == "Mother":
			suffix = "MSF"

		for q in range(1, question_count + 1):
			header += " %s%d%s" % (prefix, q, suffix)

		return header

	def get_download_testname(self):
		if self.test_name == TestBase.AdultPARQControlFatherShortName:
			return "Adult PARQ/Control: Father (Short Form)"
		elif self.test_name == TestBase.AdultPARQControlMotherShortName:
			return "Adult PARQ/Control: Mother (Short Form)"
		elif self.test_name == TestBase.ChildPARQControlFatherShortName:
			return "Child PARQ/Control: Father (Short Form)"
		elif self.test_name == TestBase.ChildPARQControlMotherShortName:
			return "Child PARQ/Control: Mother (Short Form)"
		elif self.test_name == TestBase.TeacherPARQControlShortName:
			return "Teacher PARQ/Control (Short Form)"
		elif self.test_name == TestBase.ParentPARQControlShortName:
			return "Parent PARQ/Control (Short Form)"

		return "Undefined"

	def get_download_line(self):
		line = "%s %d %d %d %d %d %d" % (self.test_id, self.as_number(self.dimension1_score), self.as_number(self.dimension2_score), self.as_number(self.dimension3_score), self.as_number(self.dimension4_score), self.as_number(self.dimension5_score), self.as_number(self.score))

		matrix	= self.get_scores_matrix()
		rows	= len(matrix)
		for row in range(0, rows):
			for col in range(0, 5):
				item_score = self.get_item_score(row, col, matrix, False)
				if item_score >= 0:
					line += " %d" % item_score

		line += "\n"
		return line

class AdultPARQControlFatherShort(PARQControlShort):
	def sets(self):
		self.relationship	= "Father"
		self.respondent		= "Adult"
		self.subject		= "Father"

class AdultPARQControlMotherShort(PARQControlShort):
	def sets(self):
		self.relationship	= "Mother"
		self.respondent		= "Adult"
		self.subject		= "Mother"

class AdultPARQControlFatherInLawShort(PARQControlShort):
	def sets(self):
		self.relationship	= "Father-in-Law"
		self.respondent		= "Adult"
		self.subject		= "Father"

class AdultPARQControlMotherInLawShort(PARQControlShort):
	def sets(self):
		self.relationship	= "Mother-in-Law"
		self.respondent		= "Adult"
		self.subject		= "Mother"

class ParentPARQControlShort(PARQControlShort):
	def sets(self):
		self.relationship	= "Other"
		self.respondent		= "Parent"
		self.subject		= "Other"
		self.show_relationship_dropdown	= True

class ChildPARQControlFatherShort(PARQControlShort):
	def sets(self):
		self.relationship	= "Father"
		self.respondent		= "Child"
		self.subject		= "Father"

class ChildPARQControlMotherShort(PARQControlShort):
	def sets(self):
		self.relationship	= "Mother"
		self.respondent		= "Child"
		self.subject		= "Mother"

class TeacherPARQControlShort(PARQControlShort):
	def sets(self):
		self.relationship	= "Other"
		self.respondent		= "Teacher"
		self.subject		= "Other"

class OARQControlShort(PARQControlShort):
	def sets(self):
		self.relationship	= "Other"
		self.respondent		= "Adult"
		self.subject		= "Other"

class PARQ(TestBase):
	dimension1_name					= "Warmth/Affection"
	dimension2_name					= "Hostility/Aggression"
	dimension3_name					= "Indifference/Neglect"
	dimension4_name					= "Undifferentiated Rejection"
	max_unanswered_items			= 3
	dimension1_max_unanswered_items	= 1
	dimension2_max_unanswered_items	= 1
	dimension3_max_unanswered_items	= 1
	dimension4_max_unanswered_items	= 1
	dimension5_max_unanswered_items	= 1

	def get_scores_matrix(self):
		return [[self.q1,	self.q2,	self.q3, 	self.q4],
				[self.q5, 	self.q6,	self.q7,	-1],
				[self.q8,	self.q9,	self.q10,	self.q11],
				[self.q12,	self.q13,	self.q14,	-1],
				[self.q15,	self.q16,	self.q17,	self.q18],
				[self.q19,	self.q20,	self.q21,	-1],
				[self.q22,	self.q23,	self.q24,	self.q25],
				[self.q26,	self.q27,	self.q28,	-1],
				[self.q29,	self.q30,	self.q31,	self.q32],
				[self.q33,	self.q34,	self.q35,	-1],
				[self.q36,	self.q37,	self.q38,	self.q39],
				[self.q40,	self.q41,	self.q42,	-1],
				[self.q43,	self.q44,	self.q45,	self.q46],
				[self.q47,	self.q48,	self.q49,	-1],
				[self.q50,	self.q51,	self.q52,	self.q53],
				[self.q54,	-1,			-1,			-1],
				[self.q55,	-1,			-1,			self.q56],
				[self.q57,	-1,			-1,			-1],
				[self.q58,	-1,			-1,			self.q59],
				[self.q60,	-1,			-1,			-1]]

	def get_reverses_matrix(self):
		return [[1,	0,	0,	0],		#q1
				[1,	0,	1, 	0],		#q5
				[1,	0,	0, 	0],		#q8
				[1,	0,	1, 	0],		#q12
				[1,	0,	0, 	0],		#q15
				[1,	0,	1, 	0],		#q19
				[1,	0,	0, 	0],		#q22
				[1,	0,	1, 	0],		#q26
				[1,	0,	0, 	0],		#q29
				[1,	0,	1, 	0],		#q33
				[1,	0,	0, 	0],		#q36
				[1,	0,	1, 	0],		#q40
				[1,	0,	0, 	0],		#q43
				[1,	0,	1, 	0],		#q47
				[1,	0,	0, 	0],		#q50
				[1,	0,	0, 	0],		#q54
				[1,	0,	0, 	0],		#q55
				[1,	0,	0, 	0],		#q57
				[1,	0,	0, 	0],		#q58
				[1,	0,	0, 	0]]

	def get_download_header(self):
		header = "id Warmth Host indiff unrejn TotlPARQ "
		prefix = "??"
		suffix = ""
		question_count = 60

		if self.respondent == "Adult":
			prefix = "AP"
		elif self.respondent == "Child":
			prefix = "CP"
		elif self.respondent == "Parent":
			prefix = "PP"

		if self.subject == "Father":
			suffix = "F"
		elif self.subject == "Mother":
			suffix = "M"

		for q in range(1, question_count + 1):
			header += " %s%d%s" % (prefix, q, suffix)

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		if self.subject == "Other":
			relationship = self.relationship
		else:
			relationship = ""

		line = "%s %s %d %d %d %d %d" % (self.test_id, relationship, self.as_number(self.dimension1_score), self.as_number(self.dimension2_score), self.as_number(self.dimension3_score), self.as_number(self.dimension4_score), self.as_number(self.score))

		matrix	= self.get_scores_matrix()
		rows	= len(matrix)
		for row in range(0, rows):
			for col in range(0, 4):
				item_score = self.get_item_score(row, col, matrix, False)
				if item_score >= 0:
					line += " %d" % item_score

		line += "\n"
		return line

class ChildPARQFather(PARQ):
	def sets(self):
		self.relationship	= "Father"
		self.respondent		= "Child"
		self.subject		= "Father"

class ChildPARQMother(PARQ):
	def sets(self):
		self.relationship	= "Mother"
		self.respondent		= "Child"
		self.subject		= "Mother"

class AdultPARQFather(PARQ):
	def sets(self):
		self.relationship	= "Father"
		self.respondent		= "Adult"
		self.subject		= "Father"

class AdultPARQMother(PARQ):
	def sets(self):
		self.relationship	= "Mother"
		self.respondent		= "Adult"
		self.subject		= "Mother"

class ParentPARQ(PARQ):
	def sets(self):
		self.relationship	= "Other"
		self.respondent		= "Adult"
		self.subject		= "Other"
		self.show_relationship_dropdown	= True

class OARQ(PARQ):
	def sets(self):
		self.relationship	= "Other"
		self.respondent		= "Adult"
		self.subject		= "Other"

class PARQShort(TestBase):
	dimension1_name					= "Warmth/Affection"
	dimension2_name					= "Hostility/Aggression"
	dimension3_name					= "Indifference/Neglect"
	dimension4_name					= "Undifferentiated Rejection"
	max_unanswered_items			= 2
	dimension1_max_unanswered_items	= 1
	dimension2_max_unanswered_items	= 1
	dimension3_max_unanswered_items	= 1
	dimension4_max_unanswered_items	= 1
	dimension5_max_unanswered_items	= 1

	def get_scores_matrix(self):
		return [[self.q1,	-1,			self.q2,	-1],
				[self.q3, 	self.q4, 	-1,			self.q5],
				[-1,		self.q6,	self.q7,	self.q8],
				[self.q9,	self.q10,	self.q11,	-1],
				[self.q12,	-1,			self.q13,	-1],
				[-1,		self.q14,	self.q15,	self.q16],
				[self.q17,	self.q18,	-1,			-1],
				[self.q19,	self.q20,	-1,			self.q21],
				[self.q22,	-1,			self.q23,	-1],
				[self.q24,	-1,			-1,			-1]]

	def get_reverses_matrix(self):
		return [[1,	0,	0,	0],		#q1
				[1,	0,	0, 	0],		#q3
				[1,	0,	0, 	0],		#
				[1,	0,	0, 	0],		#q9
				[1,	0,	1, 	0],		#q12
				[1,	0,	0, 	0],		#
				[1,	0,	0, 	0],		#q17
				[1,	0,	0, 	0],		#q19
				[1,	0,	0, 	0],		#q22
				[1,	0,	0, 	0]]

	def get_download_header(self):
		header = "id Warmth Host indiff unrejn TotlPARQ "
		prefix = "??"
		suffix = ""
		question_count = 24

		if self.respondent == "Adult":
			prefix = "AP"
		elif self.respondent == "Child":
			prefix = "CP"
		elif self.respondent == "Parent":
			prefix = "PP"

		if self.subject == "Father":
			suffix = "FSF"
		elif self.subject == "Mother":
			suffix = "MSF"
		else:
			suffix = "SF"

		for q in range(1, question_count + 1):
			header += " %s%d%s" % (prefix, q, suffix)

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		if self.subject == "Other":
			relationship = self.relationship
		else:
			relationship = ""

		line = "%s %s %s %s %s %s %s" % (self.test_id, relationship, self.as_number(self.dimension1_score), self.as_number(self.dimension2_score), self.as_number(self.dimension3_score), self.as_number(self.dimension4_score), self.as_number(self.score))

		matrix	= self.get_scores_matrix()
		rows	= len(matrix)
		for row in range(0, rows):
			for col in range(0, 4):
				item_score = self.get_item_score(row, col, matrix, False)
				if item_score >= 0:
					line += " %d" % item_score

		line += "\n"
		return line

class ChildPARQFatherShort(PARQShort):
	def sets(self):
		self.relationship	= "Father"
		self.respondent		= "Child"
		self.subject		= "Father"

class ChildPARQMotherShort(PARQShort):
	def sets(self):
		self.relationship	= "Mother"
		self.respondent		= "Child"
		self.subject		= "Mother"

class AdultPARQFatherShort(PARQShort):
	def sets(self):
		self.relationship	= "Father"
		self.respondent		= "Adult"
		self.subject		= "Father"

class AdultPARQMotherShort(PARQShort):
	def sets(self):
		self.relationship	= "Mother"
		self.respondent		= "Child"
		self.subject		= "Mother"

class ParentPARQShort(PARQShort):
	def sets(self):
		self.relationship	= "Other"
		self.respondent		= "Parent"
		self.subject		= "Other"
		self.show_relationship_dropdown	= True

class EarlyChildhoodBFARQShort(PARQShort):
	def sets(self):
		self.relationship	= "Mother"
		self.respondent		= "Child"
		self.subject		= "Mother"

class ECARQShortFather(PARQShort):
	def sets(self):
		self.relationship	= "Father"
		self.respondent		= "Child"
		self.subject		= "Mother"

class ECARQShortMother(PARQShort):
	def sets(self):
		self.relationship	= "Mother"
		self.respondent		= "Child"
		self.subject		= "Mother"

class OARQShort(PARQShort):
	def sets(self):
		self.relationship	= "Other"
		self.respondent		= "Adult"
		self.subject		= "Other"

class PAQ(TestBase):
	dimension1_name					= "Hostility/Aggression"
	dimension2_name					= "Dependency"
	dimension3_name					= "Negative Self-Esteem"
	dimension4_name					= "Negative Self-Adequacy"
	dimension5_name					= "Emotional Unresponsive"
	dimension6_name					= "Emotional Instability"
	dimension7_name					= "Negative Worldview"
	max_unanswered_items			= 4
	dimension1_max_unanswered_items	= 1
	dimension2_max_unanswered_items	= 1
	dimension3_max_unanswered_items	= 1
	dimension4_max_unanswered_items	= 1
	dimension5_max_unanswered_items	= 1
	dimension6_max_unanswered_items	= 1
	dimension7_max_unanswered_items	= 1

	def get_download_header(self):
		header = "id aggr depen esteem adeq respons stab WV TotalPAQ"
		for q in range(1, 43):
			header += " P%dC" % q

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		line = "%s %d %d %d %d %d %d %d %d" % (self.test_id, self.as_number(self.dimension1_score), self.as_number(self.dimension2_score), self.as_number(self.dimension3_score), self.as_number(self.dimension4_score), self.as_number(self.dimension5_score), self.as_number(self.dimension6_score), self.as_number(self.dimension7_score), self.as_number(self.score))

		matrix	= self.get_scores_matrix()
		rows	= len(matrix)
		for row in range(0, rows):
			for col in range(0, 7):
				line += " %d" % self.get_item_score(row, col, matrix, False)

		line += "\n"
		return line

class ChildPAQ(PAQ):
	def sets(self):
		self.relationship				= None
		self.respondent					= "Child"
		self.subject					= None

	def get_scores_matrix(self):
		return [[self.q1,	self.q2,	self.q3,	self.q4,	self.q5,	self.q6,	self.q7],
				[self.q8,	self.q9,	self.q10,	self.q11,	self.q12,	self.q13,	self.q14],
				[self.q15,	self.q16,	self.q17,	self.q18,	self.q19,	self.q20,	self.q21],
				[self.q22,	self.q23,	self.q24,	self.q25,	self.q26,	self.q27,	self.q28],
				[self.q29,	self.q30,	self.q31,	self.q32,	self.q33,	self.q34,	self.q35],
				[self.q36,	self.q37,	self.q38,	self.q39,	self.q40,	self.q41,	self.q42]]

	def get_reverses_matrix(self):
		return [[0,	0,	1,	1,	0,	0,	1],
				[0,	0,	0,	0,	1,	0,	0],
				[0,	1,	0,	1,	0,	0,	1],
				[0,	0,	1,	0,	1,	0,	0],
				[0,	0,	1,	0,	0,	1,	0],
				[0,	0,	0,	1,	1,	0,	1]]

class AdultPAQ(PAQ):
	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None

	def get_scores_matrix(self):
		return [[self.q1,	self.q2,	self.q3,	self.q4,	self.q5,	self.q6,	self.q7],
				[self.q8,	self.q9,	self.q10,	self.q11,	self.q12,	self.q13,	self.q14],
				[self.q15,	self.q16,	self.q17,	self.q18,	self.q19,	self.q20,	self.q21],
				[self.q22,	self.q23,	self.q24,	self.q25,	self.q26,	self.q27,	self.q28],
				[self.q29,	self.q30,	self.q31,	self.q32,	self.q33,	self.q34,	self.q35],
				[self.q36,	self.q37,	self.q38,	self.q39,	self.q40,	self.q41,	self.q42],
				[self.q43,	self.q44,	self.q45,	self.q46,	self.q47,	self.q48,	self.q49],
				[self.q50,	self.q51,	self.q52,	self.q53,	self.q54,	self.q55,	self.q56],
				[self.q57,	self.q58,	self.q59,	self.q60,	self.q61,	self.q62,	self.q63],
				]

	def get_reverses_matrix(self):
		return [[0,	0,	0,	0,	0,	0,	0],
				[0,	0,	1,	1,	0,	0,	1],
				[0,	1,	0,	0,	1,	1,	0],
				[0,	0,	1,	1,	0,	0,	1],
				[0,	0,	0,	0,	1,	0,	0],
				[0,	0,	1,	1,	0,	1,	1],
				[0,	1,	0,	0,	0,	0,	0],
				[0,	0,	0,	1,	1,	0,	1],
				[0,	0,	0,	0,	0,	1,	1]]

class IPARCQ(PARQControl):
	dimension5_is_control	= True
	relation				= db.StringProperty()
	current					= db.StringProperty()
	years					= db.StringProperty()
	months					= db.StringProperty()
	nature					= db.StringProperty()
	secure					= db.StringProperty()

	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None

	def store_form(self, request):
		TestBase.store_form(self, request)
		self.relation   	= request.get("relation")
		self.current		= request.get("current")
		self.years	    	= request.get("years")
		self.months	    	= request.get("months")
		self.nature	    	= request.get("nature")
		self.secure	    	= request.get("secure")

	def test_as_html_table(self, can_edit_test):
		h = "<tr><td colspan=21>"
		h += "<table border=0 width=""100%"">"
		h += "<tr>"
		h += "<th colspan=3>Relation</th>"
		h += "<th colspan=3>Current</th>"
		h += "<th colspan=3>Years / Months</th>"
		h += "<th colspan=3>Nature</th>"
		h += "<th colspan=3>Secure</th>"
		h += "</tr>"
		h += "<tr>"
		h += """<td colspan=3><input type="text" name="relation" value="%s"></td>""" % (self.relation	if self.relation != None else " ")
		h += """<td colspan=3><input type="text" name="current" value="%s"></td>""" % (self.current	if self.current  != None else " ")
		h += """<td colspan=3 nowrap><input type="text" name="years" value="%s" size=4> / """ % (self.years	if self.years	 != None else " ")
		h += """<input type=""text"" name="months" value="%s" size=4></td>""" % (self.months	if self.months	 != None else " ")
		h += """<td colspan=3><input type="text" name="nature" value="%s"></td>""" % (self.nature	if self.nature	 != None else " ")
		h += """<td colspan=3><input type="text" name="secure" value="%s"></td>""" % (self.secure	if self.secure	 != None else " ")
		h += "</tr>"
		h += "</table>"
		h += "</td></tr>"
		h += TestBase.test_as_html_table(self, can_edit_test)
		return h

	def get_download_header(self):
		header = "id Warmth Host indiff unrejn Control TotlPARQ Relation Current Length Nature Secure"
		for q in range(1, 73):
			header += " IPC%d" % q

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		line = "%s %s %s %s %s %s" % (self.test_id, self.dimension1_score, self.dimension2_score, self.dimension3_score, self.dimension4_score, self.dimension5_score)
		line += " %s" % self.relation
		line += " %s" % self.current

		age_in_months = 0
		try:
			age_in_months = int(self.years) * 12
		except:
			age_in_months = 0

		try:
			age_in_months += int(self.months)
		except:
			age_in_months = age_in_months

		line += " %i" % age_in_months
		line += " %s" % self.nature
		line += " %s" % self.secure

		matrix	= self.get_scores_matrix()
		rows	= len(matrix)
		for row in range(0, rows):
			for col in range(0, 5):
				item_score = self.get_item_score(row, col, matrix, False)
				if item_score >= 0:
					line += " %d" % item_score

		line += "\n"
		return line

class IPAQ(TestBase):
	longevity = db.IntegerProperty()

	question_labels = [["Intimate", "INTIMATE"],
						["Ongoing", "ONGOING"],
						["Longevity", "LONG"],
						["Form", "FORM"],
						["Unique", "UNIQUE"],
						["Proximity", "PROXIMITY"],
						["Distress", "DISTRESS"],
						["Joy", "JOY"],
						["Security", "SECURE"],
						["Close", "CLOSE"],
						["Anxious", "ANXIOUS"],
						["Ambivalent", "AMBIV"],
						["Avoidant", "AVOID"],
						["Well-Being", "WELL"],
						["Sad", "SAD"]]


	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None

	def test_as_html_table(self, can_edit_test):
		q_values = [self.q1, self.q2, self.q3, self.q4, self.q5, self.q6, self.q7, self.q8, self.q9, self.q10, self.q11, self.q12, self.q13, self.q14, self.q15]
		h = "<tr><td colspan=10>"
		h += "<table border=0>"
		for row in range(0, len(q_values)):
			h += "<tr>"
			h += """<td>%d.</td><td>%s</td>""" % (row + 1, self.question_labels[row][0])
			if row == 2:
				months	= self.longevity
				years	= (self.longevity / 12) if self.longevity != None else 0
				months	= (self.longevity % 12) if self.longevity != None else 0
				h += "<td>"
				h += """<input type="text" size="4" name="long_yr" value="%s">""" % (years)
				h += " / "
				h += """<input type="text" size="4" name="long_mo" value="%s">""" % (months)
				h += "</td>"
			else:
				h += """<td><input type="text" size="4" name="q%d" value="%s"></td> """ % (row+1, (q_values[row] if q_values[row] != None else ""))
			h += "</tr>"

		h += "</table>"
		h += "</td></tr>"
		return h

	def store_form(self, request):
		TestBase.store_form(self, request)
		self.longevity = int(request.get("long_yr")) * 12 + int(request.get("long_mo"))

	def get_download_header(self):
		header = "id INTIMATE ONGOING LONG FORM UNIQUE PROXMITY DISTRESS JOY SECURE CLOSE ANXIOUS AMBIV AVOID WELL SAD"
		#for q in range(1, 73):
		#	header += " IPC%d" % q

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		line = "%s" % (self.test_id)
		line += " %s" % self.longevity

		matrix	= self.get_scores_matrix()
		rows	= len(matrix)
		line += " %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s\n" % (self.q1, self.q2, self.q3, self.q4, self.q5, self.q6, self.q7, self.q8, self.q9, self.q10, self.q11, self.q12, self.q13, self.q14, self.q15)
		return line


class TESC(TestBase):
	dimension1_name					= "Warmth/Affection"
	dimension2_name					= "Hostility/Aggression"
	dimension3_name					= "Indifference/Neglect"
	max_unanswered_items			= 2
	dimension1_max_unanswered_items	= 1
	dimension2_max_unanswered_items	= 1
	dimension3_max_unanswered_items	= 1

	grade			= db.StringProperty()
	age				= db.StringProperty()
	gender			= db.StringProperty()
	teacher_name	= db.StringProperty()
	school			= db.StringProperty()

	def sets(self):
		self.relationship				= None
		self.respondent					= "Teacher"
		self.subject					= None

	def get_scores_matrix(self):
		return [[self.q1,	self.q2,	self.q3],
				[self.q4, 	self.q5,	self.q6],
				[self.q7,	self.q8,	self.q9],
				[self.q10,	self.q11,	self.q12],
				[self.q13,	self.q14,	self.q15],
				[self.q16,	self.q17,	self.q18]]

	def get_reverses_matrix(self):
		return [[0,	0,	0],
				[0,	0,	0],
				[0,	0,	0],
				[0,	0,	0],
				[0,	0,	0],
				[0,	0,	0]]

	def store_form(self, request):
		TestBase.store_form(self, request)
		self.grade		       	= request.get("grade")
		self.age			   	= request.get("age")
		self.gender		       	= request.get("gender")
		self.teacher_name      	= request.get("teacher_name")
		self.school		       	= request.get("school")

	def test_as_html_table(self, can_edit_test):
		h = "<tr><td colspan=21>"
		h += "<table border=0 width=""100%"">"

		h += "<tr>"
		h += """<td>Grade</td><td><input type=text name="grade" value="%s"</td>""" % (self.grade if self.grade != None else "")
		h += """<td>Age</td><td><input type=text name="age" value="%s"</td>""" % (self.age if self.age != None else "")
		h += """<td>Gender</td><td><input type=text name="gender" value="%s"</td>""" % (self.gender if self.gender != None else "")
		h += "</tr>"

		h += "<tr>"
		h += """<td>Teacher's Name</td><td><input type=text name="teacher_name" value="%s"</td>""" % (self.teacher_name if self.teacher_name != None else "")
		h += """<td>School</td><td><input type=text name="school" value="%s"</td>""" % (self.school if self.school != None else "")
		h += "</tr>"

		h += "</table>"
		h += "</td></tr>"
		h += TestBase.test_as_html_table(self, can_edit_test)
		return h

	def get_download_header(self):
		header = "id TOTTESC GRADE AGE GENDER TCHNAME SCHOOL TESC1 TESC2 TESC3 TESC4 TESC5 TESC6 TESC7 TESC8 TESC9 TESC10 TESC11 TESC12 TESC13 TESC14 TESC15 TESC16 TESC17 TESC18"

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		line = "%s" % (self.test_id)
		#line += " %s" % self.longevity

		matrix	= self.get_scores_matrix()
		rows	= len(matrix)
		line += " %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s\n" % (self.q1, self.q2, self.q3, self.q4, self.q5, self.q6, self.q7, self.q8, self.q9, self.q10, self.q11, self.q12, self.q13, self.q14, self.q15)
		return line

class PPQ(TestBase):
	max_unanswered_items	= 6
	sum_punishment_score	= db.IntegerProperty()
	harsh_score				= db.IntegerProperty()
	just_score				= db.IntegerProperty()
	item_validation_function		= "checkPPQEnteredValue"
	form_validation_function		= "validatePPQForm"

	question_labels = ["NEVER",
						"FREQ",
						"SEVER",
						"CONSIS",
						"PREDIC",
						"INCID",
						"FAIR",
						"DESERV",
						"TIMING",
						"EXPL",
						"SPANK",
						"SLAP",
						"SHOVE",
						"YANK",
						"KICK",
						"BEAT",
						"HIT",
						"HAIR",
						"EAR",
						"KNEEL",
						"STAND",
						"PINCH",
						"SHAKE",
						"OTH1",
						"OTH2",
						"OTH3",
						"OTH4"]

	def get_scores_matrix(self):
		return [	[self.q1,	self.q7,	self.q13,	self.q18,	self.q23],
					[self.q2,	self.q8, 	self.q14,	self.q19,	self.q24],
					[self.q3,	self.q9, 	self.q15,	self.q20,	self.q25],
					[self.q4,	self.q10, 	self.q16,	self.q21,	self.q26],
					[self.q5,	self.q11, 	self.q17,	self.q22,	self.q27],
					[self.q6,	self.q12, 	-1,			-1,			-1]]

	def get_reverses_matrix(self):
		return [[0,	0,	0,	0,	0],
				[0,	0,	0, 	0,	0],
				[0,	0,	0, 	0,	0],
				[0,	0,	0, 	0,	0],
				[0,	0,	0, 	0,	0],
				[0,	0,	0, 	0,	0]]

	def test_as_html_table(self, can_edit_test):
		q_values = [self.q1, self.q2, self.q3, self.q4, self.q5, self.q6, self.q7, self.q8, self.q9, self.q10, self.q11, self.q12, self.q13, self.q14, self.q15, self.q16, self.q17, self.q18, self.q19, self.q20, self.q21, self.q22, self.q23, self.q24, self.q25, self.q26, self.q27]
		if self.respondent == "Youth":
			prefix = "Y"
		elif self.respondent == "Adult":
			prefix = "A"
		elif self.respondent == "Parent":
			prefix = "P"
		else:
			prefix = self.respondent

		if self.subject == "Mother":
			suffix = "M"
		elif self.subject == "Father":
			suffix = "F"
		else:
			suffix = ""

		h = "<tr><td colspan=10>"
		h += "<table border=0>"
		h += "<tr>"
		h += """<td>1.</td><td>%s%s%s</td>""" % (prefix, self.question_labels[0], suffix)
		h += """<td><input type="checkbox" name="q1" id="q1" %s onChange="togglePPQNever();"></td>""" % ("checked" if self.q1 == "1" else "")
		h += "</tr>"
		for row in range(1, len(q_values)):
			h += "<tr>"
			h += """<td>%d.</td><td>%s%s%s</td>""" % (row + 1, prefix, self.question_labels[row], suffix)
			h += """<td><input type="text" size="4" name="q%d" id="q%d" value="%s" onblur="%s(this, %d)"></td> """ % (row+1, row+1, (q_values[row] if q_values[row] != None else ""), self.item_validation_function, row + 1)
			h += "</tr>"
		h += "</table>"
		h += "</td></tr>"
		return h

	def get_score(self):
		self.harsh_score			= int(self.q2) + int(self.q3)
		self.just_score				= int(self.q7) + int(self.q8)
		self.sum_punishment_score	= int(self.q11) + int(self.q12)
		scores = self.get_scores_matrix()
		for col in range(2, 5):
			for row in range(0, 5):
				self.sum_punishment_score	+= int(scores[row][col])
		self.score	= self.sum_punishment_score

	def get_download_header(self):
		if self.respondent == "Adult":
			prefix = "A"
		elif self.respondent == "Youth":
			prefix = "Y"
		elif self.respondent == "Parent":
			prefix = "P"

		suffix = ""
		if self.subject == "Father":
			suffix = "F"
		elif self.subject == "Mother":
			suffix = "M"

		header = "id"
		header += " %sSUMPUN%s %sHARSH%s %sJUST%s" % (prefix, suffix, prefix, suffix, prefix, suffix)

		for q in range(0, len(self.question_labels)):
			header += " %s%s%s" % (prefix, self.question_labels[q], suffix)

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		if self.subject == "Other":
			relationship = self.relationship
		else:
			relationship = ""

		sum_punishment_score 	= self.sum_punishment_score
		harsh_score				= self.harsh_score
		just_score				= self.just_score

		if sum_punishment_score == None:
			sum_punishment_score = 0

		if harsh_score == None:
			harsh_score = 0

		if just_score == None:
			just_score = 0

		line = "%s %d %d %d" % (self.test_id, sum_punishment_score, harsh_score, just_score)

		matrix	= self.get_scores_matrix()
		rows	= len(matrix)
		for row in range(0, rows):
			for col in range(0, 5):
				item_score = self.get_item_score(row, col, matrix, False)
				if item_score == None:
					item_score = 0
				if item_score >= 0:
					line += " %d" % item_score

		line += "\n"
		return line

class YouthPPQMother(PPQ):
	def sets(self):
		self.relationship	= "Mother"
		self.respondent		= "Youth"
		self.subject		= "Mother"

class YouthPPQFather(PPQ):
	def sets(self):
		self.relationship	= "Father"
		self.respondent		= "Youth"
		self.subject		= "Father"

class AdultPPQMother(PPQ):
	def sets(self):
		self.relationship	= "Mother"
		self.respondent		= "Adult"
		self.subject		= "Mother"

class AdultPPQFather(PPQ):
	def sets(self):
		self.relationship	= "Father"
		self.respondent		= "Adult"
		self.subject		= "Father"

class ParentPPQ(TestBase):
	max_unanswered_items	= 6
	sum_punishment_score	= db.IntegerProperty()
	harsh_score				= db.IntegerProperty()
	just_score				= db.IntegerProperty()
	item_validation_function		= "checkParentPPQEnteredValue"
	form_validation_function		= "validateParentPPQForm"

	def sets(self):
		self.relationship	= "Other"
		self.respondent		= "Adult"
		self.subject		= "Other"

	question_labels = ["CHILD",
						"AGE",
						"GENDER",
						"PARENT",
						"NEVER",
						"FREQ",
						"SEVER",
						"CONSIS",
						"PREDIC",
						"INCID",
						"FAIR",
						"DESERV",
						"TIMING",
						"EXPL",
						"SPANK",
						"SLAP",
						"SHOVE",
						"YANK",
						"KICK",
						"BEAT",
						"HIT",
						"HAIR",
						"EAR",
						"KNEEL",
						"STAND",
						"PINCH",
						"SHAKE",
						"OTH1",
						"OTH2",
						"OTH3",
						"OTH4"]

	def get_scores_matrix(self):
		return [	[self.q1,	self.q7,	self.q13,	self.q20,	self.q26],
					[self.q2,	self.q8, 	self.q14,	self.q21,	self.q27],
					[self.q3,	self.q9, 	self.q15,	self.q22,	self.q28],
					[self.q4,	self.q10, 	self.q16,	self.q23,	self.q29],
					[self.q5,	self.q11, 	self.q17,	self.q24,	self.q30],
					[self.q6,	self.q12, 	self.q18,	self.q25,	self.q31],
					[-1,		-1, 		self.q19,	-1,			-1],
					]

	def get_reverses_matrix(self):
		return [[0,	0,	0,	0,	0],
				[0,	0,	0, 	0,	0],
				[0,	0,	0, 	0,	0],
				[0,	0,	0, 	0,	0],
				[0,	0,	0, 	0,	0],
				[0,	0,	0, 	0,	0]]

	def test_as_html_table(self, can_edit_test):
		q_values = [self.q1, self.q2, self.q3, self.q4, self.q5, self.q6, self.q7, self.q8, self.q9, self.q10, self.q11, self.q12, self.q13, self.q14, self.q15, self.q16, self.q17, self.q18, self.q19, self.q20, self.q21, self.q22, self.q23, self.q24, self.q25, self.q26, self.q27, self.q28, self.q29, self.q30, self.q31]
		prefix = "P"
		suffix = ""

		h = "<tr><td colspan=10>"
		h += "<table border=0>"

		h += "<tr>"
		h += """<td>1.</td><td>%s%s%s</td>""" % (prefix, self.question_labels[0], suffix)
		h += """<td><input type="text" name="q1" id="q1" size="8" value="%s"></td> """ % (self.q1 if self.q1 != None else "")
		h += "</tr>"

		h += "<tr>"
		h += """<td>2.</td><td>%s%s%s</td>""" % (prefix, self.question_labels[1], suffix)
		h += """<td><input type="text" name="q2" id="q2" size="8" value="%s"></td> """ % (self.q2 if self.q2 != None else "")
		h += "</tr>"

		h += "<tr>"
		h += """<td>3.</td><td>%s%s%s</td>""" % (prefix, self.question_labels[2], suffix)
		h += """<td><input type="text" name="q3" id="q3" size="8" value="%s"></td> """ % (self.q3 if self.q3 != None else "")
		h += "</tr>"

		h += "<tr>"
		h += """<td>4.</td><td>%s%s%s</td>""" % (prefix, self.question_labels[3], suffix)
		h += """<td><input type="text" name="q4" id="q4" size="8" value="%s"></td> """ % (self.q4 if self.q4 != None else "")
		h += "</tr>"

		h += "<tr>"
		h += """<td>5.</td><td>%s%s%s</td>""" % (prefix, self.question_labels[4], suffix)
		h += """<td><input type="checkbox" name="q5" id="q5" %s onChange="toggleParentPPQNever();"></td>""" % ("checked" if self.q5 == "1" else "")
		h += "</tr>"

		for row in range(5, len(q_values)):
			h += "<tr>"
			h += """<td>%d.</td><td>%s%s%s</td>""" % (row + 1, prefix, self.question_labels[row], suffix)
			h += """<td><input type="text" size="4" name="q%d" id="q%d" value="%s" onblur="%s(this, %d)"></td> """ % (row+1, row+1, (q_values[row] if q_values[row] != None else ""), self.item_validation_function, row + 1)
			h += "</tr>"
		h += "</table>"
		h += "</td></tr>"
		return h

	def get_score(self):
		self.harsh_score			= int(self.q6) + int(self.q7)
		self.just_score				= int(self.q11) + int(self.q12)
		self.sum_punishment_score	= int(self.q15) + int(self.q16) + int(self.q17) + int(self.q18) + int(self.q19)
		scores = self.get_scores_matrix()
		for col in range(3, 5):
			for row in range(0, 6):
				if int(scores[row][col]) > 0:
					self.sum_punishment_score	+= int(scores[row][col])
		self.score	= self.sum_punishment_score

	def get_download_header(self):
		header = "id PSUMPUN PHARST PJUST CHILD AGE GENDER PARENT PNEVER PFREQ PSEVER PCONSIS PPREDIC PINCID PFAIR PDESERV PTIMING PEXPL PSPANK PSLAP PSHOVE PYANK PKICK PBEAT PHIT PHAIR PEAR PKNEEL PSTAND PPINCH PSHAKE POTH1 POTH2 POTH3 POTH4"
		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):

		sum_punishment_score 	= self.sum_punishment_score
		harsh_score				= self.harsh_score
		just_score				= self.just_score

		if sum_punishment_score == None:
			sum_punishment_score = 0

		if harsh_score == None:
			harsh_score = 0

		if just_score == None:
			just_score = 0

		line = "%s %d %d %d" % (self.test_id, sum_punishment_score, harsh_score, just_score)

		matrix	= self.get_scores_matrix()
		rows	= len(matrix)
		q_values = [self.q1, self.q2, self.q3, self.q4, self.q5, self.q6, self.q7, self.q8, self.q9, self.q10, self.q11, self.q12, self.q13, self.q14, self.q15, self.q16, self.q17, self.q18, self.q19, self.q20, self.q21, self.q22, self.q23, self.q24, self.q25, self.q26, self.q27, self.q28, self.q29, self.q30, self.q31]

		for q in range(0, len(q_values)):
			item_score = q_values[q]
			if item_score == None:
				item_score = 0
			if item_score >= 0:
				line += " %s" % item_score

		line += "\n"
		return line

class IARQ(PARQControl):
	iarq_q1		= db.StringProperty()
	iarq_q2		= db.StringProperty()
	iarq_q3		= db.StringProperty()
	iarq_q4		= db.StringProperty()
	iarq_q5		= db.StringProperty()
	iarq_q6		= db.StringProperty()
	iarq_q7		= db.StringProperty()
	iarq_q8		= db.StringProperty()
	iarq_q9		= db.StringProperty()
	iarq_q10	= db.StringProperty()
	iarq_q11	= db.StringProperty()
	iarq_q12	= db.StringProperty()
	iarq_q13	= db.StringProperty()
	iarq_q14	= db.StringProperty()
	iarq_q15	= db.StringProperty()
	question_count	= 73
	dimension_count = 5

	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None

	def test_as_html_table(self, can_edit_test):
		q_values = [self.iarq_q1, self.iarq_q2, self.iarq_q3, self.iarq_q4, self.iarq_q5, self.iarq_q6, self.iarq_q7, self.iarq_q8, self.iarq_q9, self.iarq_q10, self.iarq_q11, self.iarq_q12, self.iarq_q13, self.iarq_q14, self.iarq_q15]
		q_labels = ["Relation",   "Current",    "Length (mos)", "Nature",   "Unique",     "Proximity",  "Distress",   "Joy",        "Secure",     "Close",       "Anxious",     "Ambivalent",  "Avoid",       "Well",        "End"]
		h = "<tr>"

		for q in range(0, len(q_values)):
			h += """<td colspan=2 align=right>%d</td>""" % (q + 1)
			maxlength = 3 if q == 2 else 1
			h += """<td colspan=2><input type=text name="iarq_q%d" value="%s" size=%d maxlength=%d><br />%s</td>""" % (q + 1, q_values[q] if q_values[q] != None else "", (maxlength + 1), maxlength, q_labels[q])
			if (q + 1) % 5 == 0:
				h += "</tr><tr>"
		h += "</tr><tr><td colspan=21><hr size=1/></td></tr>"
		h += TestBase.test_as_html_table(self, can_edit_test)
		return h

	def store_form(self, request):
		PARQControl.store_form(self, request)
		self.iarq_q1		= request.get("iarq_q1")
		self.iarq_q2		= request.get("iarq_q2")
		self.iarq_q3		= request.get("iarq_q3")
		self.iarq_q4		= request.get("iarq_q4")
		self.iarq_q5		= request.get("iarq_q5")
		self.iarq_q6		= request.get("iarq_q6")
		self.iarq_q7		= request.get("iarq_q7")
		self.iarq_q8		= request.get("iarq_q8")
		self.iarq_q9		= request.get("iarq_q9")
		self.iarq_q10   	= request.get("iarq_q10")
		self.iarq_q11   	= request.get("iarq_q11")
		self.iarq_q12   	= request.get("iarq_q12")
		self.iarq_q13   	= request.get("iarq_q13")
		self.iarq_q14   	= request.get("iarq_q14")
		self.iarq_q15   	= request.get("iarq_q15")

	def get_download_header(self):
		header = "id "
		for q in range(1, 16):
			header += " IARQ%d" % q

		question_count = self.question_count

		for q in range(1, self.dimension_count + 1):
			header += " dim%d" % q

		prefix = "Q"
		suffix = "I"

		for q in range(1, question_count + 1):
			header += " %s%d%s" % (prefix, q, suffix)

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		line = "%s" % (self.test_id)
		line += " %s" % (self.iarq_q1)
		line += " %s" % (self.iarq_q2)
		line += " %s" % (self.iarq_q3)
		line += " %s" % (self.iarq_q4)
		line += " %s" % (self.iarq_q5)
		line += " %s" % (self.iarq_q6)
		line += " %s" % (self.iarq_q7)
		line += " %s" % (self.iarq_q8)
		line += " %s" % (self.iarq_q9)
		line += " %s" % (self.iarq_q10)
		line += " %s" % (self.iarq_q11)
		line += " %s" % (self.iarq_q12)
		line += " %s" % (self.iarq_q13)
		line += " %s" % (self.iarq_q14)
		line += " %s" % (self.iarq_q15)

		line += " %d %d %d %d" % (self.as_number(self.dimension1_score), self.as_number(self.dimension2_score), self.as_number(self.dimension3_score), self.as_number(self.dimension4_score))
		if self.dimension_count == 5:
			line += " %d" % self.as_number(self.dimension5_score)
		line += " %d" % self.as_number(self.score)

		matrix	= self.get_scores_matrix()
		rows	= len(matrix)
		for row in range(0, rows):
			for col in range(0, self.dimension_count):
				item_score = self.get_item_score(row, col, matrix, False)
				if item_score >= 0:
					line += " %d" % item_score

		line += "\n"
		return line

class IARQShort(IARQ):
	dimension5_name	= None
	question_count	= 24
	dimension_count	= 4

	def get_scores_matrix(self):
		return [[self.q1	, -1		, self.q2	, -1],
				[self.q3	, self.q4	, -1		, self.q5],
				[-1			, self.q6	, self.q7	, self.q8],
				[self.q9	, self.q10	, self.q11	, -1],
				[self.q12	, -1		, self.q13	, -1],
				[-1			, self.q14	, self.q15	, self.q16],
				[self.q17	, self.q18	, -1		, -1],
				[self.q19	, self.q20	, -1		, self.q21],
				[self.q22	, -1		, self.q23	, -1],
				[self.q24	, -1		, -1		, -1],
				]

	def get_reverses_matrix(self):
		return [[1, 0, 0, 0],
				[1, 0, 0, 0],
				[1, 0, 0, 0],
				[1, 0, 0, 0],
				[1, 0, 1, 0],
				[1, 0, 0, 0],
				[1, 0, 0, 0],
				[1, 0, 0, 0],
				[1, 0, 0, 0],
				[1, 0, 0, 0],
				]


	def store_form(self, request):
		PARQControl.store_form(self, request)
		self.iarq_q1		= request.get("iarq_q1")
		self.iarq_q2		= request.get("iarq_q2")
		self.iarq_q3		= request.get("iarq_q3")
		self.iarq_q4		= request.get("iarq_q4")
		self.iarq_q5		= request.get("iarq_q5")
		self.iarq_q6		= request.get("iarq_q6")
		self.iarq_q7		= request.get("iarq_q7")
		self.iarq_q8		= request.get("iarq_q8")
		self.iarq_q9		= request.get("iarq_q9")
		self.iarq_q10   	= request.get("iarq_q10")
		self.iarq_q11   	= request.get("iarq_q11")
		self.iarq_q12   	= request.get("iarq_q12")
		self.iarq_q13   	= request.get("iarq_q13")
		self.iarq_q14   	= request.get("iarq_q14")
		self.iarq_q15   	= request.get("iarq_q15")

class IRAQ(TestBase):
	dimension1_name					= "IRAQ Items"
	max_unanswered_items			= 4
	dimension1_max_unanswered_items	= 1

	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None


	def get_scores_matrix(self):
		return [[self.q1],
				[self.q2],
				[self.q3],
				[self.q4],
				[self.q5],
				[self.q6],
				[self.q7],
				[self.q8],
				[self.q9]
				]

	def get_reverses_matrix(self):
		return [[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0]]

	def get_download_header(self):
		header = "id "
		for q in range(1, 10):
			header += " IRAQ%d" % q

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		line = "%s" % (self.test_id)
		line += " %s" % (self.q1)
		line += " %s" % (self.q2)
		line += " %s" % (self.q3)
		line += " %s" % (self.q4)
		line += " %s" % (self.q5)
		line += " %s" % (self.q6)
		line += " %s" % (self.q7)
		line += " %s" % (self.q8)
		line += " %s" % (self.q9)

		line += "\n"
		return line

class SUQ(TestBase):
	dimension1_name					= "SUQ Items"
	max_unanswered_items			= 4
	dimension1_max_unanswered_items	= 1
	item_validation_function		= "checkSUQEnteredValue"
	form_validation_function		= "validateSUQForm"

	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None

	def get_scores_matrix(self):
		return [[self.q1],
				[self.q2],
				[self.q3],
				[self.q4],
				[self.q5]
				]

	def get_reverses_matrix(self):
		return [[0],
				[0],
				[0],
				[0],
				[0]]

	def get_download_header(self):
		header = "id "
		for q in range(1, 6):
			header += " SUQ%d" % q

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		line = "%s" % (self.test_id)
		line += " %s" % (self.q1)
		line += " %s" % (self.q2)
		line += " %s" % (self.q3)
		line += " %s" % (self.q4)
		line += " %s" % (self.q5)

		line += "\n"
		return line

class ESARQ(PARQControl):
	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None

class ILARQ(PARQControl):
	which_in_law			= db.IntegerProperty()
	show_relationship_dropdown = True

	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None

class ThreePQ(TestBase):
	power_score				= db.IntegerProperty()
	prestige_score			= db.IntegerProperty()

	dimension1_name					= "Power Items"
	dimension2_name					= "Prestige Items"
	max_unanswered_items			= 4
	dimension1_max_unanswered_items	= 1
	item_validation_function		= "checkThreePQEnteredValue"
	form_validation_function		= "validateThreePQForm"

	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None

	def get_scores_matrix(self):
		return [[self.q1, self.q2],
				[self.q3, self.q4],
				[self.q5, self.q6],
				[self.q7, self.q8],
				[self.q9, self.q10],
				]

	def get_reverses_matrix(self):
		return [[0, 0],
				[0, 0],
				[0, 0],
				[0, 0],
				[0, 0]]

	def get_score(self):
		self.power_score			= int(self.q1) + int(self.q3) + int(self.q5) + int(self.q7) + int(self.q9)
		self.prestige_score			= int(self.q2) + int(self.q4) + int(self.q6) + int(self.q8) + int(self.q10)
		self.dimension1_score		= self.power_score
		self.dimension2_score		= self.prestige_score

		self.score	= self.power_score + self.prestige_score

	def get_download_header(self):
		header = "id POWER PREST"

		suffix = "A"
		if self.respondent == "Youth":
			suffix = "Y"

		for q in range(1, 11):
			header += " 3P%d%s" % (q, suffix)

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		line = "%s" % (self.test_id)

		line += " %d" % (self.as_number(self.power_score))
		line += " %d" % (self.as_number(self.prestige_score))

		line += " %s" % (self.q1)
		line += " %s" % (self.q2)
		line += " %s" % (self.q3)
		line += " %s" % (self.q4)
		line += " %s" % (self.q5)
		line += " %s" % (self.q6)
		line += " %s" % (self.q7)
		line += " %s" % (self.q8)
		line += " %s" % (self.q9)
		line += " %s" % (self.q10)

		line += "\n"
		return line


class YouthThreePQ(ThreePQ):
	def sets(self):
		self.relationship				= None
		self.respondent					= "Youth"
		self.subject					= None

class AdultThreePQ(ThreePQ):
	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None

class BestFriendARQ(TestBase):
	dimension1_name					= "Warmth/Affection"
	dimension2_name					= "Hostility/Aggression"
	dimension3_name					= "Indifference/Neglect"
	dimension4_name					= "Undifferentiated Rejection"

	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None

	def get_scores_matrix(self):
		return [[self.q1	, self.q2	, self.q3	, self.q4],
				[self.q5	, self.q6	, self.q7	, -1],
				[self.q8	, self.q9	, self.q10	, self.q11],
				[self.q12	, self.q13	, self.q14	, -1],
				[self.q15	, self.q16	, self.q17	, self.q18],
				[self.q19	, self.q20	, self.q21	, -1],
				[self.q22	, self.q23	, self.q24	, self.q25],
				[self.q26	, self.q27	, self.q28	, -1],
				[self.q29	, self.q30	, self.q31	, self.q32],
				[self.q33	, self.q34	, self.q35	, -1],
				[self.q36	, self.q37	, self.q38	, self.q39],
				[self.q40	, self.q41	, self.q42	, -1],
				[self.q43	, self.q44	, self.q45	, self.q46],
				[self.q47	, self.q48	, self.q49	, -1],
				[self.q50	, self.q51	, self.q52	, self.q53],
				[self.q54	, -1		, -1		, -1],
				[self.q55	, -1		, -1		, self.q56],
				[self.q57	, -1		, -1		, -1],
				[self.q58	, -1		, -1		, self.q59],
				[self.q60	, -1		, -1		, -1],
				]

	def get_reverses_matrix(self):
		return [[1, 0, 0, 0],
				[1, 0, 1, 0],
				[1, 0, 0, 0],
				[1, 0, 1, 0],
				[1, 0, 0, 0],
				[1, 0, 1, 0],
				[1, 0, 0, 0],
				[1, 0, 1, 0],
				[1, 0, 0, 0],
				[1, 0, 1, 0],
				[1, 0, 0, 0],
				[1, 0, 1, 0],
				[1, 0, 0, 0],
				[1, 0, 1, 0],
				[1, 0, 0, 0],
				[1, 0, 1, 0],
				[1, 0, 1, 0],
				[1, 0, 1, 0],
				[1, 0, 1, 0],
				[1, 0, 1, 0],
				[1, 0, 1, 0],
				[1, 0]]

	def get_download_header(self):
		header = "id Warmth Host indiff unrejn TotlBFARQ "
		question_count = 60

		for q in range(1, question_count + 1):
			header += " BFARQ%d" % (q)

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		if self.subject == "Other":
			relationship = self.relationship
		else:
			relationship = ""

		line = "%s %d %d %d %d %d" % (self.test_id, self.dimension1_score, self.dimension2_score, self.dimension3_score, self.dimension4_score, self.score)

		matrix	= self.get_scores_matrix()
		rows	= len(matrix)
		for row in range(0, rows):
			for col in range(0, 4):
				item_score = self.get_item_score(row, col, matrix, False)
				if item_score >= 0:
					line += " %d" % item_score

		line += "\n"
		return line

class BestFriendARQShort(TestBase):
	dimension1_name					= "Warmth/Affection"
	dimension2_name					= "Hostility/Aggression"
	dimension3_name					= "Indifference/Neglect"
	dimension4_name					= "Undifferentiated Rejection"

	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None

	def get_scores_matrix(self):
		return [[self.q1	, -1		, self.q2	, -1],
				[self.q3	, self.q4	, -1		, self.q5],
				[-1			, self.q6	, self.q7	, self.q8],
				[self.q9	, self.q10	, self.q11	, -1],
				[self.q12	, -1		, self.q13	, -1],
				[-1			, self.q14	, self.q15	, self.q16],
				[self.q17	, self.q18	, -1		, -1],
				[self.q19	, self.q20	, -1		, self.q21],
				[self.q22	, -1		, self.q23	, -1],
				[self.q24	, -1		, -1		, -1],
				]

	def get_reverses_matrix(self):
		return [[1, 0, 0, 0],
				[1, 0, 0, 0],
				[1, 0, 0, 0],
				[1, 0, 0, 0],
				[1, 0, 1, 0],
				[1, 0, 0, 0],
				[1, 0, 0, 0],
				[1, 0, 0, 0],
				[1, 0, 0, 0],
				[1, 0, 0, 0],
				[1, 0, 0, 0],
				[1, 0, 0, 0]]

	def get_download_header(self):
		header = "id Warmth Host indiff unrejn TotlBFARQ "
		question_count = 24

		for q in range(1, question_count + 1):
			header += " BFARQS%d" % (q)

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		if self.subject == "Other":
			relationship = self.relationship
		else:
			relationship = ""

		line = "%s %d %d %d %d %d" % (self.test_id, self.dimension1_score, self.dimension2_score, self.dimension3_score, self.dimension4_score, self.score)

		matrix	= self.get_scores_matrix()
		rows	= len(matrix)
		for row in range(0, rows):
			for col in range(0, 4):
				item_score = self.get_item_score(row, col, matrix, False)
				if item_score >= 0:
					line += " %d" % item_score

		line += "\n"
		return line


class PECC(TestBase):
	dimension1_name					= "PECC Items"
	max_unanswered_items			= 4
	dimension1_max_unanswered_items	= 1

	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None

	def get_scores_matrix(self):
		return [[self.q1],
				[self.q2],
				[self.q3],
				[self.q4],
				[self.q5],
				[self.q6],
				[self.q7],
				[self.q8],
				[self.q9],
				[self.q10],
				[self.q11],
				[self.q12],
				[self.q13],
				[self.q14],
				[self.q15],
				[self.q16],
				[self.q17],
				[self.q18]
				]

	def get_reverses_matrix(self):
		return [[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0]]

	def get_download_header(self):
		header = "id"

		for q in range(1, 19):
			header += " PECC%d" % (q)

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		line = "%s" % (self.test_id)

		line += " %s" % (self.q1)
		line += " %s" % (self.q2)
		line += " %s" % (self.q3)
		line += " %s" % (self.q4)
		line += " %s" % (self.q5)
		line += " %s" % (self.q6)
		line += " %s" % (self.q7)
		line += " %s" % (self.q8)
		line += " %s" % (self.q9)
		line += " %s" % (self.q10)
		line += " %s" % (self.q11)
		line += " %s" % (self.q12)
		line += " %s" % (self.q13)
		line += " %s" % (self.q14)
		line += " %s" % (self.q15)
		line += " %s" % (self.q16)
		line += " %s" % (self.q17)
		line += " %s" % (self.q18)

		line += "\n"
		return line

class GenderInequality(TestBase):
	dimension1_name					= "Gender Inequality Items"
	max_unanswered_items			= 4
	dimension1_max_unanswered_items	= 1
	# item_validation_function		= "checkSUQEnteredValue"
	# form_validation_function		= "validateSUQForm"

	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None

	def get_scores_matrix(self):
		return [[self.q1],
				[self.q2],
				[self.q3],
				[self.q4],
				[self.q5]
				]

	def get_reverses_matrix(self):
		return [[0],
				[0],
				[0],
				[0],
				[0]]

	def get_download_header(self):
		header = "id "
		for q in range(1, 6):
			header += " GenderInequality%d" % q

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		line = "%s" % (self.test_id)
		line += " %s" % (self.q1)
		line += " %s" % (self.q2)
		line += " %s" % (self.q3)
		line += " %s" % (self.q4)
		line += " %s" % (self.q5)

		line += "\n"
		return line


class IPARLS(TestBase):
	dimension1_name					= "IPAR Loneliness Scale"
	max_unanswered_items			= 15
	dimension1_max_unanswered_items	= 1
	# item_validation_function		= "checkSUQEnteredValue"
	# form_validation_function		= "validateSUQForm"

	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None

	def get_scores_matrix(self):
		return [[self.q1],
				[self.q2],
				[self.q3],
				[self.q4],
				[self.q5],
				[self.q6],
				[self.q7],
				[self.q8],
				[self.q9],
				[self.q10],
				[self.q11],
				[self.q12],
				[self.q13],
				[self.q14],
				[self.q15]]

	def get_reverses_matrix(self):
		return [[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0],
				[0]]

	def get_download_header(self):
		header = "id "
		for q in range(1, 6):
			header += " IPARLS%d" % q

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		line = "%s" % (self.test_id)
		line += " %s" % (self.q1)
		line += " %s" % (self.q2)
		line += " %s" % (self.q3)
		line += " %s" % (self.q4)
		line += " %s" % (self.q5)
		line += " %s" % (self.q6)
		line += " %s" % (self.q7)
		line += " %s" % (self.q8)
		line += " %s" % (self.q9)
		line += " %s" % (self.q10)
		line += " %s" % (self.q11)
		line += " %s" % (self.q12)
		line += " %s" % (self.q13)
		line += " %s" % (self.q14)
		line += " %s" % (self.q15)

		line += "\n"
		return line


class IRSS(TestBase):
	# dimension1_name					= "Interpersonal Rejection Sensitivity Scale"
	max_unanswered_items			= 13
	dimension1_max_unanswered_items	= 1
	# item_validation_function		= "checkSUQEnteredValue"
	# form_validation_function		= "validateSUQForm"

	def sets(self):
		self.relationship				= None
		self.respondent					= "Adult"
		self.subject					= None

	def get_scores_matrix(self):
		return [[-1, self.q1],
				[-1, self.q2],
				[-1, self.q3],
				[-1, self.q4],
				[-1, self.q5],
				[-1, self.q6],
				[-1, self.q7],
				[-1, self.q8],
				[-1, self.q9],
				[-1, self.q10],
				[-1, self.q11],
				[-1, self.q12],
				[-1, self.q13],
				]

	def get_reverses_matrix(self):
		return [[0, 0],
				[0, 0],
				[0, 1],
				[0, 0],
				[0, 0],
				[0, 0],
				[0, 0],
				[0, 0],
				[0, 0],
				[0, 0],
				[0, 0],
				[0, 1],
				[0, 0],
				]

	def get_download_header(self):
		header = "id "
		for q in range(1, 6):
			header += " IRSS%d" % q

		return header

	def get_download_testname(self):
		return self.test_name

	def get_download_line(self):
		line = "%s" % (self.test_id)
		line += " %s" % (self.q1)
		line += " %s" % (self.q2)
		line += " %s" % (self.q3)
		line += " %s" % (self.q4)
		line += " %s" % (self.q5)
		line += " %s" % (self.q6)
		line += " %s" % (self.q7)
		line += " %s" % (self.q8)
		line += " %s" % (self.q9)
		line += " %s" % (self.q10)
		line += " %s" % (self.q11)
		line += " %s" % (self.q12)
		line += " %s" % (self.q13)

		line += "\n"
		return line
