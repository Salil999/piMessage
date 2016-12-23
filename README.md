# piMessage
### Description
This python module is a simple wrapper for AppleScript to be used in python scripts. It can send iMessages and SMS messages programatically - nothing special. Decided to release it since a few people were asking for it.

### Requirements
__Absolutely none!__ However, since this is in AppleScript, it's obvious you have to have a Macintosh machine to use it.

### Example
```python
import piMessage
number = '18004567890'
msg = 'Hello World!'
sendSMS(number, msg) # this will send a text message
sendiMessage(number, msg) # this will send an iMessage
```
Each method will return ```True``` on success and ```False``` on failure.
