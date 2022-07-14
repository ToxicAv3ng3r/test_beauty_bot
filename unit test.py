from unittest import TestCase


test_text = ('{name}, ваша запись изменена: '
             '{day_month} в {start_time}. {master}. '
             'Услуги: {services}. '
             'Управление записью {record_link}')
list_keys = ['name', 'day_month', 'day_of_week',
             'start_time', 'end_time', 'master', 'services']


class Test(TestCase):
    def test(self):
        """Проверка правильности текста"""
        for variable in list_keys:
            exp_reg = r'{' + variable + r'}'
            self.assertRegex(test_text,
                             exp_reg,
                             msg=f'В тексте нет {variable}')
