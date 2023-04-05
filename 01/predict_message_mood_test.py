import unittest
from unittest import mock

from predict_message_mood import predict_message_mood, SomeModel


class TestPredictMessageMood(unittest.TestCase):

    def setUp(self):
        self.model = SomeModel()
        self.text = 'test'

    def test_predict_res(self):
        self.assertEqual(type(self.text), str)
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_predict:
            for mock_predict.return_value in (0.2, 0.4, 0.9):
                self.assertEqual(self.text, 'test')
                self.assertEqual(self.model.predict(self.text), mock_predict.return_value)
                self.assertNotEqual(self.model.predict(self.text), 0.1)

        for _ in range(100):
            self.assertEqual(self.text, 'test')
            res = self.model.predict(self.text)
            self.assertLessEqual(res, 1)
            self.assertGreaterEqual(res, 0)

    def test_predict_mes_mood_res(self):
        with mock.patch("predict_message_mood.predict_message_mood") as mock_predict_mes_mood:
            mock_predict_mes_mood.return_value = 'неуд'
            self.assertEqual(mock_predict_mes_mood('ans', self.model), 'неуд')
            self.assertNotEqual(mock_predict_mes_mood('ans', self.model), 'отл')

    def test_predict_mes_mood_expected_res(self):
        expected_res = ('неуд', 'норм', 'отл')
        for _ in range(100):
            self.assertIn(predict_message_mood('abc', self.model), expected_res)

    def test_predict_mes_mood_res_with_defaults(self):
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_predict:
            for mock_predict.return_value, ans in zip((0.2, 0.4, 0.9), ('неуд', 'норм', 'отл')):
                self.assertEqual(type(self.text), str)
                self.assertEqual(predict_message_mood(self.text, self.model), ans)
            for mock_predict.return_value, ans in zip((0.8, 0.2, 0.4), ('неуд', 'норм', 'отл')):
                self.assertEqual(type(self.text), str)
                self.assertNotEqual(predict_message_mood(self.text, self.model), ans)

    def test_predict_mes_mood_res_non_defaults(self):
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_predict:
            for mock_predict.return_value, bad_th, good_th, ans in zip((0.07, 0.4, 0.9),
                                                                       (0.1, 0.2, 0.3),
                                                                       (0.7, 0.6, 0.8),
                                                                       ('неуд', 'норм', 'отл')):
                self.assertEqual(type(self.text), str)
                self.assertEqual(predict_message_mood(self.text, self.model, bad_th, good_th), ans)
                self.assertNotEqual(predict_message_mood(self.text, self.model, bad_th, good_th), 'ok')

    def test_predict_call_count(self):
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.5
            for _ in range(5):
                self.assertEqual(type(self.text), str)
                predict_message_mood(self.text, self.model)
            self.assertEqual(mock_predict.call_count, 5)

    def test_predict_mes_mood_default_parameters(self):
        self.assertEqual(predict_message_mood.__defaults__, (None, None, 0.3, 0.8))

    def test_some_model_message_with_predict_mes_mood(self):
        self.assertEqual(type(self.text), str)
        self.assertEqual([], self.model.message)
        self.assertNotIn(self.text, self.model.message)
        predict_message_mood(self.text, self.model)
        self.assertIn(self.text, self.model.message)
        self.assertEqual(type('abc'), str)
        self.assertNotIn('abs', self.model.message)

    def test_some_model_message_with_predict(self):
        self.assertEqual(type(self.text), str)
        self.assertEqual([], self.model.message)
        self.assertNotIn(self.text, self.model.message)
        self.model.predict(self.text)
        self.assertIn(self.text, self.model.message)
        self.assertEqual(type('abc'), str)
        self.assertNotIn('abc', self.model.message)
        self.assertEqual(self.text, 'test')

    def test_predict_mes_mood_err(self):
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_predict:
            mock_predict.side_effect = TypeError('float values only')
            with self.assertRaises(TypeError) as err:
                self.assertEqual(type(self.text), str)
                predict_message_mood(self.text, self.model)
            self.assertEqual(str(err.exception), 'float values only')

            with self.assertRaises(TypeError) as err:
                predict_message_mood()
            self.assertEqual(str(err.exception), "missing 'message' or 'model'")

    def test_predict_edge_cases(self):
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_predict:
            for mock_predict.return_value, bad_th, good_th, ans in zip((0.4, 0.8),
                                                                       (0.4, 0.4),
                                                                       (0.8, 0.8),
                                                                       ('норм', 'норм')):
                self.assertEqual(type(self.text), str)
                self.assertEqual(predict_message_mood(self.text, self.model, bad_th, good_th), ans)
                self.assertEqual(self.text, 'test')

            for mock_predict.return_value, bad_th, good_th, ans in zip((0.0, 1.0),
                                                                       (0.4, 0.4),
                                                                       (0.8, 0.8),
                                                                       ('неуд', 'отл')):
                self.assertEqual(type(self.text), str)
                self.assertEqual(predict_message_mood(self.text, self.model, bad_th, good_th), ans)
                self.assertEqual(self.text, 'test')

            for mock_predict.return_value, ans in zip((0.3, 0.8),
                                                      ('норм', 'норм')):
                self.assertEqual(type(self.text), str)
                self.assertEqual(predict_message_mood(self.text, self.model), ans)
                self.assertEqual(self.text, 'test')


if __name__ == '__main__':
    unittest.main()
