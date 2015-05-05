from google.appengine.ext import webapp 
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail

from models import DataStoreManager

class LogSenderHandler(InboundMailHandler):
    # Receiving new mail message and parsing it
    def receive(self, mail_message):                                                                                                                      
        manager = DataStoreManager()
        instance = manager.get_instance_by_email(mail_message.sender.lowercase())

        email_key = manager.store_email(instance, instance.user, mail_message, mail_message.attachments)
