class ParsedMethod(object):
	METHOD_NAME_TAG = "h4"
	METHOD_DESCRIPTION_TAG = "div"
	ANCHOR_TAG = 'a'


	def __init__(self, method, anchor, file_path):
		self.anchor = ""
		self.name = method.find(self.METHOD_NAME_TAG).get_text(' ', strip=True)
		self.description = list()
		self.set_description(method)
		self.set_anchor(anchor, file_path)

	def set_description(self, method):
		"""
			Each method may habe more than one description.
		"""
		self.description.clear()
		for method_description in method.findAll(self.METHOD_DESCRIPTION_TAG):
			self.description.append(method_description.get_text(' ', strip=True))
	
	def set_anchor(self, anchor, file_path):
		"""
			Gets the anchor to the method javadoc.
		""" 
		self.anchor = "file://" + file_path + "#" + anchor
