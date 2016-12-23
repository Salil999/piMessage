# piMessage
### Description
This python module is a simple wrapper for AppleScript to be used in python scripts. It can send iMessages and SMS messages programatically - nothing special. Decided to release it since a few people were asking for it.

### Requirements
~~__Absolutely none!__~~ Apparently, you have to have the Messages app open. Initially using the script will just launch the Messages app, but it leaves it in an unstable state. Just ensure the Messages app is running in the background when using this module.

### Example
```python
import piMessage
number = '18004567890'
msg = 'Hello World!'
sendSMS(number, msg) # this will send a text message
sendiMessage(number, msg) # this will send an iMessage
```
Each method will return ```True``` on success and ```False``` on failure.
