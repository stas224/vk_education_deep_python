import unittest
from math import isclose
from customlist import CustomList


class TestCustomList(unittest.TestCase):

    def test_adding_without_zero_elem(self):
        adding_list_1 = (CustomList([1, 2, 3]),
                         [1, 2, 3],
                         CustomList([1, 2, 3]))
        adding_list_2 = (CustomList([3, 2, 1]),
                         CustomList([3, 2, 1]),
                         [3, 2, 1])

        for add_list_1, add_list_2 in zip(adding_list_1, adding_list_2):
            template_1, template_2 = add_list_1, add_list_2
            total_list = add_list_1 + add_list_2

            self.assertEqual(add_list_1, template_1)
            self.assertEqual(add_list_2, template_2)
            self.assertEqual(total_list, [12])
            for item in total_list:
                self.assertEqual(item, 4)

            add_list_1 += add_list_2
            self.assertEqual(add_list_2, template_2)
            self.assertEqual(add_list_1, [12])
            for item, elem in enumerate(add_list_1):
                self.assertEqual(elem, total_list[item])

        add_list_1 = (CustomList([1.1, 2.2, 3.3]),
                      [3.3, 2.2, 1.1],
                      CustomList([3.3, 2.2, 1.1]))
        adding_list_2 = (CustomList([3.3, 2.2, 1.1]),
                         CustomList([3.3, 2.2, 1.1]),
                         [3.3, 2.2, 1.1])
        for add_list_1, add_list_2 in zip(add_list_1, adding_list_2):
            template_1, template_2 = add_list_1, add_list_2
            total_list = add_list_1 + add_list_2

            self.assertEqual(add_list_1, template_1)
            self.assertEqual(add_list_2, template_2)
            self.assertEqual(total_list, [13.2])
            for item, elem in enumerate(total_list):
                self.assertTrue(isclose(add_list_1[item] +
                                        add_list_2[item], elem))

            add_list_1 += add_list_2
            self.assertEqual(add_list_2, template_2)
            self.assertEqual(add_list_1, [13.2])
            for item, elem in enumerate(add_list_1):
                self.assertEqual(elem, total_list[item])

    def test_adding_with_zero_elem(self):
        adding_list_1 = (CustomList([1, 2, 3, 0]),
                         [1, 2, 3, 0],
                         CustomList([1, 2, 3, 0]))
        adding_list_2 = (CustomList([3, 2, 1]),
                         CustomList([3, 2, 1]),
                         [3, 2, 1])

        for add_list_1, add_list_2 in zip(adding_list_1, adding_list_2):
            template_1, template_2 = add_list_1, add_list_2
            total_list = add_list_1 + add_list_2

            self.assertEqual(add_list_1, template_1)
            self.assertEqual(add_list_2, template_2)
            self.assertEqual(total_list, [12])
            self.assertEqual(len(total_list), 4)
            for item, elem in enumerate(total_list):
                self.assertEqual(add_list_1[item] +
                                 (add_list_2[item]
                                  if item < len(add_list_2)
                                  else 0), elem)

            add_list_1 += add_list_2
            self.assertEqual(add_list_2, template_2)
            self.assertEqual(add_list_1, [12])
            for item, elem in enumerate(add_list_1):
                self.assertEqual(elem, total_list[item])

        adding_list_1 = (CustomList([1.1, 2.2, 3.3]),
                         [3.3, 2.2, 1.1],
                         CustomList([3.3, 2.2, 1.1]))
        adding_list_2 = (CustomList([3.3, 2.2, 1.1, 10.0]),
                         CustomList([3.3, 2.2, 1.1, 10]),
                         [3.3, 2.2, 1.1, 10])

        for add_list_1, add_list_2 in zip(adding_list_1, adding_list_2):
            template_1, template_2 = add_list_1, add_list_2
            total_list = add_list_1 + add_list_2

            self.assertEqual(add_list_1, template_1)
            self.assertEqual(add_list_2, template_2)
            self.assertEqual(total_list, [23.2])
            self.assertEqual(len(total_list), 4)
            for item, elem in enumerate(total_list):
                self.assertTrue(isclose(add_list_2[item] +
                                        (add_list_1[item]
                                         if item < len(add_list_1)
                                         else 0), elem))

            add_list_1 += add_list_2
            self.assertEqual(add_list_2, template_2)
            self.assertEqual(add_list_1, [23.2])
            for item, elem in enumerate(add_list_1):
                self.assertEqual(elem, total_list[item])

    def test_subtraction_without_zero_elem(self):
        subtract_list_1 = (CustomList([1, 2, 3]),
                           [1, 2, 3],
                           CustomList([1, 2, 3]))
        subtract_list_2 = (CustomList([3, 2, 1]),
                           CustomList([3, 2, 1]),
                           [3, 2, 1])
        for sub_list_1, sub_list_2 in zip(subtract_list_1, subtract_list_2):
            template_1, template_2 = sub_list_1, sub_list_2
            total_list = sub_list_1 - sub_list_2

            self.assertEqual(sub_list_1, template_1)
            self.assertEqual(sub_list_2, template_2)
            self.assertEqual(total_list, [0])
            for item, elem in enumerate(total_list):
                self.assertEqual(sub_list_1[item] - sub_list_2[item], elem)

            sub_list_1 -= sub_list_2
            self.assertEqual(sub_list_2, template_2)
            self.assertEqual(sub_list_1, [0])
            for item, elem in enumerate(sub_list_1):
                self.assertEqual(elem, total_list[item])

        subtract_list_1 = (CustomList([1.1, 2.2, 3.3]),
                           [3.3, 2.2, 1.1],
                           CustomList([3.3, 2.2, 1.1]))
        subtract_list_2 = (CustomList([3.3, 2.2, 1.1]),
                           CustomList([3.3, 2.2, 1.1]),
                           [3.3, 2.2, 1.1])
        for sub_list_1, sub_list_2 in zip(subtract_list_1, subtract_list_2):
            template_1, template_2 = sub_list_1, sub_list_2
            total_list = sub_list_1 - sub_list_2

            self.assertEqual(sub_list_1, template_1)
            self.assertEqual(sub_list_2, template_2)
            self.assertEqual(total_list, [0])
            for item, elem in enumerate(total_list):
                self.assertTrue(isclose(sub_list_1[item] -
                                        sub_list_2[item], elem))

            sub_list_1 -= sub_list_2
            self.assertEqual(sub_list_2, template_2)
            self.assertEqual(sub_list_1, [0])
            for item, elem in enumerate(sub_list_1):
                self.assertEqual(elem, total_list[item])

    def test_subtraction_with_zero_elem(self):
        subtract_list_1 = (CustomList([1, 2, 3, 0]),
                           [1, 2, 3, 0],
                           CustomList([1, 2, 3, 0]))
        subtract_list_2 = (CustomList([3, 2, 1]),
                           CustomList([3, 2, 1]),
                           [3, 2, 1])
        for sub_list_1, sub_list_2 in zip(subtract_list_1, subtract_list_2):
            template_1, template_2 = sub_list_1, sub_list_2
            total_list = sub_list_1 - sub_list_2

            self.assertEqual(sub_list_1, template_1)
            self.assertEqual(sub_list_2, template_2)
            self.assertEqual(total_list, [0])
            self.assertEqual(len(total_list), 4)
            for i, elem in enumerate(total_list):
                self.assertEqual(sub_list_1[i] -
                                 (sub_list_2[i] if i < len(sub_list_2)
                                  else 0),
                                 elem)

            sub_list_1 -= sub_list_2
            self.assertEqual(sub_list_2, template_2)
            self.assertEqual(sub_list_1, [0])
            for item, elem in enumerate(sub_list_1):
                self.assertEqual(elem, total_list[item])

        subtract_list_1 = (CustomList([1.1, 2.2, 3.3]),
                           [3.3, 2.2, 1.1],
                           CustomList([3.3, 2.2, 1.1]))
        subtract_list_2 = (CustomList([3.3, 2.2, 1.1, 10.0]),
                           CustomList([3.3, 2.2, 1.1, 10]),
                           [3.3, 2.2, 1.1, 10])
        for sub_list_1, sub_list_2 in zip(subtract_list_1, subtract_list_2):
            template_1, template_2 = sub_list_1, sub_list_2
            total_list = sub_list_1 - sub_list_2

            self.assertEqual(sub_list_1, template_1)
            self.assertEqual(sub_list_2, template_2)
            self.assertEqual(total_list, [-10])
            self.assertEqual(len(total_list), 4)
            for i, elem in enumerate(sub_list_1):
                self.assertTrue(isclose((elem if i < len(sub_list_1) else 0)
                                        - sub_list_2[i],
                                        total_list[i]))

            sub_list_1 -= sub_list_2
            self.assertEqual(sub_list_2, template_2)
            self.assertEqual(sub_list_1, [-10])
            for i, elem in enumerate(sub_list_1):
                self.assertEqual(elem, total_list[i])

    def test_eq_ne_le_ge(self):
        compare_list = CustomList([1, 2, 3])
        compare_list_1 = [CustomList([1, 2, 3]),
                          CustomList([2, 3, 1]),
                          CustomList([2, 3, 1, 0, 0])]
        compare_list_2 = [CustomList([1, 2, 4]),
                          CustomList([2, 3, 4]),
                          CustomList([2, 3, 1, 0, 4])]

        check_list, check_list_1, check_list_2 =\
            compare_list, compare_list_1, compare_list_2

        for item in range(3):
            self.assertTrue(compare_list == compare_list_1[item])
            self.assertTrue(compare_list >= compare_list_1[item])
            self.assertTrue(compare_list <= compare_list_1[item])
            self.assertFalse(compare_list == compare_list_2[item])
            self.assertTrue(compare_list != compare_list_2[item])
            self.assertFalse(compare_list != compare_list_1[item])

        self.assertEqual(compare_list, check_list)
        self.assertEqual(compare_list_1, check_list_1)
        self.assertEqual(compare_list_2, check_list_2)

        compare_list = CustomList([1.1, 2.2, 3.3])
        compare_list_1 = [CustomList([1.1, 2.2, 3.3]),
                          CustomList([2.2, 3.3, 1.1]),
                          CustomList([2.2, 3.3, 1.1, 0, 0])]
        compare_list_2 = [CustomList([1.1, 2.2, 4.4]),
                          CustomList([2.2, 3.3, 4.4]),
                          CustomList([2.2, 3.3, 1.1, 0, 4.4])]

        check_list, check_list_1, check_list_2 =\
            compare_list, compare_list_1, compare_list_2

        for item in range(3):
            self.assertTrue(compare_list == compare_list_1[item])
            self.assertTrue(compare_list >= compare_list_1[item])
            self.assertTrue(compare_list <= compare_list_1[item])
            self.assertFalse(compare_list == compare_list_2[item])
            self.assertTrue(compare_list != compare_list_2[item])
            self.assertFalse(compare_list != compare_list_1[item])

        self.assertEqual(compare_list, check_list)
        self.assertEqual(compare_list_1, check_list_1)
        self.assertEqual(compare_list_2, check_list_2)

    def test_lt_le_gt_ge(self):
        compare_list = CustomList([1, 2, 3])
        compare_list_1 = [CustomList([6]),
                          CustomList([5]),
                          CustomList([4, 0, 0])]
        compare_list_2 = [CustomList([1, 2, 3, 0, 0]),
                          CustomList([2, 3, 4]),
                          CustomList([2, 3, 1, 0, 4])]

        check_list, check_list_1, check_list_2 =\
            compare_list, compare_list_1, compare_list_2

        for item in range(len(compare_list)):
            self.assertTrue(compare_list >= compare_list_1[item])
            self.assertTrue(compare_list <= compare_list_2[item])
            self.assertFalse(compare_list < compare_list_1[item])
            self.assertFalse(compare_list > compare_list_2[item])

        self.assertEqual(compare_list, check_list)
        self.assertEqual(compare_list_1, check_list_1)
        self.assertEqual(compare_list_2, check_list_2)

        compare_list = CustomList([1.1, 2.2, 3.3])
        compare_list_1 = [CustomList([6.6]),
                          CustomList([6.1, 0.2]),
                          CustomList([2.1, 3.2, 1.1, 0, 0])]
        compare_list_2 = [CustomList([1.1, 2.2, 4.4]),
                          CustomList([2.2, 3.3, 4.4, 4.5]),
                          CustomList([2.2, 3.3, 1.1, 0, 4.4])]

        check_list, check_list_1, check_list_2 =\
            compare_list, compare_list_1, compare_list_2

        for item in range(len(compare_list)):
            self.assertTrue(compare_list >= compare_list_1[item])
            self.assertTrue(compare_list <= compare_list_2[item])
            self.assertFalse(compare_list < compare_list_1[item])
            self.assertFalse(compare_list > compare_list_2[item])

        self.assertEqual(compare_list, check_list)
        self.assertEqual(compare_list_1, check_list_1)
        self.assertEqual(compare_list_2, check_list_2)

    def test_str(self):
        a_list = CustomList([1, 2, 3])
        self.assertEqual(str(a_list), f'{[1, 2, 3]}'
                                      f' sum : {round(sum(a_list), 10)}')
        b_list = CustomList([1.1, 2.2, 3.3])
        self.assertEqual(str(b_list), f'{[1.1, 2.2, 3.3]}'
                                      f' sum : {round(sum(b_list), 10)}')

    def test_adding_with_different_lengths(self):  # pylint: disable=R0914
        list_1 = [1, 2.2, 3, 4, 5.12]
        custom_list_1 = CustomList(list_1)
        list_2 = [1, 2, 3.9]
        custom_list_2 = CustomList(list_2)

        template_1, template_2 = list_1, list_2
        template_c_1, template_c_2 = custom_list_1, custom_list_2

        total_1 = list_1 + custom_list_2
        total_c_2 = custom_list_2 + list_1
        total_2 = list_2 + custom_list_1
        total_c_1 = custom_list_1 + list_2
        total_all_c_1 = custom_list_1 + custom_list_2
        total_all_c_2 = custom_list_2 + custom_list_1

        self.assertEqual(total_1, total_c_2)
        self.assertEqual(total_2, total_c_1)
        self.assertEqual(total_1, total_2)
        self.assertEqual(total_all_c_1, total_all_c_2)
        self.assertEqual(total_1, total_all_c_1)

        self.assertEqual(template_1, list_1)
        self.assertEqual(template_2, list_2)
        self.assertEqual(template_c_1, custom_list_1)
        self.assertEqual(template_c_2, custom_list_2)

        for item, elem in enumerate(total_1):
            self.assertTrue(isclose(list_1[item] +
                                    (custom_list_2[item]
                                     if item < len(custom_list_2)
                                     else 0), elem))
            self.assertTrue(isclose(list_1[item] +
                                    (custom_list_2[item]
                                     if item < len(custom_list_2)
                                     else 0), total_c_2[item]))

        for item, elem in enumerate(total_2):
            self.assertTrue(isclose(custom_list_1[item] +
                                    (list_2[item]
                                     if item < len(list_2)
                                     else 0), elem))
            self.assertTrue(isclose(custom_list_1[item] +
                                    (list_2[item]
                                     if item < len(list_2)
                                     else 0), total_c_1[item]))

        for item, elem in enumerate(total_all_c_1):
            self.assertTrue(isclose(custom_list_1[item] +
                                    (custom_list_2[item]
                                     if item < len(custom_list_2)
                                     else 0), elem))
            self.assertTrue(isclose(custom_list_1[item] +
                                    (custom_list_2[item]
                                     if item < len(custom_list_2)
                                     else 0), total_c_2[item]))

    def test_subs_with_different_lengths(self):  # pylint: disable=R0914
        list_1 = [1, 2.2, 3, 4, 5.12]
        custom_list_1 = CustomList(list_1)
        list_2 = [1, 2, 3.9]
        custom_list_2 = CustomList(list_2)

        template_1, template_2 = list_1, list_2
        template_c_1, template_c_2 = custom_list_1, custom_list_2

        total_1 = list_1 - custom_list_2
        total_c_1 = custom_list_1 - list_2
        total_all_c_1 = custom_list_1 - custom_list_2

        total_2 = list_2 - custom_list_1
        total_c_2 = custom_list_2 - list_1
        total_all_c_2 = custom_list_2 - custom_list_1

        self.assertEqual(total_1, total_c_1)
        self.assertEqual(total_1, total_all_c_1)

        self.assertEqual(total_2, total_c_2)
        self.assertEqual(total_2, total_all_c_2)

        self.assertEqual(template_1, list_1)
        self.assertEqual(template_2, list_2)
        self.assertEqual(template_c_1, custom_list_1)
        self.assertEqual(template_c_2, custom_list_2)

        for item, elem in enumerate(total_1):
            self.assertTrue(isclose(list_1[item] -
                                    (custom_list_2[item]
                                     if item < len(custom_list_2)
                                     else 0), elem))
            self.assertTrue(isclose(custom_list_1[item] -
                                    (list_2[item]
                                     if item < len(list_2)
                                     else 0), total_c_1[item]))
            self.assertTrue(isclose(custom_list_1[item] -
                                    (custom_list_2[item]
                                     if item < len(custom_list_2)
                                     else 0), total_all_c_1[item]))

        for item, elem in enumerate(total_2):
            self.assertTrue(isclose((list_2[item]
                                     if item < len(list_2)
                                     else 0) - custom_list_1[item], elem))
            self.assertTrue(isclose((custom_list_2[item]
                                     if item < len(custom_list_2)
                                     else 0) - list_1[item], total_c_2[item]))
            self.assertTrue(isclose((custom_list_2[item]
                                     if item < len(custom_list_2)
                                     else 0) -
                                    custom_list_1[item], total_all_c_2[item]))


if __name__ == '__main__':
    unittest.main()
