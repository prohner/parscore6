from google.appengine.api import users

class Util(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		
	@staticmethod
	def get_signout_url():
		return "<a href=\"%s\">%s, Sign out </a>" % (users.create_logout_url("/"), users.get_current_user().nickname())		
		