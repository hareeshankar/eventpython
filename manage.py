#!/usr/bin/env python
import os
import sys
from django.contrib.auth import get_user_model; 

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
    User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password1')
