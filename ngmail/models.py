from django.db import models
from django.utils import timezone
from django.db.models import Q


def shorten_string(s, slen):
    if len(s) > slen:
        return s[:slen]+'...'
    else:
        return s


class NGMessageFolder(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    @classmethod
    def get_folder_by_name(cls, folder):
        if not folder:
            return None
        try:
            return NGMessageFolder.objects.get(name__iexact=folder)
        except NGMessageFolder.DoesNotExist:
            return None


class NGUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices=(('male', 'мужской'), ('female', 'женский')))
    address = models.CharField(max_length=100)
    email = models.EmailField()
    avatar_url = models.CharField(max_length=200)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name,)

    @classmethod
    def get_user_by_id(cls, uid):
        if not uid:
            return None
        try:
            return NGUser.objects.get(id=uid)
        except NGUser.DoesNotExist:
            return None


class NGMessage(models.Model):
    sender = models.ForeignKey(NGUser, related_name='sender')
    recipient = models.ForeignKey(NGUser, related_name='recipient')
    date_and_time = models.DateTimeField(default=timezone.now)
    text = models.TextField(null=True)
    folder = models.ForeignKey(NGMessageFolder)

    MESSAGE_NAME_DISPLAY_LENGTH = 70

    def __str__(self):
        res = '[' + shorten_string(self.sender.__str__(), 30) + ']'
        res += '[' + shorten_string(self.text, self.MESSAGE_NAME_DISPLAY_LENGTH) + ']'
        return res

    @classmethod
    def get_message_by_id(cls, uid):
        if not uid:
            return None
        try:
            return NGMessage.objects.get(id=uid)
        except NGMessage.DoesNotExist:
            return None

    @classmethod
    def filter_messages(cls, folderName, user, show_deleted=False):
        qs = NGMessage.objects.filter(folder__name__iexact=folderName).filter(Q(recipient=user) | Q(sender=user))
        if show_deleted:
            qs = qs.filter(sender__deleted=False)
        qs = qs.order_by('-date_and_time')
        return qs
