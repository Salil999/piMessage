import os

def sendiMessage(number, message):
	msg = """osascript<<END

	tell application "Messages"
	
	send "{}" to buddy "{}" of (service 1 whose service type is iMessage)
	
	end tell

	END""".format(message, number)
	try:
		os.system(msg)
		return True
	except Exception as e:
		print(e)
		return False

def sendSMS(number, message):
	msg = """osascript<<END
	
	tell application "Messages"

	send "{}" to buddy "{}" of service "SMS"

	end tell

	END""".format(message, number)
	try:
		os.system(msg)
		return True
	except Exception as e:
		print(e)
		return False
