from django.core.mail import EmailMultiAlternatives
from html2text import html2text

class AutoTextMail(EmailMultiAlternatives):
	'''
	see ``EmailMultiAlternatives`` documentation on the django website for 
	options

	'''
	def __init__(self, subject='', body='', from_email=None, to=None, bcc=None,
		connection=None, attachments=None, headers=None, alternatives=None,
		cc=None):
		text_body = html2text(body)
		super(AutoTextMail, self).__init__(
			''.join(subject.splitlines()), #no line here !!!!
			text_body, 
			from_email, to, bcc, 
			connection, 
			attachments, 
			headers, 
			alternatives, 
			cc
			)
		self.attach_alternative(body,"text/html")
