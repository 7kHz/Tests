import unittest

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

total_request_quantity = len(queries)

dct = {}
percent_words_list = []
percent_words_list_test = ['3 слова в запросе составляют 57.1%', '2 слова в запросе составляют 42.9%']


def percent_words(data_queries):
    for query in data_queries:
        count = len(query.split())
        dct[count] = dct.get(count, 0) + 1
    for key in dct:
        percent_of_queries = round((dct[key] / total_request_quantity * 100), 1)
        percent_words_list.append(f'{key} слова в запросе составляют {percent_of_queries}%')
    return percent_words_list


class TestPercentWords(unittest.TestCase):
    def test_percent_words(self):
        self.assertEqual(percent_words(queries), percent_words_list_test)


if __name__ == '__main__':
    unittest.main()