from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class MainUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True,
                                        verbose_name='Оповещения отсылать?')

    class Meta(AbstractUser.Meta):
        pass