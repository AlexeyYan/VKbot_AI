import vk
import apiai, json
import time
import config
session=vk.Session(config.token)
api = vk.API(session)

def Bot() :
 notread=api.messages.get(cout=1,filters=1)
 if (notread[0] ==0):
  time.sleep(3)
 else:
  msg=notread[1]
  uid=msg['uid']
  msg=msg['body']


  request=apiai.ApiAI(config.ai_token).text_request()
  request.lang='ru'
  request.session_id='MyVKbot'
  request.query=msg

  responseJson=json.loads(request.getresponse().read().decode('utf-8'))
  response=responseJson['result']['fulfillment']['speech']
 
  if response:
    api.messages.send(user_id=uid, chat_id=uid, message=response)
  else:
    api.messages.send(user_id=uid, chat_id=uid, message="Прости, я тебя не понял")

while (True):
 Bot();
 time.sleep(3)
 
