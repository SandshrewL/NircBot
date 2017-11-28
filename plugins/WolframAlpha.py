import urllib.request
import urllib.parse
import logging


class WolframAlpha():
    api = "http://api.wolframalpha.com/v2/query?input={}&appid={}"
    appId = ""
    name = "WolframAlpha"
    commands = ['w', 'wa']

    def _apiFetch(self, userInput):
        apiRequest = urllib.request.Request(
            self.api.format(input, self.appId))
        try:
            apiResonse = urllib.request.urlopen(apiRequest).read()
        except urllib.error.URLError:
            return False
        else:
            if "Appid missing" in str(apiResonse):
                logging.error("The WolframAlpha plugin requires a valid AppId.")
                return False
            else:
                return apiResonse

    def command(self, bot=None, command=None, arguments=None,
                nick=None, channel=None, ident=None, host=None):
        if not arguments:
            bot.say(channel, "Incorrect usage. '{} <value>''".format(command))
        else:
            args = ''.join(arguments)
            apiData = self._apiFetch(arguments)
            if apiData == False:
                bot.say(channel, "Error, please look at the console.")
            else:
                print(apiData)

    def loadSettings(self, settings, **args):
        self.api = settings['api']
