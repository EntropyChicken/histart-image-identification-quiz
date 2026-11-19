import random

import answers
from images import load_image_paths
from quiz import QuizApp

# The last ha-number included in the quiz. Swap in another range from answers.py
# (ALL, INDIA_AND_BANGLADESH, JAPAN, GUTAI, JIKKEN_KOBO, MAO, POST_MAO,
# KOREA_AND_JAPAN, NEW).
IMAGE_RANGE = answers.NEW


def main():
    answers.print_answer_key()
    image_paths = load_image_paths(IMAGE_RANGE)
    random.shuffle(image_paths)
    QuizApp(image_paths, answers.answers).run()


if __name__ == "__main__":
    main()
