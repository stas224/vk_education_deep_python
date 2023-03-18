import unittest
from unittest import mock

from predict_message_mood import predict_message_mood, SomeModel


class TestPredictMessageMood(unittest.TestCase):

    def setUp(self):
        self.model = SomeModel()

    def test_predict_res(self):
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_predict:
            for mock_predict.return_value in zip((0.2, 0.4, 0.9)):
                self.assertEqual(self.model.predict('test'), mock_predict.return_value)
                self.assertNotEqual(self.model.predict('test'), 0.1)

        for _ in range(100):
            res = self.model.predict('test')
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
                self.assertEqual(predict_message_mood('test', self.model), ans)
            for mock_predict.return_value, ans in zip((0.8, 0.2, 0.4), ('неуд', 'норм', 'отл')):
                self.assertNotEqual(predict_message_mood('test', self.model), ans)

    def test_predict_mes_mood_res_non_defaults(self):
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_predict:
            for mock_predict.return_value, bad_th, good_th, ans in zip((0.07, 0.4, 0.9),
                                                                       (0.1, 0.2, 0.3),
                                                                       (0.7, 0.6, 0.8),
                                                                       ('неуд', 'норм', 'отл')):
                self.assertEqual(predict_message_mood('test', self.model, bad_th, good_th), ans)
                self.assertNotEqual(predict_message_mood('test', self.model, bad_th, good_th), 'ok')

    def test_predict_call_count(self):
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.5
            for _ in range(5):
                predict_message_mood('test', self.model)
            self.assertEqual(mock_predict.call_count, 5)

    def test_predict_mes_mood_default_parameters(self):
        self.assertEqual(predict_message_mood.__defaults__, (0.3, 0.8))

    def test_some_model_message_with_predict_mes_mood(self):
        self.assertEqual([], self.model.message)
        self.assertNotIn('test', self.model.message)
        predict_message_mood('test', self.model)
        self.assertIn('test', self.model.message)
        self.assertNotIn('abs', self.model.message)

    def test_some_model_message_with_predict(self):
        self.assertEqual([], self.model.message)
        self.assertNotIn('test', self.model.message)
        self.model.predict('test')
        self.assertIn('test', self.model.message)
        self.assertNotIn('abc', self.model.message)

    def test_predict_mes_mood_err(self):
        with mock.patch("predict_message_mood.SomeModel.predict") as mock_predict:

            mock_predict.side_effect = TypeError('float values only')
            with self.assertRaises(TypeError) as err:
                predict_message_mood('test', self.model)
            self.assertEqual(str(err.exception), 'float values only')

            with self.assertRaises(TypeError) as err:
                predict_message_mood()
            self.assertEqual(str(err.exception), "missing 'message' and 'model'")


if __name__ == '__main__':
    unittest.main()
