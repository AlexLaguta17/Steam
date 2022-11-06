from games.api.v1.serializers import ApplicationSerializer, LibrarySerializer
from games.models import Application, Library


def get_user_apps(input_data):
    library = Library.objects.all().filter(user_id=input_data.get('user_id'))
    if input_data.get('asc_app_name')==True and input_data.get('desc_app_time')==True:
        return None
    if input_data.get('asc_app_name'):
        library = library.order_by('application__name')
    if input_data.get('desc_app_time'):
        library = library.order_by('-app_time')
    return library


def get_top_user_apps(input_data):
    library = Library.objects.all().filter(user_id=input_data)
    library = library.order_by('-app_time', '-last_launch')[:3]
    if library:
        return library
    else:
        return None
