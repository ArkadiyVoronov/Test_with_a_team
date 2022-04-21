Автотесты для сайта https://berpress.github.io/react-shop/

[![Pytest Selenium Allure status](https://github.com/ArkadiyVoronov/Test_with_a_team/actions/workflows/pytest_selenium_allure.yml/badge.svg)](https://github.com/ArkadiyVoronov/Test_with_a_team/actions/workflows/pytest_selenium_allure.yml)


Локальный запуск

Для локального запуска необходим Python версии 3.8 и выше
При первом запуске надо создать виртуальное окружение

```angular2html
python3 -m venv env
```

Активировать виртуальное окружение

```angular2html
source env/bin/activate
```

Нужно установить зависимости проекта

```angular2html
pip3 install -r requirements.txt
```

Запуск тестов

```angular2html
pytest
```
---

Проверка кода организована через pre-commit
Подробнее https://pre-commit.com/

---

CI организован через https://semgrep.dev/

---
Логирование реализовано через пакет logging
Подробнее https://docs.python.org/3/library/logging.html

---
[Allure-report](https://arkadiyvoronov.github.io/Test_with_a_team/)
---

Чек-лист команды:
+ [x] договорились о работе в ветках, наименование фича_бранч
+ [x] общение в канале 
+ [x] сообщаем о MR 
+ [x] проходим и проводим ревью
+ [x] решаем конфликты

Чек-лист нашего проекта:
+ [ ] readMe, в процессе
+ [x] добавить ci\cd
+ [x] добавить линтер
+ [x] добавить логи
+ [x] добавить отчеты

