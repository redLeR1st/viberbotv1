from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

import keys

print(keys.AUTH_API_KEY)

bot_configuration = BotConfiguration(
	name='PythonSampleBot',
	avatar='http://viber.com/avatar.jpg',
	auth_token=keys.AUTH_API_KEY
)
viber = Api(bot_configuration)

# main()