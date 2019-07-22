import unittest
import logging
import inspect

from google.appengine.ext import db
from Models.TestModels import *
#import model

class SuccessFailError(unittest.TestCase):
	def setUp(self):
		logging.info('In setUp()')

	def tearDown(self):
		logging.info('In tearDown()')

	def test_parq_control(self):
		logging.info('Running test_parq_control()')
		t = PARQControl(test_name=TestBase.AdultPARQControlFatherName)
		self.assign_ones(t)
		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 80)
		self.assertTrue(self.dimension2_score(t) == 15)
		self.assertTrue(self.dimension3_score(t) == 36)
		self.assertTrue(self.dimension4_score(t) == 10)
		self.assertTrue(self.dimension5_score(t) == 25)

		self.assertTrue(t.score == 141)

		t = PARQControl(test_name=TestBase.AdultPARQControlFatherName)
		self.assign_fours(t)
		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 20)
		self.assertTrue(self.dimension2_score(t) == 60)
		self.assertTrue(self.dimension3_score(t) == 39)
		self.assertTrue(self.dimension4_score(t) == 40)
		self.assertTrue(self.dimension5_score(t) == 40)

		self.assertTrue(t.score == 159)

	def test_parq_control_with_blank(self):
		logging.info('Running test_parq_control_with_blank()')
		t = PARQControl(test_name=TestBase.AdultPARQControlFatherName)
		self.assign_fours(t)
		t.q73 = "0"
		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 20)
		self.assertTrue(self.dimension2_score(t) == 60)
		self.assertTrue(self.dimension3_score(t) == 39)
		self.assertTrue(self.dimension4_score(t) == 40)
		self.assertTrue(self.dimension5_score(t) == 40)

		self.assertTrue(t.score == 159)
		
	def test_parq_control_with_a_few_blanks(self):
		logging.info('Running test_parq_control_with_a_few_blanks()')
		t = PARQControl(test_name=TestBase.AdultPARQControlFatherName)
		self.assign_fours(t)
		t.q59 = "0"
		t.q64 = "0"
		t.q65 = "0"
		t.q66 = "0"
		t.q73 = "0"
		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 20)
		self.assertTrue(self.dimension2_score(t) == 60)
		self.assertTrue(self.dimension3_score(t) == 38)
		self.assertTrue(self.dimension4_score(t) == 40)
		self.assertTrue(self.dimension5_score(t) == 39)

		self.assertTrue(t.score == 158)

	def test_parq_control_short(self):
		logging.info('Running test_parq_control_short()')
		t = PARQControlShort(test_name=TestBase.ChildPARQFatherShortName)
		self.assign_ones(t)
		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 32)
		self.assertTrue(self.dimension2_score(t) == 6)
		self.assertTrue(self.dimension3_score(t) == 9)
		self.assertTrue(self.dimension4_score(t) == 4)
		self.assertTrue(self.dimension5_score(t) == 8)

		self.assertTrue(t.score == 51)

	def test_parq_control_short_with_twos(self):
		logging.info('Running test_parq_control_short_with_twos()')
		t = PARQControlShort(test_name=TestBase.ChildPARQFatherShortName)
		self.assign_twos(t)
		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 24)
		self.assertTrue(self.dimension2_score(t) == 12)
		self.assertTrue(self.dimension3_score(t) == 13)
		self.assertTrue(self.dimension4_score(t) == 8)
		self.assertTrue(self.dimension5_score(t) == 11)

		self.assertTrue(t.score == 57)

	def test_parq_control_short_with_a_few_blanks(self):
		logging.info('Running test_parq_control_short_with_a_few_blanks()')
		t = PARQControlShort(test_name=TestBase.ChildPARQFatherShortName)
		self.assign_twos(t)

		t.q4 = "0"
		t.q5 = "0"
		t.q16 = "0"

		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 24)
		self.assertTrue(self.dimension2_score(t) == 12)
		self.assertTrue(self.dimension3_score(t) == 13)
		self.assertTrue(self.dimension4_score(t) == 8)
		self.assertTrue(self.dimension5_score(t) == 11)

		self.assertTrue(t.score == 57)

	def test_parq_control_infant(self):
		logging.info('Running test_parq_control_infant()')
		t = PARQControlInfant(test_name=TestBase.PARQControlInfantName)
		self.assign_ones(t)
		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 68)
		self.assertTrue(self.dimension2_score(t) == 15)
		self.assertTrue(self.dimension3_score(t) == 31)
		self.assertTrue(self.dimension4_score(t) == 16)
		self.assertTrue(self.dimension5_score(t) == 14)

		self.assertTrue(t.score == 130)

		self.assign_threes(t)
		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 34)
		self.assertTrue(self.dimension2_score(t) == 45)
		self.assertTrue(self.dimension3_score(t) == 33)
		self.assertTrue(self.dimension4_score(t) == 28)
		self.assertTrue(self.dimension5_score(t) == 22)

		self.assertTrue(t.score == 140)
		
	def test_parq_control_infant_with_a_few_blanks(self):
		logging.info('Running test_parq_control_infant_with_a_few_blanks()')
		t = PARQControlInfant(test_name=TestBase.PARQControlInfantName)
		self.assign_threes(t)
		t.q36	= "0"
		t.q37	= "0"
		t.q38	= "0"
		t.q39	= "0"
		t.q40	= "0"

		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 34)
		self.assertTrue(self.dimension2_score(t) == 45)
		self.assertTrue(self.dimension3_score(t) == 33)
		self.assertTrue(self.dimension4_score(t) == 28)
		self.assertTrue(self.dimension5_score(t) == 22)

		self.assertTrue(t.score == 140)
		
	def test_parq(self):
		logging.info('Running test_parq()')
		t = PARQ(test_name=TestBase.ChildPARQFatherName)
		self.assign_ones(t)
		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 80)
		self.assertTrue(self.dimension2_score(t) == 15)
		self.assertTrue(self.dimension3_score(t) == 36)
		self.assertTrue(self.dimension4_score(t) == 10)

		self.assertTrue(t.score == 141)

		self.assign_twos(t)
		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 60)
		self.assertTrue(self.dimension2_score(t) == 30)
		self.assertTrue(self.dimension3_score(t) == 37)
		self.assertTrue(self.dimension4_score(t) == 20)

		self.assertTrue(t.score == 147)

	def test_parq_with_a_few_blanks(self):
		logging.info('Running test_parq_with_a_few_blanks()')
		t = PARQ(test_name=TestBase.AdultPARQControlFatherName)
		self.assign_twos(t)
		t.q40	= "0"
		t.q41	= "0"
		t.q42	= "0"
		t.q46	= "0"
		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 60)
		self.assertTrue(self.dimension2_score(t) == 30)
		self.assertTrue(self.dimension3_score(t) == 37)
		self.assertTrue(self.dimension4_score(t) == 20)

		self.assertTrue(t.score == 147)


	def test_parq_short(self):
		logging.info('Running test_parq_control_short()')
		t = PARQShort(test_name=TestBase.ChildPARQFatherShortName)
		self.assign_ones(t)
		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 32)
		self.assertTrue(self.dimension2_score(t) == 6)
		self.assertTrue(self.dimension3_score(t) == 9)
		self.assertTrue(self.dimension4_score(t) == 4)

		self.assertTrue(t.score == 51)

	def test_child_paq(self):
		logging.info('Running test_child_paq()')
		t = ChildPAQ(test_name=TestBase.ChildPAQName)
		self.assign_ones(t)
		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 6)
		self.assertTrue(self.dimension2_score(t) == 9)
		self.assertTrue(self.dimension3_score(t) == 15)
		self.assertTrue(self.dimension4_score(t) == 15)
		self.assertTrue(self.dimension5_score(t) == 15)
		self.assertTrue(self.dimension6_score(t) == 9)
		self.assertTrue(self.dimension7_score(t) == 15)

		self.assertTrue(t.score == 84)

	def test_adult_paq(self):
		logging.info('Running test_adult_paq()')
		t = AdultPAQ(test_name=TestBase.AdultPAQName)
		self.assign_ones(t)
		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 9)
		self.assertTrue(self.dimension2_score(t) == 15)
		self.assertTrue(self.dimension3_score(t) == 18)
		self.assertTrue(self.dimension4_score(t) == 21)
		self.assertTrue(self.dimension5_score(t) == 18)
		self.assertTrue(self.dimension6_score(t) == 18)
		self.assertTrue(self.dimension7_score(t) == 24)

		self.assertTrue(t.score == 123)

	def test_iparcq(self):
		logging.info('Running test_iparcq()')
		t = IPARCQ(test_name=TestBase.IPARCQName)
		self.assign_ones(t)
		t.get_score()

		self.assertTrue(self.dimension1_score(t) == 80)
		self.assertTrue(self.dimension2_score(t) == 15)
		self.assertTrue(self.dimension3_score(t) == 36)
		self.assertTrue(self.dimension4_score(t) == 10)
		self.assertTrue(self.dimension5_score(t) == 25)

		self.assertTrue(t.score == 141)

	def test_tesc(self):
		logging.info('Running test_tesc()')
		t = TESC(test_name=TestBase.TESCName)
		self.assign_ones(t)
		t.get_score()

		self.assertTrue(t.score == 18)

	def test_ppq(self):
		logging.info('Running test_ppq()')
		t = PPQ(test_name=TestBase.YouthPPQMotherName)
		self.assign_ones(t)
		t.get_score()

		self.assertTrue(t.harsh_score == 2)
		self.assertTrue(t.just_score == 2)
		self.assertTrue(t.score == 17)

	def test_parent_ppq(self):
		logging.info('Running test_parent_ppq()')
		t = ParentPPQ(test_name=TestBase.ParentPPQName)
		self.assign_ones(t)
		t.get_score()

		self.assertTrue(t.harsh_score == 2)
		self.assertTrue(t.just_score == 2)
		self.assertTrue(t.score == 17)

	def test_three_pq(self):
		logging.info('Running test_three_pq()')
		t = YouthThreePQ(test_name=TestBase.YouthThreePQName)
		self.assign_ones(t)
		t.get_score()

		self.assertTrue(t.power_score == 5)
		self.assertTrue(t.prestige_score == 5)
		self.assertTrue(t.score == 10)

	def test_pecc(self):
		logging.info('Running test_pecc()')
		t = PECC(test_name=TestBase.PECCName)
		self.assign_ones(t)
		t.get_score()

		self.assertTrue(t.score == 18)

	def dimension1_score(self, t):
		dim_sum, new_msg, score_type, dim_number_of_zeroes, dim_avg = t.get_dimension_score(0, t.get_scores_matrix(), t.dimension1_max_unanswered_items, t.dimension1_name)
		return dim_sum
	def dimension2_score(self, t):
		dim_sum, new_msg, score_type, dim_number_of_zeroes, dim_avg = t.get_dimension_score(1, t.get_scores_matrix(), t.dimension2_max_unanswered_items, t.dimension2_name)
		return dim_sum
	def dimension3_score(self, t):
		dim_sum, new_msg, score_type, dim_number_of_zeroes, dim_avg = t.get_dimension_score(2, t.get_scores_matrix(), t.dimension3_max_unanswered_items, t.dimension3_name)
		return dim_sum
	def dimension4_score(self, t):
		dim_sum, new_msg, score_type, dim_number_of_zeroes, dim_avg = t.get_dimension_score(3, t.get_scores_matrix(), t.dimension4_max_unanswered_items, t.dimension4_name)
		return dim_sum
	def dimension5_score(self, t):
		dim_sum, new_msg, score_type, dim_number_of_zeroes, dim_avg = t.get_dimension_score(4, t.get_scores_matrix(), t.dimension5_max_unanswered_items, t.dimension5_name)
		return dim_sum
	def dimension6_score(self, t):
		dim_sum, new_msg, score_type, dim_number_of_zeroes, dim_avg = t.get_dimension_score(5, t.get_scores_matrix(), t.dimension6_max_unanswered_items, t.dimension6_name)
		return dim_sum
	def dimension7_score(self, t):
		dim_sum, new_msg, score_type, dim_number_of_zeroes, dim_avg = t.get_dimension_score(6, t.get_scores_matrix(), t.dimension7_max_unanswered_items, t.dimension7_name)
		return dim_sum
		
	def assign_ones(self, t):
		self.assign_value(t, "1")
		
	def assign_twos(self, t):
		self.assign_value(t, "2")

	def assign_threes(self, t):
		self.assign_value(t, "3")

	def assign_fours(self, t):
		self.assign_value(t, "4")

	def assign_value(self, t, v):
		t.q1 = v
		t.q2 = v
		t.q3 = v
		t.q4 = v
		t.q5 = v
		t.q6 = v
		t.q7 = v
		t.q8 = v
		t.q9 = v
		t.q10 = v
		t.q11 = v
		t.q12 = v
		t.q13 = v
		t.q14 = v
		t.q15 = v
		t.q16 = v
		t.q17 = v
		t.q18 = v
		t.q19 = v
		t.q20 = v
		t.q21 = v
		t.q22 = v
		t.q23 = v
		t.q24 = v
		t.q25 = v
		t.q26 = v
		t.q27 = v
		t.q28 = v
		t.q29 = v
		t.q30 = v
		t.q31 = v
		t.q32 = v
		t.q33 = v
		t.q34 = v
		t.q35 = v
		t.q36 = v
		t.q37 = v
		t.q38 = v
		t.q39 = v
		t.q40 = v
		t.q41 = v
		t.q42 = v
		t.q43 = v
		t.q44 = v
		t.q45 = v
		t.q46 = v
		t.q47 = v
		t.q48 = v
		t.q49 = v
		t.q50 = v
		t.q51 = v
		t.q52 = v
		t.q53 = v
		t.q54 = v
		t.q55 = v
		t.q56 = v
		t.q57 = v
		t.q58 = v
		t.q59 = v
		t.q60 = v
		t.q61 = v
		t.q62 = v
		t.q63 = v
		t.q64 = v
		t.q65 = v
		t.q66 = v
		t.q67 = v
		t.q68 = v
		t.q69 = v
		t.q70 = v
		t.q71 = v
		t.q72 = v
		t.q73 = v
