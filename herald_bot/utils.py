from herald_bot.models import StudyGroup
import requests

URL_TEMPLATE = 'https://mai.ru/education/schedule/data/{}.txt'


def _is_exist_on_site(group_name):
    result = requests.get(URL_TEMPLATE.format(group_name))
    if result.status_code == 404:
        return False
    else:
        return True


def is_group_exist(group_name, user):
    exist_in_db = StudyGroup.objects.filter(name=group_name)
    if not exist_in_db:
        exist_on_site = _is_exist_on_site(group_name)
        if not exist_on_site:
            return False
        new_group = StudyGroup(name=group_name)
        new_group.save()
        user.group_name = new_group
        user.save()
        return True
    else:
        user.group_name = exist_in_db[0]
        user.save()
        return True
