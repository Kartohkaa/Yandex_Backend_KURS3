from datetime import date

title = input("Название фотографии: ")

print("\nБазовые категории: горы, лес, вода, небо, поле, пустыня")
print("Если вашей категории нет в списке — введите 'своя'")
category = input("Категория: ").lower()

if category == "своя":
    custom_category = input("Введите название своей категории: ").lower()
    if custom_category == "":
        print("Своя категория не указана — присвоена 'другое'")
        category = "другое"
    else:
        category = custom_category

location = input("Место съёмки: ")

print("\nЧто вы чувствуете сейчас? (спокойствие, радость, грусть, тревога, вдохновение)")
print("Если чувство не из списка — введите 'своё'")
mood = input("Настроение: ").lower()

if mood == "своё":
    custom_mood = input("Опишите своё состояние: ").lower()
    if custom_mood == "":
        mood = "не указано"
    else:
        mood = custom_mood

description = input("Опишите ощущения от фотографии или что у вас на душе: ")

print("\n=== Проверка данных ===")

if len(title) < 3:
    print("Ошибка: название слишком короткое (минимум 3 символа)")
elif len(title) > 50:
    print("Ошибка: название слишком длинное (максимум 50 символов)")
else:
    print(f"Название '{title}' принято")

base_categories = ["горы", "лес", "вода", "небо", "поле", "пустыня"]

if category in base_categories:
    print(f"Категория '{category}' определена")
elif category == "":
    print("Категория не указана — присвоена 'другое'")
    category = "другое"
else:
    print(f"Создана пользовательская категория '{category}'")

base_moods = ["спокойствие", "радость", "грусть", "тревога", "вдохновение"]

if mood in base_moods:
    print(f"Настроение отмечено: {mood}")
elif mood == "не указано":
    print("Настроение не указано")
else:
    print(f"Отмечено состояние: {mood}")

if location == "":
    print("Предупреждение: место съёмки не указано")
else:
    print(f"Место съёмки: {location}")

if description == "":
    print("Примечание: описание не заполнено")
elif len(description) < 10:
    print("Описание короткое — попробуйте добавить больше деталей")
else:
    print(f"Описание принято ({len(description)} символов)")

today = date.today()
print(f"\nДата добавления: {today}")
print(f"Фотография '{title}' сохранена в категории '{category}'")
print(f"Настроение: {mood}")
print("Запись добавлена в вашу галерею воспоминаний")