from herald_bot.handlers.core.state import BaseState as State
from .registration import ChooseLanguageState as StartState


class BootStrapState(State):
    def on_trigger(self, trigger):
        # TODO уточнить насчет заведомого создания пользователя
        trigger.create_user()
        return StartState()
