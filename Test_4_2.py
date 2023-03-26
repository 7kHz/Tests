import unittest

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
number_list = []
ids_set = {98, 35, 15, 213, 54, 119}


def unique_ids(ids_data):
    for key, value in ids_data.items():
        for number in value:
            number_list.append(number)
    return set(number_list)


class TestUniqueIds(unittest.TestCase):
    def test_ids(self):
        self.assertEqual(unique_ids(ids), ids_set)


if __name__ == '__main__':
    unittest.main()
