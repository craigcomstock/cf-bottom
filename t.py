from tom.bot import Bot
from tom.main import setup_bot
from tom.utils import read_json
from tom.reports import Reports

config = read_json("config.json")
secrets = read_json("cfengine-secrets.json")
bot_data = config["bots"][0]
bot_data["secrets_data"] = secrets
directory=""
interactive=True
reports=Reports("")
bot = setup_bot(directory, interactive, bot_data, reports)
bot.handle_pull_url("https://api.github.com/repos/cfengine/core/pulls/4992")
#bot.handle_pull_url("https://github.com/cfengine/documentation/pull/2772")
