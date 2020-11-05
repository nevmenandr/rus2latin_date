import unittest
from rus2latin_date import Converter

ldays = [('1 января 2018', 'Kalendis Ianuariis'),
    ('2 января.', 'ante diem IIII Nonas Ianuarias'),
    ('03-01-1988', 'ante diem III Nonas Ianuarias'),
    ('04.01.1998', 'pridie Nonas Ianuarias'),
    ('2002-01-05', 'Nonis Ianuariis'),
    ('6.1.2002', 'ante diem VIII Idus Ianuarias'),
    ('7 января 2333', 'ante diem VII Idus Ianuarias'),
    ('8 января 147', 'ante diem VI Idus Ianuarias'),
    ('9 ЯНВАРЯ', 'ante diem V Idus Ianuarias'),
    ('1/10/1914', 'ante diem IIII Idus Ianuarias'),
    ('11 января', 'ante diem III Idus Ianuarias'),
    ('12 января', 'pridie Idus Ianuarias'),
    ('13 января', 'Idibus Ianuariis'),
    ('14 января', 'ante diem XIX Kalendas Februarias'),
    ('15 января', 'ante diem XVIII Kalendas Februarias'),
    ('16 января', 'ante diem XVII Kalendas Februarias'),
    ('17 января', 'ante diem XVI Kalendas Februarias'),
    ('18 января', 'ante diem XV Kalendas Februarias'),
    ('19 января', 'ante diem XIIII Kalendas Februarias'),
    ('20 января', 'ante diem XIII Kalendas Februarias'),
    ('21 января', 'ante diem XII Kalendas Februarias'),
    ('22 января', 'ante diem XI Kalendas Februarias'),
    ('23 января', 'ante diem X Kalendas Februarias'),
    ('24 января', 'ante diem IX Kalendas Februarias'),
    ('25 января', 'ante diem VIII Kalendas Februarias'),
    ('26 января', 'ante diem VII Kalendas Februarias'),
    ('27 января', 'ante diem VI Kalendas Februarias'),
    ('28 января', 'ante diem V Kalendas Februarias'),
    ('29 января', 'ante diem IIII Kalendas Februarias'),
    ('30 января', 'ante diem III Kalendas Februarias'),
    ('31 января', 'pridie Kalendas Februarias'),
    ('1 февраля', 'Kalendis Februariis'),
    ('2 февраля', 'ante diem IIII Nonas Februarias'),
    ('3 февраля', 'ante diem III Nonas Februarias'),
    ('4 февраля', 'pridie Nonas Februarias'),
    ('5 февраля', 'Nonis Februariis'),
    ('6 февраля', 'ante diem VIII Idus Februarias'),
    ('7 февраля', 'ante diem VII Idus Februarias'),
    ('8 февраля', 'ante diem VI Idus Februarias'),
    ('9 февраля', 'ante diem V Idus Februarias'),
    ('10 февраля', 'ante diem IIII Idus Februarias'),
    ('11 февраля', 'ante diem III Idus Februarias'),
    ('12 февраля', 'pridie Idus Februarias'),
    ('13 февраля', 'Idibus Februariis'),
    ('14 февраля', 'ante diem XVI Kalendas Martias'),
    ('15 февраля', 'ante diem XV Kalendas Martias'),
    ('16 февраля', 'ante diem XIIII Kalendas Martias'),
    ('17 февраля', 'ante diem XIII Kalendas Martias'),
    ('18 февраля', 'ante diem XII Kalendas Martias'),
    ('19 февраля', 'ante diem XI Kalendas Martias'),
    ('20 февраля', 'ante diem X Kalendas Martias'),
    ('21 февраля', 'ante diem IX Kalendas Martias'),
    ('22 февраля', 'ante diem VIII Kalendas Martias'),
    ('23 февраля', 'ante diem VII Kalendas Martias'),
    ('24 февраля 2016', 'ante diem VI Kalendas Martias'),
    ('25 февраля 2020', 'ante diem VI Kalendas Martias'),
    ('26 февраля 2024', 'ante diem V Kalendas Martias'),
    ('27 февраля 2028', 'ante diem IIII Kalendas Martias'),
    ('28 февраля 2012', 'ante diem III Kalendas Martias'),
    ('29 февраля 2012', 'pridie Kalendas Martias'),
    ('1 марта', 'Kalendis Martiis'),
    ('2 марта', 'ante diem VI Nonas Martias'),
    ('3 марта', 'ante diem V Nonas Martias'),
    ('4 марта', 'ante diem IIII Nonas Martias'),
    ('5 марта', 'ante diem III Nonas Martias'),
    ('6 марта', 'pridie Nonas Martias'),
    ('7 марта', 'Nonis Martiis'),
    ('8 марта', 'ante diem VIII Idus Martias'),
    ('9 марта', 'ante diem VII Idus Martias'),
    ('10 марта', 'ante diem VI Idus Martias'),
    ('11 марта', 'ante diem V Idus Martias'),
    ('12 марта', 'ante diem IIII Idus Martias'),
    ('13 марта', 'ante diem III Idus Martias'),
    ('14 марта', 'pridie Idus Martias'),
    ('15 марта', 'Idibus Martiis'),
    ('16 марта', 'ante diem XVII Kalendas Apriles'),
    ('17 марта', 'ante diem XVI Kalendas Apriles'),
    ('18 марта', 'ante diem XV Kalendas Apriles'),
    ('19 марта', 'ante diem XIIII Kalendas Apriles'),
    ('20 марта', 'ante diem XIII Kalendas Apriles'),
    ('21 марта', 'ante diem XII Kalendas Apriles'),
    ('22 марта', 'ante diem XI Kalendas Apriles'),
    ('23 марта', 'ante diem X Kalendas Apriles'),
    ('24 марта', 'ante diem IX Kalendas Apriles'),
    ('25 марта', 'ante diem VIII Kalendas Apriles'),
    ('26 марта', 'ante diem VII Kalendas Apriles'),
    ('27 марта', 'ante diem VI Kalendas Apriles'),
    ('28 марта', 'ante diem V Kalendas Apriles'),
    ('29 марта', 'ante diem IIII Kalendas Apriles'),
    ('30 марта', 'ante diem III Kalendas Apriles'),
    ('31 марта', 'pridie Kalendas Apriles'),
    ('1 апреля', 'Kalendis Aprilibus'),
    ('2 апреля', 'ante diem IIII Nonas Apriles'),
    ('3 апреля', 'ante diem III Nonas Apriles'),
    ('4 апреля', 'pridie Nonas Apriles'),
    ('5 апреля', 'Nonis Aprilibus'),
    ('6 апреля', 'ante diem VIII Idus Apriles'),
    ('7 апреля', 'ante diem VII Idus Apriles'),
    ('8 апреля', 'ante diem VI Idus Apriles'),
    ('9 апреля', 'ante diem V Idus Apriles'),
    ('10 апреля', 'ante diem IIII Idus Apriles'),
    ('11 апреля', 'ante diem III Idus Apriles'),
    ('12 апреля', 'pridie Idus Apriles'),
    ('13 апреля', 'Idibus Aprilibus'),
    ('14 апреля', 'ante diem XVIII Kalendas Maias'),
    ('15 апреля', 'ante diem XVII Kalendas Maias'),
    ('16 апреля', 'ante diem XVI Kalendas Maias'),
    ('17 апреля', 'ante diem XV Kalendas Maias'),
    ('18 апреля', 'ante diem XIIII Kalendas Maias'),
    ('19 апреля', 'ante diem XIII Kalendas Maias'),
    ('20 апреля', 'ante diem XII Kalendas Maias'),
    ('21 апреля', 'ante diem XI Kalendas Maias'),
    ('22 апреля', 'ante diem X Kalendas Maias'),
    ('23 апреля', 'ante diem IX Kalendas Maias'),
    ('24 апреля', 'ante diem VIII Kalendas Maias'),
    ('25 апреля', 'ante diem VII Kalendas Maias'),
    ('26 апреля', 'ante diem VI Kalendas Maias'),
    ('27 апреля', 'ante diem V Kalendas Maias'),
    ('28 апреля', 'ante diem IIII Kalendas Maias'),
    ('29 апреля', 'ante diem III Kalendas Maias'),
    ('30 апреля', 'pridie Kalendas Maias'),
    ('1 мая', 'Kalendis Maiis'),
    ('2 мая', 'ante diem VI Nonas Maias'),
    ('3 мая', 'ante diem V Nonas Maias'),
    ('4 мая', 'ante diem IIII Nonas Maias'),
    ('5 мая', 'ante diem III Nonas Maias'),
    ('6 мая', 'pridie Nonas Maias'),
    ('7 мая', 'Nonis Maiis'),
    ('8 мая', 'ante diem VIII Idus Maias'),
    ('9 мая', 'ante diem VII Idus Maias'),
    ('10 мая', 'ante diem VI Idus Maias'),
    ('11 мая', 'ante diem V Idus Maias'),
    ('12 мая', 'ante diem IIII Idus Maias'),
    ('13 мая', 'ante diem III Idus Maias'),
    ('14 мая', 'pridie Idus Maias'),
    ('15 мая', 'Idibus Maiis'),
    ('16 мая', 'ante diem XVII Kalendas Iunias'),
    ('17 мая', 'ante diem XVI Kalendas Iunias'),
    ('18 мая', 'ante diem XV Kalendas Iunias'),
    ('19 мая', 'ante diem XIIII Kalendas Iunias'),
    ('20 мая', 'ante diem XIII Kalendas Iunias'),
    ('21 мая', 'ante diem XII Kalendas Iunias'),
    ('22 мая', 'ante diem XI Kalendas Iunias'),
    ('23 мая', 'ante diem X Kalendas Iunias'),
    ('24 мая', 'ante diem IX Kalendas Iunias'),
    ('25 мая', 'ante diem VIII Kalendas Iunias'),
    ('26 мая', 'ante diem VII Kalendas Iunias'),
    ('27 мая', 'ante diem VI Kalendas Iunias'),
    ('28 мая', 'ante diem V Kalendas Iunias'),
    ('29 мая', 'ante diem IIII Kalendas Iunias'),
    ('30 мая', 'ante diem III Kalendas Iunias'),
    ('31 мая', 'pridie Kalendas Iunias'),
    ('1 июня', 'Kalendis Iuniis'),
    ('2 июня', 'ante diem IIII Nonas Iunias'),
    ('3 июня', 'ante diem III Nonas Iunias'),
    ('4 июня', 'pridie Nonas Iunias'),
    ('5 июня', 'Nonis Iuniis'),
    ('6 июня', 'ante diem VIII Idus Iunias'),
    ('7 июня', 'ante diem VII Idus Iunias'),
    ('8 июня', 'ante diem VI Idus Iunias'),
    ('9 июня', 'ante diem V Idus Iunias'),
    ('10 июня', 'ante diem IIII Idus Iunias'),
    ('11 июня', 'ante diem III Idus Iunias'),
    ('12 июня', 'pridie Idus Iunias'),
    ('13 июня', 'Idibus Iuniis'),
    ('14 июня', 'ante diem XVIII Kalendas Iulias'),
    ('15 июня', 'ante diem XVII Kalendas Iulias'),
    ('16 июня', 'ante diem XVI Kalendas Iulias'),
    ('17 июня', 'ante diem XV Kalendas Iulias'),
    ('18 июня', 'ante diem XIIII Kalendas Iulias'),
    ('19 июня', 'ante diem XIII Kalendas Iulias'),
    ('20 июня', 'ante diem XII Kalendas Iulias'),
    ('21 июня', 'ante diem XI Kalendas Iulias'),
    ('22 июня', 'ante diem X Kalendas Iulias'),
    ('23 июня', 'ante diem IX Kalendas Iulias'),
    ('24 июня', 'ante diem VIII Kalendas Iulias'),
    ('25 июня', 'ante diem VII Kalendas Iulias'),
    ('26 июня', 'ante diem VI Kalendas Iulias'),
    ('27 июня', 'ante diem V Kalendas Iulias'),
    ('28 июня', 'ante diem IIII Kalendas Iulias'),
    ('29 июня', 'ante diem III Kalendas Iulias'),
    ('30 июня', 'pridie Kalendas Iulias'),
    ('1 июля', 'Kalendis Iuliis'),
    ('2 июля', 'ante diem VI Nonas Iulias'),
    ('3 июля', 'ante diem V Nonas Iulias'),
    ('4 июля', 'ante diem IIII Nonas Iulias'),
    ('5 июля', 'ante diem III Nonas Iulias'),
    ('6 июля', 'pridie Nonas Iulias'),
    ('7 июля', 'Nonis Iuliis'),
    ('8 июля', 'ante diem VIII Idus Iulias'),
    ('9 июля', 'ante diem VII Idus Iulias'),
    ('10 июля', 'ante diem VI Idus Iulias'),
    ('11 июля', 'ante diem V Idus Iulias'),
    ('12 июля', 'ante diem IIII Idus Iulias'),
    ('13 июля', 'ante diem III Idus Iulias'),
    ('14 июля', 'pridie Idus Iulias'),
    ('15 июля', 'Idibus Iuliis'),
    ('16 июля', 'ante diem XVII Kalendas Augustas'),
    ('17 июля', 'ante diem XVI Kalendas Augustas'),
    ('18 июля', 'ante diem XV Kalendas Augustas'),
    ('19 июля', 'ante diem XIIII Kalendas Augustas'),
    ('20 июля', 'ante diem XIII Kalendas Augustas'),
    ('21 июля', 'ante diem XII Kalendas Augustas'),
    ('22 июля', 'ante diem XI Kalendas Augustas'),
    ('23 июля', 'ante diem X Kalendas Augustas'),
    ('24 июля', 'ante diem IX Kalendas Augustas'),
    ('25 июля', 'ante diem VIII Kalendas Augustas'),
    ('26 июля', 'ante diem VII Kalendas Augustas'),
    ('27 июля', 'ante diem VI Kalendas Augustas'),
    ('28 июля', 'ante diem V Kalendas Augustas'),
    ('29 июля', 'ante diem IIII Kalendas Augustas'),
    ('30 июля', 'ante diem III Kalendas Augustas'),
    ('31 июля', 'pridie Kalendas Augustas'),
    ('1 августа', 'Kalendis Augustis'),
    ('2 августа', 'ante diem IIII Nonas Augustas'),
    ('3 августа', 'ante diem III Nonas Augustas'),
    ('4 августа', 'pridie Nonas Augustas'),
    ('5 августа', 'Nonis Augustis'),
    ('6 августа', 'ante diem VIII Idus Augustas'),
    ('7 августа', 'ante diem VII Idus Augustas'),
    ('8 августа', 'ante diem VI Idus Augustas'),
    ('9 августа', 'ante diem V Idus Augustas'),
    ('10 августа', 'ante diem IIII Idus Augustas'),
    ('11 августа', 'ante diem III Idus Augustas'),
    ('12 августа', 'pridie Idus Augustas'),
    ('13 августа', 'Idibus Augustis'),
    ('14 августа', 'ante diem XIX Kalendas Septembres'),
    ('15 августа', 'ante diem XVIII Kalendas Septembres'),
    ('16 августа', 'ante diem XVII Kalendas Septembres'),
    ('17 августа', 'ante diem XVI Kalendas Septembres'),
    ('18 августа', 'ante diem XV Kalendas Septembres'),
    ('19 августа', 'ante diem XIIII Kalendas Septembres'),
    ('20 августа', 'ante diem XIII Kalendas Septembres'),
    ('21 августа', 'ante diem XII Kalendas Septembres'),
    ('22 августа', 'ante diem XI Kalendas Septembres'),
    ('23 августа', 'ante diem X Kalendas Septembres'),
    ('24 августа', 'ante diem IX Kalendas Septembres'),
    ('25 августа', 'ante diem VIII Kalendas Septembres'),
    ('26 августа', 'ante diem VII Kalendas Septembres'),
    ('27 августа', 'ante diem VI Kalendas Septembres'),
    ('28 августа', 'ante diem V Kalendas Septembres'),
    ('29 августа', 'ante diem IIII Kalendas Septembres'),
    ('30 августа', 'ante diem III Kalendas Septembres'),
    ('31 августа', 'pridie Kalendas Septembres'),
    ('1 сентября', 'Kalendis Septembribus'),
    ('2 сентября', 'ante diem IIII Nonas Septembres'),
    ('3 сентября', 'ante diem III Nonas Septembres'),
    ('4 сентября', 'pridie Nonas Septembres'),
    ('5 сентября', 'Nonis Septembribus'),
    ('6 сентября', 'ante diem VIII Idus Septembres'),
    ('7 сентября', 'ante diem VII Idus Septembres'),
    ('8 сентября', 'ante diem VI Idus Septembres'),
    ('9 сентября', 'ante diem V Idus Septembres'),
    ('10 сентября', 'ante diem IIII Idus Septembres'),
    ('11 сентября', 'ante diem III Idus Septembres'),
    ('12 сентября', 'pridie Idus Septembres'),
    ('13 сентября', 'Idibus Septembribus'),
    ('14 сентября', 'ante diem XVIII Kalendas Octobres'),
    ('15 сентября', 'ante diem XVII Kalendas Octobres'),
    ('16 сентября', 'ante diem XVI Kalendas Octobres'),
    ('17 сентября', 'ante diem XV Kalendas Octobres'),
    ('18 сентября', 'ante diem XIIII Kalendas Octobres'),
    ('19 сентября', 'ante diem XIII Kalendas Octobres'),
    ('20 сентября', 'ante diem XII Kalendas Octobres'),
    ('21 сентября', 'ante diem XI Kalendas Octobres'),
    ('22 сентября', 'ante diem X Kalendas Octobres'),
    ('23 сентября', 'ante diem IX Kalendas Octobres'),
    ('24 сентября', 'ante diem VIII Kalendas Octobres'),
    ('25 сентября', 'ante diem VII Kalendas Octobres'),
    ('26 сентября', 'ante diem VI Kalendas Octobres'),
    ('27 сентября', 'ante diem V Kalendas Octobres'),
    ('28 сентября', 'ante diem IIII Kalendas Octobres'),
    ('29 сентября', 'ante diem III Kalendas Octobres'),
    ('30 сентября', 'pridie Kalendas Octobres'),
    ('1 октября', 'Kalendis Octobribus'),
    ('2 октября', 'ante diem VI Nonas Octobres'),
    ('3 октября', 'ante diem V Nonas Octobres'),
    ('4 октября', 'ante diem IIII Nonas Octobres'),
    ('5 октября', 'ante diem III Nonas Octobres'),
    ('6 октября', 'pridie Nonas Octobres'),
    ('7 октября', 'Nonis Octobribus'),
    ('8 октября', 'ante diem VIII Idus Octobres'),
    ('9 октября', 'ante diem VII Idus Octobres'),
    ('10 октября', 'ante diem VI Idus Octobres'),
    ('11 октября', 'ante diem V Idus Octobres'),
    ('12 октября', 'ante diem IIII Idus Octobres'),
    ('13 октября', 'ante diem III Idus Octobres'),
    ('14 октября', 'pridie Idus Octobres'),
    ('15 октября', 'Idibus Octobribus'),
    ('16 октября', 'ante diem XVII Kalendas Novembres'),
    ('17 октября', 'ante diem XVI Kalendas Novembres'),
    ('18 октября', 'ante diem XV Kalendas Novembres'),
    ('19 октября', 'ante diem XIIII Kalendas Novembres'),
    ('20 октября', 'ante diem XIII Kalendas Novembres'),
    ('21 октября', 'ante diem XII Kalendas Novembres'),
    ('22 октября', 'ante diem XI Kalendas Novembres'),
    ('23 октября', 'ante diem X Kalendas Novembres'),
    ('24 октября', 'ante diem IX Kalendas Novembres'),
    ('25 октября', 'ante diem VIII Kalendas Novembres'),
    ('26 октября', 'ante diem VII Kalendas Novembres'),
    ('27 октября', 'ante diem VI Kalendas Novembres'),
    ('28 октября', 'ante diem V Kalendas Novembres'),
    ('29 октября', 'ante diem IIII Kalendas Novembres'),
    ('30 октября', 'ante diem III Kalendas Novembres'),
    ('31 октября', 'pridie Kalendas Novembres'),
    ('1 ноября', 'Kalendis Novembribus'),
    ('2 ноября', 'ante diem IIII Nonas Novembres'),
    ('3 ноября', 'ante diem III Nonas Novembres'),
    ('4 ноября', 'pridie Nonas Novembres'),
    ('5 ноября', 'Nonis Novembribus'),
    ('6 ноября', 'ante diem VIII Idus Novembres'),
    ('7 ноября', 'ante diem VII Idus Novembres'),
    ('8 ноября', 'ante diem VI Idus Novembres'),
    ('9 ноября', 'ante diem V Idus Novembres'),
    ('10 ноября', 'ante diem IIII Idus Novembres'),
    ('11 ноября', 'ante diem III Idus Novembres'),
    ('12 ноября', 'pridie Idus Novembres'),
    ('13 ноября', 'Idibus Novembribus'),
    ('14 ноября', 'ante diem XVIII Kalendas Decembres'),
    ('15 ноября 1983', 'ante diem XVII Kalendas Decembres'),
    ('16 ноября', 'ante diem XVI Kalendas Decembres'),
    ('17 ноября', 'ante diem XV Kalendas Decembres'),
    ('18 ноября', 'ante diem XIIII Kalendas Decembres'),
    ('19 ноября', 'ante diem XIII Kalendas Decembres'),
    ('20 ноября', 'ante diem XII Kalendas Decembres'),
    ('21 ноября', 'ante diem XI Kalendas Decembres'),
    ('22 ноября', 'ante diem X Kalendas Decembres'),
    ('23 ноября', 'ante diem IX Kalendas Decembres'),
    ('24 ноября', 'ante diem VIII Kalendas Decembres'),
    ('25 ноября', 'ante diem VII Kalendas Decembres'),
    ('26 ноября', 'ante diem VI Kalendas Decembres'),
    ('27 ноября', 'ante diem V Kalendas Decembres'),
    ('28 ноября', 'ante diem IIII Kalendas Decembres'),
    ('29 ноября', 'ante diem III Kalendas Decembres'),
    ('30 ноября', 'pridie Kalendas Decembres'),
    ('1 декабря', 'Kalendis Decembribus'),
    ('2 декабря', 'ante diem IIII Nonas Decembres'),
    ('3 декабря', 'ante diem III Nonas Decembres'),
    ('4 декабря', 'pridie Nonas Decembres'),
    ('5 декабря', 'Nonis Decembribus'),
    ('6 декабря', 'ante diem VIII Idus Decembres'),
    ('7 декабря', 'ante diem VII Idus Decembres'),
    ('8 декабря', 'ante diem VI Idus Decembres'),
    ('9 декабря', 'ante diem V Idus Decembres'),
    ('10 декабря', 'ante diem IIII Idus Decembres'),
    ('11 декабря', 'ante diem III Idus Decembres'),
    ('12 декабря', 'pridie Idus Decembres'),
    ('13 декабря', 'Idibus Decembribus'),
    ('14 декабря', 'ante diem XIX Kalendas Ianuarias'),
    ('15 декабря', 'ante diem XVIII Kalendas Ianuarias'),
    ('16 декабря', 'ante diem XVII Kalendas Ianuarias'),
    ('17 декабря', 'ante diem XVI Kalendas Ianuarias'),
    ('18 декабря', 'ante diem XV Kalendas Ianuarias'),
    ('19 декабря', 'ante diem XIIII Kalendas Ianuarias'),
    ('20 декабря', 'ante diem XIII Kalendas Ianuarias'),
    ('21 декабря', 'ante diem XII Kalendas Ianuarias'),
    ('22 декабря', 'ante diem XI Kalendas Ianuarias'),
    ('23 декабря', 'ante diem X Kalendas Ianuarias'),
    ('24 декабря', 'ante diem IX Kalendas Ianuarias'),
    ('25 декабря', 'ante diem VIII Kalendas Ianuarias'),
    ('26 декабря', 'ante diem VII Kalendas Ianuarias'),
    ('27 декабря', 'ante diem VI Kalendas Ianuarias'),
    ('28 декабря', 'ante diem V Kalendas Ianuarias'),
    ('29 декабря', 'ante diem IIII Kalendas Ianuarias'),
    ('30 декабря', 'ante diem III Kalendas Ianuarias'),
    ('31 декабря', 'pridie Kalendas Ianuarias')]

class TestConvrter(unittest.TestCase):

    def test_ldays(self):
        c = Converter()
        for src_text, roman_date in ldays:
            self.assertEqual(c.conv(src_text), roman_date)


if __name__ == '__main__':
    unittest.main()