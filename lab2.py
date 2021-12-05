# ФИО: Фам Нгок Хунг
# № Группа 6112
# Вариант 112

import json
import re
import argparse
from tqdm import tqdm


def lab2_app():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Get path file input')
    parser.add_argument('output', help='Get path file output')
    args = parser.parse_args()

    class Validator:
        """
        Объект класса Validator
        Он нужен для того, что проверить данные валидными или нет
        """

        def __init__(self, __person):
            self.person = __person

        def check_telephone(self) -> bool:
            """
            Выполняет проверку корректности номера телефона
            Если телефон не иммет вид '+7-(111)-222-33-44' то будет возвращено False

            Параметры
            ---------
              telephone:
                параметр для проверки корректности

            Return
            ------
              bool:
                Булевый результат на коррестность
            """
            if type(self.person['telephone']) != str:
                return False
            pattern = '\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}'
            if re.match(pattern, self.person['telephone']):
                return True
            return False

        def check_height(self) -> bool:
            """
            Выполняет проверку корректности массы
            Если масса нет строки вида '1.22' или больше '2.51' то будет ворвращено False

            Параметры
            ---------
              height : str
                Параметр для проверки корректности

            Return
            ------
              bool:
                Булевый результат на коррестность
            """
            pattern = '[1-2]\.\d{2}'
            if re.match(pattern, str(self.person['height'])) is not None:
                if float(self.person['height']) < 2.51:
                    return True
            return False

        def check_passport(self) -> bool:
            """
              Выполняет проверку корректности номера паспорта
              Если номер паспорта не состоит из последовательности 6 цифр то возвращено False

              Параметры
              ---------
                passport : int
                  Целое число для проверки корректности

              Return
              ------
                 bool:
                   Булевый результат на корректность
              """
            if type(self.person['passport_number']) != int:
                return False
            if len(str(self.person['passport_number'])) == 6:
                return True
            return False

        def check_inn(self) -> bool:
            """
            Выполняет проверку корректности ИНН
            Если ИНН не состоит из последовательности 12 цифр то возвращено False

            Параметры
            ---------
              inn : str
                Строка для проверки корректности

            Return
            ------
              bool:
                Булевый результат на корректность
            """
            if type(person['inn']) != str:
                return False
            pattern = '\d{12}'
            if re.match(pattern, person['inn']):
                return True
            return False

        def check_address(self) -> bool:
            """
              Выполняет проверку корректности адреса
              Если адрес нет строки или указан не в формате "улица пробел номер дома" то возвращено False

              Параметры
              ---------
                address:
                  Параметр для проверки корректности

              Return
              ------
                bool:
                  Булевый результат на корректность
            """
            pattern = '[а-яА-Я.\s\d-]+\s+[0-9]+$'
            if type(self.person['address']) != str:
                return False
            if re.match(pattern, self.person['address']):
                return True
            return False

        def check_work_exp(self) -> bool:
            """
              Выполняет проверку типа данных параметра
              Если пераметр не имеет тип данных int то возвращено False

              Параметры
              ---------
                number:
                  Параметр для проверки типа данных

              Return
              ------
                bool:
                  Булевый результат на корректность
            """
            if type(self.person['work_experience']) == int and int(self.person['work_experience']) >= 0 and int(self.person['work_experience']) <= 60:
                return True
            return False

        @property
        def check_university(self) -> bool:
            """
              Выполняет проверку типа данных параметра
              Если пераметр не имеет тип данных str возвращено False

              Параметры
              ---------
                string:
                  Параметр для проверки типа данных

              Return
              ------
                bool:
                  Булевый результат на корректность
            """
            pattern = '[а-яА-Я\.\- ]*([Уу]ниверситет|[Гг]осуниверситет|им\.|[Ии]нститут|МФТИ|политех|МГТУ|[аА]кадеми[ия]|СПбГУ|имени)[а-яА-Я\.\- ]*'
            if re.match(pattern, self.person['university']):
                return True
            return False

        def check_political_view(self) -> bool:
            """
              Выполняет проверку типа данных параметра
              Если пераметр не имеет тип данных str возвращено False

              Параметры
              ---------
                string:
                  Параметр для проверки типа данных

              Return
              ------
                bool:
                  Булевый результат на корректность
            """
            if type(self.person['political_views']) != str:
                return False
            return True

        def check_world_view(self) -> bool:
            """
              Выполняет проверку типа данных параметра
              Если пераметр не имеет тип данных str возвращено False

              Параметры
              ---------
                string:
                  Параметр для проверки типа данных

              Return
              ------
                bool:
                  Булевый результат на корректность
            """
            if type(self.person['worldview']) != str:
                return False
            return True

    data = json.load(open(args.input, encoding='windows-1251'))

    true_data = list()
    telephone = 0
    height = 0
    passport = 0
    address = 0
    work_experience = 0
    inn = 0
    university = 0
    worldview = 0
    political_view = 0
    with tqdm(total=len(data)) as progressbar:
        for person in data:
            check_person = Validator(person)
            temp = True
            if not check_person.check_telephone():
                telephone += 1
                temp = False
            if not check_person.check_height():
                height += 1
                temp = False
            if not check_person.check_inn():
                inn += 1
                temp = False
            if not check_person.check_passport():
                passport += 1
                temp = False
            if not check_person.check_address():
                address += 1
                temp = False
            if not check_person.check_work_exp():
                work_experience += 1
                temp = False
            if not check_person.check_university:
                university += 1
                temp = False
            if not check_person.check_political_view():
                political_view += 1
                temp = False
            if not check_person.check_world_view():
                worldview += 1
                temp = False
            if temp:
                true_data.append(person)
            progressbar.update(1)

    out_put = open(args.output, 'w', encoding='windows-1251')
    beauty_data = json.dumps(true_data, ensure_ascii=False, indent=4)
    out_put.write(beauty_data)
    out_put.close()


    print(f'Число валидных записей: {len(true_data)}')
    print(f'Число невалидных записей: {len(data) - len(true_data)}')
    print(f'  - Число невалидных номеров телефона:  {telephone}')
    print(f'  - Число невалидных масс: {height}')
    print(f'  - Число невалидных ИНН: {inn}')
    print(f'  - Число невалидных номеров паспорта: {passport}')
    print(f'  - Число невалидных университетов: {university}')
    print(f'  - Число невалидных рабочих стажей: {work_experience}')
    print(f'  - Число невалидных политических взглядов: {political_view}')
    print(f'  - Число невалидных мировоззрений: {worldview}')
    print(f'  - Число невалидных адрессов: {address}')
    print('\n*Замечание: каждый человек может быть иметь несколько невалидых записей')
# help(Validator)
# !autopsy8 - - in -place - -aggressive - -aggressive lab2.py
