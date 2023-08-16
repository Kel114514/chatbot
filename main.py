from pycqBot import cqHttpApi, cqLog

cqLog()

cqapi = cqHttpApi()
bot = cqapi.create_bot()
bot.start()