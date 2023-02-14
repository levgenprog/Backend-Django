import random
from typing import Protocol, OrderedDict
import uuid
from rest_framework_simplejwt import tokens
from django.core.cache import cache 
from django.core.mail import send_mail
from django.conf import settings
from . import repos, models


class UserServicesInterface(Protocol):

    def create_user(self, data: OrderedDict) -> dict:
        ...
    
    def verify_user(self, data: OrderedDict):
        ...

    def create_token(self, data: OrderedDict) -> dict:
        ...
    
    def verify_token(self, data: OrderedDict) -> dict:
        ...

class UserServicesV1:
    user_repos: repos.UserReposInterface = repos.UserReposV1()

    def create_user(self, data: OrderedDict) -> dict:
        session_id = self._verify_phone_number(data)
        return {
            'session_id': session_id,
        }

    def verify_user(self, data: OrderedDict):
        user_data = cache.get(data['session_id'])

        if not user_data or data['code'] != user_data['code']:
            return

        user = self.user_repos.create_user(data={
            'email': user_data['email'],
            'phone_number': user_data['phone_number'],
        })
        self._send_email(email=user.email)



    def create_token(self, data: OrderedDict) -> dict:
        session_id = self._verify_phone_number(data, exists=True)

        return {
            'session_id': session_id,
        }


    def verify_token(self, data: OrderedDict) -> dict:
        session = cache.get(data['session_id'])

        if not session:
            return

        if session['code'] != data['code']:
            return

        user = self.user_repos.get_user(data={'phone_number': session['phone_number']})
        access = tokens.AccessToken.for_user(user=user)
        refresh = tokens.RefreshToken.for_user(user=user)

        return {
            'access': str(access),
            'refresh': str(refresh),
        }

    def _verify_phone_number(self, data: OrderedDict, exists: bool = False) -> str:
        phone_number = data['phone_number']
        if exists:
            user = self.user_repos.get_user(data)
            phone_number = str(user.phone_number)
        code = self._generate_code()
        session_id = self._generate_session_id()
        cache.set(session_id, {'phone_number': phone_number, 'code': code, **data}, timeout=300)
        self._send_sms_to_phone_number(phone_number=data['phone_number'], code=code) 

        return session_id
    

    @staticmethod
    def _generate_code(length: int = 4) -> str:
        numbers = [str(i) for i in range(10)]
        return (''.join(random.choices(numbers, k=length)))

    @staticmethod
    def _generate_session_id() -> str:
        return str(uuid.uuid4())
        
    @staticmethod
    def _send_email(email: str) -> None:
        send_mail(
            subject="Welcome!",
            message="Thank you for the registration!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False 
        )

    @staticmethod
    def _send_sms_to_phone_number(phone_number: str, code: str) -> None:
        print(f"sent code {code} to {phone_number}")