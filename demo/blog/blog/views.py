import json
import random
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse


def create_user(request, *args, **kwargs):
    for i in range(10000):
        User.objects.create(
            username="test{}".format(i),
            password=make_password('1qaz1qaz'),
            is_superuser=0,
            email="test{}@xuetangx.com".format(i),
            is_staff=1,
            is_active=1
        )

    return HttpResponse(json.dumps({"status": "ok"}), content_type="text/json")


def get_user(request, *args, **kwargs):
    user = User.objects.filter(username="test{}".format(random.randint(0, 100))).first()

    return HttpResponse(json.dumps({"status": "ok", "email": user.email}), content_type="text/json")
