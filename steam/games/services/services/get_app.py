from games.models import Application


def get_app(input_data):
    output_data = Application.objects.all()
    if 'app_name' in input_data:
        output_data = output_data.filter(name=input_data.get('app_name'))
        return output_data
    if 'category' in input_data:
        output_data = output_data.filter(category=input_data.get('category'))
    if 'price_from' in input_data:
        output_data = output_data.filter(price__gte=input_data.get('price_from'))
    if 'price_to' in input_data:
        output_data = output_data.filter(price__lte=input_data.get('price_to'))
    if input_data.get('asc'):
        output_data = output_data.order_by('price')
    return output_data
