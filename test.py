from pprint import pprint


def get_unique():
    """Подсчет элементов"""
    list_version = [['665587', 2], ['669532', 1], ['669537', 2],
                    ['669532', 1], ['665587', 1], ['665587', 2],
                    ['669537', 2]]
    unique_list = []
    for element in list_version:
        if element not in unique_list:
            unique_list.append(element)
    for unique_element in unique_list:
        unique_element.append(list_version.count(unique_element))
    return unique_list


print(get_unique())


def json_diff():
    """Сравнение двух Json"""
    json_old = {'company_id': 111111, 'resource': 'record',
                'resource_id': 406155061, 'status': 'create',
                'data': {'id': 11111111, 'company_id': 111111, 'services': [
                    {'id': 9035445, 'title': 'Стрижка', 'cost': 1500,
                     'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}],
                         'goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'},
                         'client': {'id': 130345867, 'name': 'Клиент', 'phone': '79111111111',
                                    'success_visits_count': 2, 'fail_visits_count': 0}, 'clients_count': 1,
                         'datetime': '2022-01-25T11:00:00+03:00', 'create_date': '2022-01-22T00:54:00+03:00',
                         'online': False, 'attendance': 0, 'confirmed': 1, 'seance_length': 3600, 'length': 3600,
                         'master_request': 1, 'visit_id': 346427049, 'created_user_id': 10573443, 'deleted': False,
                         'paid_full': 0, 'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '',
                         'date': '2022-01-22 10:00:00'}}
    json_new = {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create',
                'data': {'id': 11111111, 'company_id': 111111, 'services': [
                    {'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500,
                     'amount': 1}], 'goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'},
                         'client': {'id': 130345867, 'name': 'Клиент', 'phone': '79111111111',
                                    'success_visits_count': 2, 'fail_visits_count': 0}, 'clients_count': 1,
                         'datetime': '2022-01-25T13:00:00+03:00', 'create_date': '2022-01-22T00:54:00+03:00',
                         'online': False, 'attendance': 2, 'confirmed': 1, 'seance_length': 3600, 'length': 3600,
                         'master_request': 1, 'visit_id': 346427049, 'created_user_id': 10573443, 'deleted': False,
                         'paid_full': 1, 'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '',
                         'date': '2022-01-22 10:00:00'}}
    diff_list = ['services', 'staff', 'datetime']
    result = {}
    #  не совсем понятно, меняться могут данные только в data
    #  или любые. Есди только в data, то первого цикла
    #  в решении не было бы.
    for key in json_old.keys():
        if json_old[key] != json_new[key] and key != 'data':
            result[key] = json_new[key]
    for key, value in json_new['data'].items():
        if key in diff_list and value != json_old['data'][key]:
            result[key] = value

    return result


pprint(json_diff())
