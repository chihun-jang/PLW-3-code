#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
    # default로 사용할 Django Settings의 경로를 변경해주었습니다
    # 프로젝트 설정 폴더 이름도 config로 바꾸어 주었고 settings 폴더 밑에 dev를 위치시켰으므로
    # 다음과 같이 표현된 것을 확인할 수 있습니다
    
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
