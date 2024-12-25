from main.models import Banner

class Services():
    @staticmethod
    def services_func_id():
        return Banner.objects.latest("id")