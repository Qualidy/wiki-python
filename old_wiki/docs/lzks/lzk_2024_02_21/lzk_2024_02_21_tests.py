from unittest import TestCase
from lzk_2024_02_21_solutions import *
from unittest import main
main(argv=[''], verbosity=1, exit=False)

class TestRemove(TestCase):

    def test_remove_float_and_int_keys_0(self):
        self.assertIsInstance(remove_float_and_int_keys({'h': 1, 4: 2, 2.0: "e"}), dict)

    def test_remove_float_and_int_keys_1(self):
        self.assertDictEqual(remove_float_and_int_keys({'h': 1, 4: 2, 2.0: "e"}), {'h': 1})

    def test_remove_float_and_int_keys_2(self):
        self.assertDictEqual(remove_float_and_int_keys({'h': 1, '4': 2, '2.0': "e"}), {'h': 1, '4': 2, '2.0': "e"})

    def test_remove_float_and_int_keys_3(self):
        self.assertDictEqual(remove_float_and_int_keys({5: 1, 4: 2, 2.0: "e"}), dict())

    def test_remove_float_and_int_keys_4(self):
        self.assertDictEqual(remove_float_and_int_keys(dict()), dict())

    def test_remove_float_and_int_keys_5(self):
        my_dict = {'h': 1, 4: 2, 2.0: "e"}
        _ = remove_float_and_int_keys(my_dict)
        self.assertDictEqual(my_dict, my_dict)

    def test_restort_within_word_0(self):
        self.assertIsInstance(resort_within_word(""), str)

    def test_resort_within_word_1(self):
        result = resort_within_word("Hallo wie geht es dir")
        self.assertEqual(result, "ollaH eiw theg se rid")

    def test_resort_within_word_2(self):
        self.assertEqual(resort_within_word(""), "")

    def test_resort_within_word_3(self):
        self.assertEqual(resort_within_word("abc"), "cba")

    def test_resort_within_word_4(self):
        self.assertEqual(resort_within_word("Aab baA"), "baA Aab")

    def test_resort_within_word_5(self):
        self.assertEqual(resort_within_word("AAA aaa AaA aAa"), "AAA aaa AaA aAa")

    def test_resort_within_word_6(self):
        self.assertEqual(resort_within_word("t t s t"), "t t s t")

    def test_keep_smallest_biggest_0(self):
        self.assertIsInstance(keep_smallest_biggest([]), list)

    def test_keep_smallest_biggest_1(self):
        self.assertListEqual(keep_smallest_biggest([]), [])

    def test_keep_smallest_biggest_2(self):
        self.assertListEqual(keep_smallest_biggest([1, 4, 3, 4, 1, 2]), [1, 4, 4, 1])

    def test_keep_smallest_biggest_3(self):
        self.assertListEqual(keep_smallest_biggest([1]), [1])

    def test_keep_smallest_biggest_4(self):
        self.assertListEqual(keep_smallest_biggest([-3, -4, -5]), [-3, -5])

    def test_keep_smallest_biggest_5(self):
        self.assertListEqual(keep_smallest_biggest(list(range(100_000))), [0, 99_999])

    def test_keep_smallest_biggest_6(self):
        self.assertListEqual(keep_smallest_biggest(list(range(100_000, 0, -1))), [100_000, 1])

    def test_count_letters_0(self):
        self.assertIsInstance(count_letters(""), dict)

    def test_count_letters_1(self):
        result = count_letters("Hallo wie geht es dir?")
        expected = {'?': 1,
                    'H': 1,
                    'a': 1,
                    'd': 1,
                    'e': 3,
                    'g': 1,
                    'h': 1,
                    'i': 2,
                    'l': 2,
                    'o': 1,
                    'r': 1,
                    's': 1,
                    't': 1,
                    'w': 1}
        self.assertEqual(result, expected)

    def test_count_letters_2(self):
        self.assertEqual(count_letters(""), dict())

    def test_count_letters_3(self):
        self.assertEqual(count_letters("   "), dict())

    def test_count_letters_4(self):
        self.assertEqual(count_letters("du da"), {"d": 2, "u": 1, "a": 1})

    def test_count_letters_5(self):
        self.assertEqual(count_letters("a b Aa" * 100), {'a': 200, 'b': 100, 'A': 100})

    def test_count_letters_6(self):
        self.assertEqual(count_letters("12321"), {"1": 2, "2": 2, "3": 1})

    def test_funny_sum_0(self):
        self.assertIsInstance(funny_sum([]), int)

    def test_funny_sum_1(self):
        self.assertEqual(funny_sum([]), 0)

    def test_funny_sum_2(self):
        self.assertEqual(funny_sum([1, 2, 3, 4, 5]), -3)

    def test_funny_sum_3(self):
        self.assertEqual(funny_sum([0, 0, 0]), 0)

    def test_funny_sum_4(self):
        self.assertEqual(funny_sum([-1, -3, -5]), 9)

    def test_funny_sum_5(self):
        self.assertEqual(funny_sum([-1, 1, 3, 4, -4, 8]), 5)

    def test_funny_sum_6(self):
        self.assertEqual(funny_sum(list(range(1001))), 500)

    def test_funny_sum_7(self):
        self.assertEqual(funny_sum(list(range(1000))), -500)

    def test_is_left_bigger_0(self):
        self.assertIsInstance(is_left_bigger([]), tuple)

    def test_is_left_bigger_1(self):
        self.assertTupleEqual(is_left_bigger([]), tuple())

    def test_is_left_bigger_2(self):
        self.assertTupleEqual(is_left_bigger([4]), tuple())

    def test_is_left_bigger_3(self):
        self.assertTupleEqual(is_left_bigger([2, 1]), (True,))

    def test_is_left_bigger_4(self):
        self.assertTupleEqual(is_left_bigger([4, 2, 6, 3, 1, 1]), (True, False, True, True, False))

    def test_is_left_bigger_5(self):
        self.assertTupleEqual(is_left_bigger([4, 2, 6, 3, 1]), (True, False, True, True))

    def test_is_left_bigger_6(self):
        input_list = [4, 2, 6, 3, 1]
        result = is_left_bigger(input_list)
        self.assertEqual(len(result), len(input_list) - 1)

    def test_is_left_bigger_7(self):
        self.assertTupleEqual(is_left_bigger(list(range(100))), (False,) * 99)

    def test_is_left_bigger_8(self):
        self.assertTupleEqual(is_left_bigger(list(range(100, 0, -1))), (True,) * 99)

    def test_swap_digets_0(self):
        self.assertIsInstance(swap_digets(0), int)

    def test_swap_digets_1(self):
        self.assertEqual(swap_digets(13050), 5031)

    def test_swap_digets_2(self):
        self.assertEqual(swap_digets(0), 0)

    def test_swap_digets_3(self):
        self.assertEqual(swap_digets(1234), 4321)

    def test_swap_digets_4(self):
        self.assertEqual(swap_digets(100000), 1)

    def test_swap_digets_5(self):
        self.assertEqual(swap_digets(11111), 11111)

    def test_swap_digets_6(self):
        self.assertEqual(swap_digets(1000011), 1100001)

    def test_swap_case_0(self):
        self.assertIsInstance(swap_case(""), str)

    def test_swap_case_1(self):
        self.assertEqual(swap_case("Aloh"), "aLOH")

    def test_swap_case_2(self):
        self.assertEqual(swap_case(""), "")

    def test_swap_case_3(self):
        self.assertEqual(swap_case("aaaa"), "AAAA")

    def test_swap_case_4(self):
        self.assertEqual(swap_case("Ich bin ein Text"), "iCH BIN EIN tEXT")

    def test_swap_case_5(self):
        text = "Ich bin ein Text  "
        self.assertEqual(swap_case(swap_case(text)), text)

    def test_swap_case_6(self):
        text = "es ist 10 nach 11"
        self.assertEqual(swap_case(text), "ES IST 10 NACH 11")

    def test_add_and_sub_0(self):
        self.assertIsInstance(add_and_sub(1, 1), tuple)

    def test_add_and_sub_1(self):
        r1, r2 = add_and_sub(1, 1)
        self.assertIsInstance(r1, int)
        self.assertIsInstance(r2, int)

    def test_add_and_sub_2(self):
        self.assertEqual(add_and_sub(0, 0), (0, 0))

    def test_add_and_sub_3(self):
        self.assertEqual(add_and_sub(10, 10), (20, 0))

    def test_add_and_sub_4(self):
        self.assertEqual(add_and_sub(12, -10), (2, 22))

    def test_add_and_sub_5(self):
        self.assertEqual(add_and_sub(-22, -3), (-25, -19))

    def test_all_len_0(self):
        self.assertIsInstance(all_len(""), tuple)

    def test_all_len_1(self):
        self.assertTupleEqual(all_len("Hallowiegehts"), (13,))

    def test_all_len_2(self):
        self.assertTupleEqual(all_len("Hallo wie gehts"), (5, 3, 5))

    def test_all_len_3(self):
        self.assertTupleEqual(all_len(""), tuple())

    def test_all_len_4(self):
        self.assertTupleEqual(all_len("   "), tuple())

    def test_all_len_5(self):
        self.assertTupleEqual(all_len("Hallo wer bist  du denn"), (5, 3, 4, 2, 4))

    def test_get_unique_numbers_0(self):
        self.assertIsInstance(get_unique_numbers(""), set)

    def test_get_unique_numbers_1(self):
        self.assertSetEqual(get_unique_numbers("10 10 100 1"), {1, 10, 100})

    def test_get_unique_numbers_2(self):
        self.assertSetEqual(get_unique_numbers("10"), {10})

    def test_get_unique_numbers_3(self):
        self.assertSetEqual(get_unique_numbers("Hier gibt es keine Zahlen"), set())

    def test_get_unique_numbers_4(self):
        self.assertSetEqual(get_unique_numbers("10 ist größer als 8 ist gleich 8"), {8, 10})

    def test_get_unique_numbers_5(self):
        text = "wir sind 100000 und mit 10 wird das 0"
        expected = {100000, 10, 0}
        self.assertEqual(get_unique_numbers(text), expected)

    def test_get_unique_numbers_6(self):
        self.assertEqual(get_unique_numbers("no numbers here"), set())

    def test_change_type_0(self):
        self.assertIsInstance(change_type(list()), tuple)

    def test_change_type_1(self):
        self.assertIsInstance(change_type(set()), list)

    def test_change_type_2(self):
        self.assertIsInstance(change_type(tuple()), set)

    def test_change_type_3(self):
        self.assertTupleEqual(change_type(list()), tuple())

    def test_change_type_4(self):
        self.assertTupleEqual(change_type([1, 2, 3]), (1, 2, 3))

    def test_change_type_5(self):
        self.assertListEqual(change_type(set()), list())

    def test_change_type_6(self):
        self.assertListEqual(change_type({1, 2, 3, 2, 1}), [1, 3])

    def test_change_type_7(self):
        self.assertListEqual(change_type({1}), [1, 1])

    def test_change_type_8(self):
        self.assertSetEqual(change_type(tuple()), set())

    def test_change_type_9(self):
        self.assertSetEqual(change_type((1, 2, 3, 2, 1)), {1, 2, 3})

    def test_apply_operation_0(self):
        def add(a, b):
            return a + b

        self.assertIsInstance(apply_operation([], add), list)

    def test_apply_operation_1(self):
        def add(a, b):
            return a + b

        self.assertListEqual(apply_operation([(1, 3), (4.5, 5.5)], add), [4, 10.0])

    def test_apply_operation_2(self):
        def add(a, b):
            return a + b

        self.assertListEqual(apply_operation([("du", "da")], add), ["duda"])

    def test_apply_operation_3(self):
        self.assertListEqual(apply_operation([(1, 3), (4.5, 5.5)], max), [3, 5.5])

    def test_apply_operation_4(self):
        self.assertListEqual(apply_operation([], max), [])

    def test_apply_operation_5(self):
        self.assertListEqual(apply_operation([("A", "B"), ("C", "D")], max), ["B", "D"])

    def test_deep_positive_check_0(self):
        self.assertIsInstance(deep_positive_check([[1]], True), list)

    def test_deep_positive_check_1(self):
        self.assertListEqual(deep_positive_check([[1]]), [[True]])

    def test_deep_positive_check_2(self):
        self.assertListEqual(deep_positive_check([[1, 2], [0, -1], [-1, 0, 1]]),
                             [[True, True], [True, False], [False, True, True]])

    def test_deep_positive_check_3(self):
        self.assertListEqual(deep_positive_check([[1, 2], [0, -1], [-1, 0, 1]], False),
                             [[True, True], [False, False], [False, False, True]])

    def test_deep_positive_check_4(self):
        self.assertListEqual(deep_positive_check([[1, -1, 0]]), [[True, False, True]])

    def test_deep_positive_check_5(self):
        self.assertListEqual(deep_positive_check([[1], [-1], [0]]), [[True], [False], [True]])

    def test_deep_positive_check_6(self):
        self.assertTupleEqual(deep_positive_check.__defaults__, (True,))
