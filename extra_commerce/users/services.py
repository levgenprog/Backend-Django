from typing import Protocol, OrderedDict
from . import repos


class UserServicesInterface(Protocol):

    def create_user(self, data: OrderedDict) -> None:
        ...

class UserServicesV1:
    user_repos: repos.UserReposInterface = repos.UserReposV1()

    def create_user(self, data: OrderedDict) -> None:
        user = self.user_repos.create_user(data=data)
        self._send_email(email_txt=user.email)

    @staticmethod
    def _send_email(email_txt: str) -> None:
        print(f'sent {email_txt}')