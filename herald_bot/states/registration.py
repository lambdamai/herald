from herald_bot.handlers.core.state import BaseState as State
from herald_bot.models import User
from herald_bot.utils import is_group_exist

languages = [language[1] for language in User.languages]


class ChooseGroupState(State):
    def on_enter(self, trigger):
        trigger.send_message('Напишите, из какой вы группы')

    def on_trigger(self, trigger):
        if is_group_exist(trigger.text, trigger.get_user()):
            trigger.send_message('Регистрация успеша, мы вас запомнили')
            return
        else:
            trigger.send_message('Такой группы не существует')
            return ChooseGroupState()


class ChooseLanguageState(State):
    def on_enter(self, trigger):
        trigger.send_keyboard('Выберите язык из списка', languages)

    def on_trigger(self, trigger):
        if trigger.text in languages:
            user = trigger.get_user()
            user.language = languages.index(trigger.text)
            user.save()
            return ChooseGroupState()
        else:
            trigger.send_message('Некорректный язык')
            return ChooseLanguageState()
