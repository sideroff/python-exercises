from roman import to_roman, from_roman
import unittest

known_values = (
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (7, 'VII'),
    (8, 'VIII'),
    (9, 'IX'),
    (10, 'X'),
    (50, 'L'),
    (100, 'C'),
    (500, 'D'),
    (1000, 'M'),
    (31, 'XXXI'),
    (148, 'CXLVIII'),
    (294, 'CCXCIV'),
    (312, 'CCCXII'),
    (421, 'CDXXI'),
    (528, 'DXXVIII'),
    (621, 'DCXXI'),
    (782, 'DCCLXXXII'),
    (870, 'DCCCLXX'),
    (941, 'CMXLI'),
    (1043, 'MXLIII'),
    (1110, 'MCX'),
    (1226, 'MCCXXVI'),
    (1301, 'MCCCI'),
    (1485, 'MCDLXXXV'),
    (1509, 'MDIX'),
    (1607, 'MDCVII'),
    (1754, 'MDCCLIV'),
    (1832, 'MDCCCXXXII'),
    (1993, 'MCMXCIII'),
    (2074, 'MMLXXIV'),
    (2152, 'MMCLII'),
    (2212, 'MMCCXII'),
    (2343, 'MMCCCXLIII'),
    (2499, 'MMCDXCIX'),
    (2574, 'MMDLXXIV'),
    (2646, 'MMDCXLVI'),
    (2723, 'MMDCCXXIII'),
    (2892, 'MMDCCCXCII'),
    (2975, 'MMCMLXXV'),
    (3051, 'MMMLI'),
    (3185, 'MMMCLXXXV'),
    (3250, 'MMMCCL'),
    (3313, 'MMMCCCXIII'),
    (3408, 'MMMCDVIII'),
    (3501, 'MMMDI'),
    (3610, 'MMMDCX'),
    (3743, 'MMMDCCXLIII'),
    (3844, 'MMMDCCCXLIV'),
    (3888, 'MMMDCCCLXXXVIII'),
    (3940, 'MMMCMXL'),
    (3999, 'MMMCMXCIX')
)

to_roman_bad_types = [
    None,
    1.0,
    True,
    'test',
    b"test",
    [1, 2],
    (1, 2),
    {1, 2},
    {'test': 1},
    print,
]

from_roman_bad_types = [
    None,
    1,
    1.0,
    True,
    b"test",
    [1, 2],
    (1, 2),
    {1, 2},
    {'test': 1},
    print,
]

less_than_min = [
    0,
    -1,
    -999999999999999999,
]

more_than_max = [
    4000,
    4001,
    999999999999999999
]


# class ToRoman(unittest.TestCase):
#     def test_known_values(self):
#         '''to_roman should return known output for known input'''

#         for integer, numeral in known_values:
#             self.assertEqual(to_roman(integer), numeral)

#     def test_bad_type_input(self):
#         '''to_roman should return TypeError when called with any type != int'''

#         for value in to_roman_bad_types:
#             self.assertRaises(TypeError, to_roman, value)

#     def test_less_than_min_input(self):
#         '''to_roman should return ValueError when called with any int <= 0'''

#         for value in less_than_min:
#             self.assertRaises(ValueError, to_roman, value)

#     def test_greater_than_max_input(self):
#         '''to_roman should return ValueError when called with any int > 3999'''

#         for value in more_than_max:
#             self.assertRaises(ValueError, to_roman, value)


class FromRoman(unittest.TestCase):
    def test_known_values(self):
        '''from_roman should return known output for known input'''

        for integer, numeral in known_values:
            self.assertEqual(from_roman(numeral), integer)

    # # not a good idea relying on to_roman imo
    # def test_all_possible_values(self):
    #     '''from_roman should return valid output for valid input'''

    #     for integer in range(1,4000):
    #         self.assertEqual(from_roman(to_roman(integer)), integer)

    def test_bad_type_input(self):
        '''from_input should return TypeError when called with any type != str'''

        for value in from_roman_bad_types:
            self.assertRaises(TypeError, from_roman, value)

    def test_too_many_repeated_numerals(self):
        '''from_roman should fail with too many repeated numerals'''
        for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(ValueError, from_roman, s)

    def test_repeated_pairs(self):
        '''from_roman should fail with repeated pairs of numerals'''
        for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(ValueError, from_roman, s)

    def test_malformed_antecedents(self):
        '''from_roman should fail with malformed antecedents'''
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(ValueError, from_roman, s)


if __name__ == '__main__':
    unittest.main()
