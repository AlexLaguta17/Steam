from django.db.models import Min

from account.models import Inventory
from games.models import Item


def get_user_inventory(input_data):
    output_data = Inventory.objects.filter(item__application_id=input_data.get('app_id'),
                                           user_id=input_data.get('user_id'))
    return output_data


def get_active_lots(input_data):
    output_data = Inventory.objects.filter(user_id=input_data.get('user_id'), is_on_sale=True, item__is_sellable=True)
    return output_data


def get_selling_items(input_data):
    items = Item.objects.filter(Inventories__is_on_sale=True, is_sellable=True).distinct()
    if 'item_name' in input_data:
        items = items.filter(name__contains=input_data.get('item_name'))
    if 'app_id' in input_data:
        items = items.filter(application=input_data.get('app_id'))
    if 'price_from' in input_data:
        items = items.filter(Inventories__price__gte=input_data.get('price_from'))
    if 'price_to' in input_data:
        items = items.filter(Inventories__price__lte=input_data.get('price_to'))
    output_data = []
    for item in items:
        output_data.append({'item': item, 'amount': _get_items_amount(item), 'min_price': _get_item_price(item)})
    return output_data


def _get_items_amount(item):
    amount = Inventory.objects.filter(is_on_sale=True, item__is_sellable=True, item_id=item.id).count()
    return amount


def _get_item_price(item):
    price = Inventory.objects.filter(is_on_sale=True, item__is_sellable=True, item_id=item.id).aggregate(Min('price'))
    return price['price__min']
