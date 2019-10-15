class Template(object):
	def __init__(self, code=1):
		self._code = code

	@staticmethod
	def run():
		return 'Ingesting! Nom nom nom...'

	def public_method(self):
		print(self._code)

	def __private_method(self):
		print(self._code)

	@classmethod
	def class_method(cls):
		print(cls.run())
