import unittest

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

geo_rus_list = [{'visit1': ['Москва', 'Россия']},
                {'visit3': ['Владимир', 'Россия']},
                {'visit7': ['Тула', 'Россия']},
                {'visit8': ['Тула', 'Россия']},
                {'visit9': ['Курск', 'Россия']},
                {'visit10': ['Архангельск', 'Россия']}]

geo_rus_list_test = []


def geo_logs_rus(data_list):
    for list_ in data_list:
        for key, value in list_.items():
            if value[1] == 'Россия':
                geo_rus_list_test.append(list_)
    return geo_rus_list


class Test_logs(unittest.TestCase):
    def test_geo_logs_rus(self):
        self.assertEqual(geo_logs_rus(geo_logs), geo_rus_list_test)


if __name__ == '__main__':
    unittest.main()