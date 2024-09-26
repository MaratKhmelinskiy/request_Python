
import unittest

import requests
from config import API_BASE_URL, CLIENT, COOKIE


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.query = "маша"


    def test_search_video(self):


        # Выполнить GET-запрос
        response = requests.get(f"{API_BASE_URL}?query={self.query}&client={CLIENT}", cookies=COOKIE)

        # Проверка статуса кода
        self.assertEqual(response.status_code, 200)

        # Проверка наличия нужного хедера в ответе
        self.assertIn('abt', response.headers)
        self.assertEqual(response.headers['abt'], 'search:f;')

        # Проверка содержимого ответа
        data = response.json()
        # Проверка типов данных
        self.assertIsInstance(data["count"], int)
        self.assertIsInstance(data["has_next"], bool)
        self.assertIsInstance(data["current_page"], int)

        # Проверка наличия результатов резулт - не пуст
        self.assertIn("results", data)
        self.assertGreater(len(data["results"]), 0, "Не найдено ни одного результата.")

        # Проверка параметров внутри массива results
        video = data["results"][0]
        self.assertIn("id", video)


        self.assertIn("is_reborn_channel", video)  # Проверка наличия поля is_reborn_channel
        self.assertIsInstance(video["is_reborn_channel"], bool)  # Проверка типа

        self.assertIn("author", video)  # Проверка наличия объекта author
        self.assertIn("name", video["author"])  # Проверка наличия поля name
        self.assertTrue(video["author"]["name"].startswith("Маша"))  # Проверка, что название канала начинается с "Маша"
        self.assertTrue(video["title"].startswith("Маша"))          # Проверка, что название видео начинается с "Маша"



if __name__ == '__main__':
    unittest.main()