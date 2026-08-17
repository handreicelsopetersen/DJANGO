from django.contrib.auth.models import User
user = User.objects.get(username='sup')
print(user.is_superuser)
print(user.is_staff)
print(user.has_perm('receitas.delete_category'))
