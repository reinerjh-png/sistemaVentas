import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_ventas.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "reiner"
email = "reinerjj11@gmail.com"
password = "1974"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("✅ Superusuario creado correctamente.")
else:
    print("⚠️ El superusuario ya existe.")
