from django.apps import AppConfig


class FindtutorsConfig(AppConfig):
    name = 'FindTutors'

    def ready(self):
        import FindTutors.signals