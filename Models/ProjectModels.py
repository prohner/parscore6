import os
import sys

from google.appengine.ext import db 
from google.appengine.ext.db import polymodel
from google.appengine.api import users

#sys.path.append(os.path.join(os.path.dirname(__file__), "Models"))
import Models.TestModels 

class ParScoreUser(db.Model):
	project_owner				= db.UserProperty()
	current_project				= db.StringProperty()

class Project(db.Model):
	project_owner				= db.UserProperty()
	name_of_researcher			= db.StringProperty()
	city						= db.StringProperty()
	province					= db.StringProperty()
	country						= db.StringProperty()
	affiliated_institution		= db.StringProperty()
	project_title				= db.StringProperty()
	project_category			= db.StringProperty()
	language_used				= db.StringProperty()
	measures_used_in_project	= db.StringProperty()
	has_been_saved				= db.StringProperty()
	permission_granted			= db.StringProperty()
	reason_not_agreeing			= db.StringProperty()
	date_added					= db.DateTimeProperty(auto_now_add=True)
	date_updated				= db.DateTimeProperty(auto_now=True)

	category_01					= db.StringProperty()
	category_02					= db.StringProperty()
	category_03					= db.StringProperty()
	category_04					= db.StringProperty()
	category_05					= db.StringProperty()
	category_06					= db.StringProperty()
	category_07					= db.StringProperty()
	category_08					= db.StringProperty()
	category_09					= db.StringProperty()
	category_10					= db.StringProperty()
	category_11					= db.StringProperty()
	category_12					= db.StringProperty()
	category_13					= db.StringProperty()
	category_14					= db.StringProperty()
	category_15					= db.StringProperty()
	category_16					= db.StringProperty()
	category_17					= db.StringProperty()
	category_18					= db.StringProperty()
	category_19					= db.StringProperty()
	category_20					= db.StringProperty()
	category_21					= db.StringProperty()
	category_22					= db.StringProperty()
	category_23					= db.StringProperty()
	category_24					= db.StringProperty()
	category_25					= db.StringProperty()
	category_26					= db.StringProperty()
	category_27					= db.StringProperty()
	category_28					= db.StringProperty()
	category_29					= db.StringProperty()
	category_30					= db.StringProperty()
	category_31					= db.StringProperty()
	category_32					= db.StringProperty()
	category_33					= db.StringProperty()
	category_34					= db.StringProperty()

	measure_01					= db.StringProperty()
	measure_02					= db.StringProperty()
	measure_03					= db.StringProperty()
	measure_04					= db.StringProperty()
	measure_05					= db.StringProperty()
	measure_06					= db.StringProperty()
	measure_07					= db.StringProperty()
	measure_08					= db.StringProperty()
	measure_09					= db.StringProperty()
	measure_10					= db.StringProperty()
	measure_11					= db.StringProperty()
	measure_12					= db.StringProperty()
	measure_13					= db.StringProperty()
	measure_14					= db.StringProperty()
	measure_15					= db.StringProperty()
	measure_16					= db.StringProperty()
	measure_17					= db.StringProperty()
	measure_18					= db.StringProperty()
	measure_19					= db.StringProperty()
	measure_20					= db.StringProperty()
	measure_21					= db.StringProperty()
	measure_22					= db.StringProperty()
	measure_23					= db.StringProperty()
	measure_24					= db.StringProperty()
	measure_25					= db.StringProperty()
	measure_26					= db.StringProperty()
	measure_27					= db.StringProperty()
	measure_28					= db.StringProperty()
	measure_29					= db.StringProperty()
	measure_30					= db.StringProperty()
	measure_31					= db.StringProperty()
	measure_32					= db.StringProperty()
	measure_33					= db.StringProperty()
	measure_34					= db.StringProperty()
	measure_35					= db.StringProperty()
	measure_36					= db.StringProperty()
	measure_37					= db.StringProperty()
	measure_38					= db.StringProperty()
	measure_39					= db.StringProperty()
	measure_40					= db.StringProperty()
	measure_41					= db.StringProperty()
	measure_42					= db.StringProperty()
	measure_43					= db.StringProperty()
	measure_44					= db.StringProperty()
	measure_45					= db.StringProperty()
	measure_46					= db.StringProperty()

	def store_form(self, req):
		if not self.project_owner:
			self.project_owner			= users.get_current_user()
		self.name_of_researcher			= req.get("name_of_researcher")
		self.city						= req.get("city")
		self.province					= req.get("province")
		self.country					= req.get("country")
		self.affiliated_institution		= req.get("affiliated_institution")
		self.project_title				= req.get("project_title")
		self.language_used				= req.get("language_used")
		self.permission_granted			= req.get("permission_granted")
		self.reason_not_agreeing		= req.get("reason_not_agreeing")


		self.category_01	= req.get("category_1")
		self.category_02	= req.get("category_2")
		self.category_03	= req.get("category_3")
		self.category_04	= req.get("category_4")
		self.category_05	= req.get("category_5")
		self.category_06	= req.get("category_6")
		self.category_07	= req.get("category_7")
		self.category_08	= req.get("category_8")
		self.category_09	= req.get("category_9")
		self.category_10	= req.get("category_10")
		self.category_11	= req.get("category_11")
		self.category_12	= req.get("category_12")
		self.category_13	= req.get("category_13")
		self.category_14	= req.get("category_14")
		self.category_15	= req.get("category_15")
		self.category_16	= req.get("category_16")
		self.category_17	= req.get("category_17")
		self.category_18	= req.get("category_18")
		self.category_19	= req.get("category_19")
		self.category_20	= req.get("category_20")
		self.category_21	= req.get("category_21")
		self.category_22	= req.get("category_22")
		self.category_23	= req.get("category_23")
		self.category_24	= req.get("category_24")
		self.category_25	= req.get("category_25")
		self.category_26	= req.get("category_26")
		self.category_27	= req.get("category_27")
		self.category_28	= req.get("category_28")
		self.category_29	= req.get("category_29")
		self.category_30	= req.get("category_30")
		self.category_31	= req.get("category_31")
		self.category_32	= req.get("category_32")
		self.category_33	= req.get("category_33")
		self.category_34	= req.get("category_34")

		self.measure_01	= req.get("measure_1")
		self.measure_02	= req.get("measure_2")
		self.measure_03	= req.get("measure_3")
		self.measure_04	= req.get("measure_4")
		self.measure_05	= req.get("measure_5")
		self.measure_06	= req.get("measure_6")
		self.measure_07	= req.get("measure_7")
		self.measure_08	= req.get("measure_8")
		self.measure_09	= req.get("measure_9")
		self.measure_10	= req.get("measure_10")
		self.measure_11	= req.get("measure_11")
		self.measure_12	= req.get("measure_12")
		self.measure_13	= req.get("measure_13")
		self.measure_14	= req.get("measure_14")
		self.measure_15	= req.get("measure_15")
		self.measure_16	= req.get("measure_16")
		self.measure_17	= req.get("measure_17")
		self.measure_18	= req.get("measure_18")
		self.measure_19	= req.get("measure_19")
		self.measure_20	= req.get("measure_20")
		self.measure_21	= req.get("measure_21")
		self.measure_22	= req.get("measure_22")
		self.measure_23	= req.get("measure_23")
		self.measure_24	= req.get("measure_24")
		self.measure_25	= req.get("measure_25")
		self.measure_26	= req.get("measure_26")
		self.measure_27	= req.get("measure_27")
		self.measure_28	= req.get("measure_28")
		self.measure_29	= req.get("measure_29")
		self.measure_30	= req.get("measure_30")
		self.measure_31	= req.get("measure_31")
		self.measure_32	= req.get("measure_32")
		self.measure_33	= req.get("measure_33")
		self.measure_34	= req.get("measure_34")
		self.measure_35	= req.get("measure_35")
		self.measure_36	= req.get("measure_36")
		self.measure_37	= req.get("measure_37")
		self.measure_38	= req.get("measure_38")
		self.measure_39	= req.get("measure_39")
		self.measure_40	= req.get("measure_40")
		self.measure_41	= req.get("measure_41")
		self.measure_42	= req.get("measure_42")
		self.measure_43	= req.get("measure_43")
		self.measure_44	= req.get("measure_44")
		self.measure_45	= req.get("measure_45")
		self.measure_46	= req.get("measure_46")
		
	def get_measures_checkboxes(self, user_is_owner):
		h = "<table border=0>"
		list = Models.TestModels.TestBase.get_project_test_list()
		indenting = False

		question_number = 0
		for cb in range(0, len(list)):
			if list[cb].startswith("T:"):
				indenting = True
				h += """<tr><td>&nbsp;&gt;</td><td colspan=2>%s</td></tr>""" % (list[cb][2:])
			elif list[cb] == "END:":
				indenting = False
			else:
				h += "<tr>"
				if indenting:
					h += "<td>&nbsp;</td>"
				h += "<td>"
				
				if user_is_owner:
					h += """<input type="checkbox" value="%s" name="measure_%d" """ % (list[cb], question_number + 1)
					if self.measure_values()[question_number] != "" and self.measure_values()[question_number] != None:
						h += " checked "
					h += ">"
					h += "</td>"
					h += "<td %s>" % ("" if indenting else "colspan=2")
					h += """%s """ % (list[cb])
					#h += """ (question_number==%d), (cb==%d) """ % (question_number, cb)
				else:
					if self.measure_values()[question_number] != "" and self.measure_values()[question_number] != None:
						h += " &radic;"
					else:
						h += " &nbsp;"
					h += "<td %s>" % ("" if indenting else "colspan=2")
					h += """%s """ % (list[cb])
				h += "</td>"
				h += "</tr>"
				question_number += 1
			
		h += "</table>"
		return h



		if user_is_owner:
			h += """<input type="checkbox" value="%s" name="category_%d" """ % (self.categories[cb], cb + 1)
			if self.category_values()[cb] != "" and self.category_values()[cb] != None:
				h += " checked "
			h += ">%s" % (self.categories[cb])
		else:
			if self.category_values()[cb] != "" and self.category_values()[cb] != None:
				h += " &radic; "
			else:
				h += " &nbsp; "
			h += "%s" % (self.categories[cb])







		
	def measure_values(self):
		return [self.measure_01,
				self.measure_02,
				self.measure_03,
				self.measure_04,
				self.measure_05,
				self.measure_06,
				self.measure_07,
				self.measure_08,
				self.measure_09,
				self.measure_10,
				self.measure_11,
				self.measure_12,
				self.measure_13,
				self.measure_14,
				self.measure_15,
				self.measure_16,
				self.measure_17,
				self.measure_18,
				self.measure_19,
				self.measure_20,
				self.measure_21,
				self.measure_22,
				self.measure_23,
				self.measure_24,
				self.measure_25,
				self.measure_26,
				self.measure_27,
				self.measure_28,
				self.measure_29,
				self.measure_30,
				self.measure_31,
				self.measure_32,
				self.measure_33,
				self.measure_34,
				self.measure_35,
				self.measure_36,
				self.measure_37,
				self.measure_38,
				self.measure_39,
				self.measure_40,
				self.measure_41,
				self.measure_42,
				self.measure_43,
				self.measure_44,
				self.measure_45,
				self.measure_46
				]
	def get_category_checkboxes(self, user_is_owner):
		h = "<table border=0>"
		h += "<tr>"
		i = 0
		for cb in range(0, len(self.categories)):
			if i % 2 == 0:
				h += "<tr>"
			i += 1
			
			h += "<td nowrap>"
			if user_is_owner:
				h += """<input type="checkbox" value="%s" name="category_%d" """ % (self.categories[cb], cb + 1)
				if self.category_values()[cb] != "" and self.category_values()[cb] != None:
					h += " checked "
				h += ">%s" % (self.categories[cb])
			else:
				if self.category_values()[cb] != "" and self.category_values()[cb] != None:
					h += " &radic; "
				else:
					h += " &nbsp; "
				h += "%s" % (self.categories[cb])

			h += "</td>"
			if i % 2 == 0:
				h += "</tr>"
		h += "</table>"
		return h
		
	def category_values(self):
		return [self.category_01,
				self.category_02,
				self.category_03,
				self.category_04,
				self.category_05,
				self.category_06,
				self.category_07,
				self.category_08,
				self.category_09,
				self.category_10,
				self.category_11,
				self.category_12,
				self.category_13,
				self.category_14,
				self.category_15,
				self.category_16,
				self.category_17,
				self.category_18,
				self.category_19,
				self.category_20,
				self.category_21,
				self.category_22,
				self.category_23,
				self.category_24,
				self.category_25,
				self.category_26,
				self.category_27,
				self.category_28,
				self.category_29,
				self.category_30,
				self.category_31,
				self.category_32,
				self.category_33,
				self.category_34
				]

	categories = ['Academic and School issues',
					'Acculturation/Immigration',
					'Affectionate communication',
					'Applied research/practice', 
					'Attachment',
					'Biological correlates',
					'Bridging theories',
					'Child abuse and neglect',
					'Clinical practice',
					'Corporal punishment',
					'Developmental problems',
					'Ethnicity',
					'Evolutionary perspective',
					'Family interaction',
					'Family violence (other than child abuse & neglect)',
					'Father love',
					'Gender/Gender differences',
					'Intimate partner',
					'Law/legal/courts',
					'Lifespan perspective',
					'Methodological issues',
					'Normal growth and development',
					'Ostracism/Social exclusion',
					'Overview (summary of existing research)',
					'Parenting education',
					'Peer and sibling acceptance-rejection',
					'Psychological & behavioral adjustment & maladjustment',
					'Psychological & behavioral control',
					'Rejection sensitivity',
					'Research (other)',
					'Resilience, and Coping with rejection',
					'Sociocultural correlates of acceptance-rejection',
					'Substance abuse',
					'Teacher acceptance-rejection']

	def get_sub_projectsXXXXXXX(self):
		sub_projects = SubProject.all()
		sub_projects.filter("project =", self.key())
		
		h = "<table border=0>"
		h += "<tr>"
		i = 0
		for cb in range(0, len(self.categories)):
			if i % 2 == 0:
				h += "<tr>"
			i += 1

			h += "<td nowrap>"
			if user_is_owner:
				h += """<input type="checkbox" value="%s" name="category_%d" """ % (self.categories[cb], cb + 1)
				if self.category_values()[cb] != "" and self.category_values()[cb] != None:
					h += " checked "
				h += ">%s" % (self.categories[cb])
			else:
				if self.category_values()[cb] != "" and self.category_values()[cb] != None:
					h += " &radic; "
				else:
					h += " &nbsp; "
				h += "%s" % (self.categories[cb])

			h += "</td>"
			if i % 2 == 0:
				h += "</tr>"
		h += "</table>"
		return h
	
	def get_sub_projects(self):
		subprojects = SubProject.all()
		subprojects.filter("project =", self)
		return subprojects
		
class SubProject(db.Model):
	name_of_subproject		= db.StringProperty()
	project					= db.ReferenceProperty(Project)
	subproject_owner		= db.UserProperty()
