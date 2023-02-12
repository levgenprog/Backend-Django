from typing import Protocol, OrderedDict
from rest_framework_simplejwt import tokens
from . import repos


class UserServicesInterface(Protocol):

    def create_user(self, data: OrderedDict) -> None:
        ...

    def create_token(self, data: OrderedDict) -> dict:
        ...

class UserServicesV1:
    user_repos: repos.UserReposInterface = repos.UserReposV1()

    def create_user(self, data: OrderedDict) -> None:
        user = self.user_repos.create_user(data=data)
        self._send_email(email_txt=user.email)

    @staticmethod
    def _send_email(email_txt: str) -> None:
        print(f'sent {email_txt}')

    def create_token(self, data: OrderedDict) -> dict:
        user = self.user_repos.get_user(data=data)

        access = tokens.AccessToken.for_user(user=user)
        refresh = tokens.RefreshToken.for_user(user=user)

        return {
            'access': str(access),
            'refresh': str(refresh),
        }
    