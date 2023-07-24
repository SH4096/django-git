from django.views import View
from django.http import JsonResponse
from apps.users import models


class UsernameCountView(View):
    def get(self, request, username):
        count = models.User.objects.filter(username=username).count()
        return JsonResponse({'code': 0, 'count': count, 'errors': 'ok'})
