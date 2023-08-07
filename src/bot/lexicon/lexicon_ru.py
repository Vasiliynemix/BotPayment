class BotMainMenuLexicon:
    def __init__(self):
        self.MAIN_MENU_COMMANDS: dict[str, str] = {
            '/help': 'Описание команды хелп',
        }


class Lexicon:
    menu: BotMainMenuLexicon = BotMainMenuLexicon()


lexicon = Lexicon()
