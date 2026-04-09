import os
import re
import random
from datetime import datetime, timedelta
from flask import Flask

app = Flask(__name__)

# Глобальные данные
CARS = ["Chevrolet", "Renault", "Ford", "Lada"]
CAT_BREEDS = [
    "корниш-рекс",
    "русская голубая",
    "шотландская вислоухая",
    "мейн-кун",
    "манчкин"
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, "war_and_peace.txt")


def load_words_from_book():
    """
    Загружает слова из книги один раз при запуске приложения.
    Убирает знаки препинания и оставляет только слова.
    """
    with open(BOOK_FILE, "r", encoding="utf-8") as book:
        text = book.read()

    # Берём только слова без цифр и знаков препинания
    words = re.findall(r"[^\W\d_]+", text, flags=re.UNICODE)
    return words


BOOK_WORDS = load_words_from_book()
counter_visits = 0


@app.route('/hello_world')
def hello_world():
    return "Привет, мир!"


@app.route('/cars')
def get_cars():
    return ", ".join(CARS)


@app.route('/cats')
def get_random_cat():
    random_cat = random.choice(CAT_BREEDS)
    return random_cat


@app.route('/get_time/now')
def get_current_time():
    current_time = datetime.now()
    return f"Точное время: {current_time}"


@app.route('/get_time/future')
def get_future_time():
    current_time_after_hour = datetime.now() + timedelta(hours=1)
    return f"Точное время через час будет {current_time_after_hour}"


@app.route('/get_random_word')
def get_random_word():
    random_word = random.choice(BOOK_WORDS)
    return random_word


@app.route('/counter')
def counter():
    global counter_visits
    counter_visits += 1
    return str(counter_visits)


if __name__ == '__main__':
    app.run(debug=True)