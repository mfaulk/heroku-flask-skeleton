""" Configuration patterned after https://realpython.com/blog/python/flask-by-example-part-1-project-setup/
"""

class Config(object):
	DEBUG = True
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'too-many-secrets'

class ProductionConfig(Config):
	DEBUG = False

class StagingConfig(Config):
	DEVELOPMENT = True
	DEBUG = True

class DevelopmentConfig(Config):
	DEVELOPMENT = True
	DEBUG = True
