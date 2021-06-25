import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = f"https://api.vk.com/method/users.get?fields=sex,about&access_token={response['access_token']}&v=5.131"

    vk_response = requests.get(api_url)
    if vk_response.status_code != 200:
        return

    if response['email']:
        user.email = response['email']

    vk_data = vk_response.json()['response'][0]

    if vk_data['sex']:
        if vk_data['sex'] == 1:
            user.userprofile.gender = UserProfile.FEMALE
        elif vk_data['sex'] == 2:
            user.userprofile.gender = UserProfile.MALE
        else:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

    if vk_data['about']:
        user.userprofile.about_me = vk_data['about']

    user.save()
