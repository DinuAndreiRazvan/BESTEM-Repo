from send_message import *

send_email('contacts.txt', 'inc_stocks.txt')
send_Wapp_Message('You have received an email ragarding current stocks. Please check your email for more details', 'contacts.txt')
send_sms('You have received an email ragarding current stocks. Please check your email for more details', 'contacts.txt')
