
class TelegramBot(object):

    def __init__(self, token):
        self.token = token

    def bot(self):
        import telegram
        bot = telegram.Bot(token=self.token)
        return bot

    @staticmethod
    def run(value):
        return 'Hello telegram!' + value

    @staticmethod
    def _run():
        return 'Hello telegram!'

    def send_message(self, channel_id, message):
        bot = self.bot()
        bot.send_message(chat_id=channel_id, text=message)

    def send_html_message(self, channel_id, message):
        bot = self.bot()
        bot.send_message(chat_id=channel_id, text=message, parse_mode=telegram.ParseMode.HTML)

    def build_success_msg(self, action, channel_id, message):
        text = '<b>' + action + ' Has Been Successfully</b>\r\n' + message
        self.send_html_message(channel_id, text)

    def build_error_msg(self, action, channel_id, message):
        text = '<b>' + action + ' Failed</b>\r\n'
        text += message
        self.send_html_message(channel_id, text)
