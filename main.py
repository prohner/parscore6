"""
Running Google App Engine locally:

cd /Users/preston/parscore6
python /Applications/google-cloud-sdk/bin/dev_appserver.py app.yaml

"""



#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import operator

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users

from Models.TestModels import *
from Models.ProjectModels import *
from Utils import *

class MainHandler(webapp.RequestHandler):
    def get(self):
		user = users.get_current_user()
		if user:
			tests = TestBase.gql("where score >= 0")##.order('-date_updated')
			path = os.path.join(os.path.dirname(__file__), 'home.html')
			self.response.out.write(template.render(path, { 'tests' : tests,
															'TestBase' : TestBase,
															'signout_url' : Util.get_signout_url(),
															'user' : users.get_current_user() } ))
		else:
			self.redirect("/welcome")

class ScoringMeasuresHandler(webapp.RequestHandler):
    def get(self):
		user = users.get_current_user()
		if user:
			tests = TestBase.gql("where score >= 0")##.order('-date_updated')
			path = os.path.join(os.path.dirname(__file__), 'scoring.html')
			self.response.out.write(template.render(path, { 'tests' : tests,
                                                            'TestBase' : TestBase,
                                                            'signout_url': Util.get_signout_url(),
                                                            'is_development' : os.environ['SERVER_SOFTWARE'].startswith('Development')
                                                            } ))
		else:
			self.redirect("/welcome")

class LoginHandler(webapp.RequestHandler):
	def get(self):
		path = os.path.join(os.path.dirname(__file__), 'welcome.html')
		self.response.out.write(template.render(path, { 'login_url' : users.create_login_url("/") } ))

class AddSubProjectHandler(webapp.RequestHandler):
	def get(self):
		project = Project.get(self.request.get("project_key"))
		subproject = SubProject(name_of_subproject = self.request.get("subproject_name"),
								project = project,
								subproject_owner = users.get_current_user()
								)
		subproject.put()
		self.redirect("/choose-project?test_name=%s" % self.request.get("test_name"))

class ChooseProjectHandler(webapp.RequestHandler):
	def get(self):
		projects = Project.all()
		projects.filter("project_owner =", users.get_current_user())
		projects.filter("permission_granted =", "Yes")
		#for project in projects:
		#	subs = SubProject.all()
		#	subs.filter("project = ", project.key())

		path = os.path.join(os.path.dirname(__file__), 'choose_project.html')
		self.response.out.write(template.render(path, { 'projects' : projects,
														'test_name' : self.request.get('test_name')
														} ))


class ShowTestHandler(webapp.RequestHandler):
	def get(self):
		projects = Project.all()
		projects.filter("project_owner =", users.get_current_user())
		projects.filter("permission_granted =", "Yes")
		if projects.count() == 0:
			self.redirect("/list-projects?m=All questionnaires must be part of a project that has consent to share.  Please Add Project for the questionnaires.")

		t = TestBase.get_test(self.request.get("test_name"), self.request.get("key"))

		subprojects = SubProject.all()
		subprojects.filter("subproject_owner =", users.get_current_user())

		selected_project_key = self.request.get("project")
		selected_subproject_key = self.request.get("subproject")
		selected_project = None
		selected_subproject = None

		if t.is_saved() == False:
			t.test_id = "%s" % (t.get_test_id_number())
			if len(selected_project_key) > 0:
				selected_project = Project.get(selected_project_key)
				t.project = selected_project
			if len(selected_subproject_key) > 0:
				selected_subproject = SubProject.get(selected_subproject_key)
				t.subproject = selected_subproject

		if selected_project == None:
			selected_project = t.project
			selected_subproject = t.subproject

		can_edit_test = False
		if not self.request.get("key"):
			t.test_owner 	= users.get_current_user()
			can_edit_test	= True

		if self.request.get("redo") == "y":
			can_edit_test	= True

		t.put()

		user = users.get_current_user()
		path = os.path.join(os.path.dirname(__file__), 'test_form.html')

		self.response.out.write(template.render(path, { 't' : t,
		 												'h' : t.test_as_html_table(can_edit_test),
		 												'user' : users.get_current_user(),
														'signout_url' : Util.get_signout_url(),
														'projects' : projects,
														'subprojects' : subprojects,
														'can_edit_test' : can_edit_test,
														'selected_project' : selected_project,
														'selected_subproject' : selected_subproject } ))

class SaveTestHandler(webapp.RequestHandler):
    def get(self):
		t = TestBase.get_test(self.request.get("test_name"), self.request.get("key"))

		if self.request.get('relationship'):
			t.relationship = self.request.get('relationship')

		if len(self.request.get('project_key')) > 5:
			project = Project.get(self.request.get('project_key'))
			if project:
				t.project = project

		if len(self.request.get('subproject_key')) > 5:
			subproject = SubProject.get(self.request.get('subproject_key'))
			if subproject:
				t.subproject = subproject

		t.store_form(self.request)
		validation_messages = t.validate()
		if not validation_messages:
			t.get_score()
			t.put()
			self.redirect("""/show-test?test_name=%s&key=%s""" % (self.request.get("test_name"), self.request.get("key")))
		else:
			self.response.out.write("<br />%s<br />" % validation_messages)

		#path = os.path.join(os.path.dirname(__file__), 'test_form.html')
		#self.response.out.write(template.render(path, { 't' : t,
		# 												'h' : t.test_as_html_table(False),
		# 												'user' : users.get_current_user(),
		# 												'validation_messages' : validation_messages} ))

class ListTestsHandler(webapp.RequestHandler):
	def get(self):
		tests = TestBase.all()

		if not users.is_current_user_admin():
			tests.filter("test_owner =", users.get_current_user())

		if self.request.get("p"):
			tests.filter("project = ", Project.get(self.request.get("p")))
		else:
			tests.filter("test_name =", self.request.get("test_name"))
			#tests.order("-date_updated")

		if self.request.get("test_name").find("PPQ") < 0:
			tests.filter("score >", 0)

		path = os.path.join(os.path.dirname(__file__), 'list_tests.html')
		self.response.headers['Cache-Control'] = 'no-store'
		self.response.headers['Cache-Control'] = 'no-cache'
		self.response.headers['Pragma'] = 'no-store'
		self.response.headers.add_header("Expires", "Thu, 01 Dec 1994 16:00:00 GMT")
		self.response.out.write(template.render(path, { 'tests' : tests, 'signout_url': Util.get_signout_url(), 'user' : users.get_current_user() } ))

class ShowProjectHandler(webapp.RequestHandler):
	def get(self):
		if self.request.get("key"):
			p = Project.get(self.request.get("key"))
		else:
			p = Project()
			p.project_owner = users.get_current_user()
			p.has_been_saved = "No"
			p.put()
		user_is_owner = p.project_owner == users.get_current_user()
		#user_is_owner = False

		if user_is_owner:
			path = os.path.join(os.path.dirname(__file__), 'project.html')
		else:
			path = os.path.join(os.path.dirname(__file__), 'project_readonly.html')

		self.response.out.write(template.render(path, { 'project' : p,
											'signout_url': Util.get_signout_url(),
											'user' : users.get_current_user(),
											'tb' : TestBase,
											'category_checkboxes' : p.get_category_checkboxes(user_is_owner),
											'measures_checkboxes' : p.get_measures_checkboxes(user_is_owner) } ))

class SaveProjectHandler(webapp.RequestHandler):
	def post(self):
		if self.request.get("key"):
			p = Project.get(self.request.get("key"))
		else:
			p = Project()
		p.store_form(self.request)
		p.has_been_saved = "Yes"
		p.put()
		##self.response.out.write("Hello from the handlers")
		self.redirect("/list-projects")

class DownloadHandler(webapp.RequestHandler):
	def get(self):
		project = Project.get(self.request.get("p"))
		test_name = self.request.get("n")
		filename = project.project_title + '_' + test_name + '.txt'
		filename = filename.replace('/', '_').replace(',', '_').replace(' ', '_').replace(':', '_').replace('\\', '_').replace('__', '_')

		tests = TestBase.all()
		tests.filter("project = ", project)
		tests.filter("test_name = ", test_name)
		# self.response.out.write(tests.count())

		line_terminator = "<br/>"
		if self.request.get("dnld") != "n":
			self.response.headers['Content-Type'] = 'text'
			self.response.headers['Content-Disposition'] = "attachment; filename=" + filename
			line_terminator = "\n"
		t = tests[0]

		self.response.out.write(t.get_download_header() + line_terminator)
		self.response.out.write(t.get_download_testname() + line_terminator)
		for t in tests:
			self.response.out.write(t.get_download_line() + line_terminator)


class DownloadChooserHandler(webapp.RequestHandler):
	def get(self):
		all_tests = TestBase.all()
		project = Project.get(self.request.get("p"))
		all_tests.filter("project = ", project)

		test_names = dict( {} )
		for test in all_tests:
			if test.test_name in test_names:
				test_names[test.test_name] = test_names[test.test_name] + 1
			else:
				test_names[test.test_name] = 1

		#tests = test_names
		#test_name_seq = test_names.keys()
		#test_name_seq.sort()
		#test_names2 = [test_names[key] for key in test_name_seq]
		keys = test_names.keys()
		keys.sort()
		tests = []
		for key in keys:
			tests.append([key, test_names[key]])
		#tests = sorted(test_names.iteritems(), key=operator.itemgetter(1))

		path = os.path.join(os.path.dirname(__file__), 'choose_download.html')
		self.response.out.write(template.render(path, { 'test_names' : tests,
		 												'project' : project,
		 												'is_development' : os.environ['SERVER_SOFTWARE'].startswith('Development') } ))

class ListProjectsHandler(webapp.RequestHandler):
	def get(self):
		projects = Project.all()
		projects.filter("has_been_saved =", "Yes")

		if self.request.get("s") == "1":
			projects.order("name_of_researcher")
		elif self.request.get("s") == "2":
			projects.order("project_title")
		elif self.request.get("s") == "3":
			projects.order("city")
		elif self.request.get("s") == "4":
			projects.order("province")
		elif self.request.get("s") == "5":
			projects.order("country")
		elif self.request.get("s") == "6":
			projects.order("affiliated_institution")
		elif self.request.get("s") == "7":
			projects.order("language_used")
		elif self.request.get("s") == "8":
			projects.order("project_owner")
		elif self.request.get("s") == "9":
			projects.order("-date_updated")

		#projects.filter("project_owner =", users.get_current_user())
		if users.is_current_user_admin():
			is_admin_user = 1
		else:
			is_admin_user = 0

		path = os.path.join(os.path.dirname(__file__), 'list_projects.html')
		self.response.headers['Cache-Control'] = 'no-store'
		self.response.headers['Cache-Control'] = 'no-cache'
		self.response.headers['Pragma'] = 'no-store'
		self.response.headers.add_header("Expires", "Thu, 01 Dec 1994 16:00:00 GMT")
		self.response.out.write(template.render(path, { 'projects' : projects,
														'signout_url': Util.get_signout_url(),
														'msg' : self.request.get("m"),
														'user' : users.get_current_user(),
														'is_admin_user' : is_admin_user } ))

class HelpHandler(webapp.RequestHandler):
	def get(self):
		path = os.path.join(os.path.dirname(__file__), 'help/help.html')
		self.response.out.write(template.render(path, {} ))

class HelpVideoHandler(webapp.RequestHandler):
	def get(self):
		path = os.path.join(os.path.dirname(__file__), 'help/video.html')
		self.response.out.write(template.render(path, {} ))


def main():
    application = webapp.WSGIApplication([('/', MainHandler),
											('/scoring', ScoringMeasuresHandler),
											('/choose-project', ChooseProjectHandler),
											('/add_sub_project', AddSubProjectHandler),
											('/show-test', ShowTestHandler),
											('/save-test', SaveTestHandler),
											('/list-test', ListTestsHandler),
											('/show-project', ShowProjectHandler),
											('/save-project', SaveProjectHandler),
											('/list-projects', ListProjectsHandler),
											('/download-chooser', DownloadChooserHandler),
											('/download-set', DownloadHandler),
											('/help', HelpHandler),
											('/video', HelpVideoHandler),
											('/welcome', LoginHandler)
											],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
