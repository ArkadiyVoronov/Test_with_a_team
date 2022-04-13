# Автотесты для сайта https://berpress.github.io/react-shop/

---

https://img.shields.io/github/issues-pr-closed/ArkadiyVoronov/Test_with_a_team.svg

---

# Локальный запуск

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
В текущей реализации: 
* trailing-whitespace - обрезает пробелы
* check-json - проверяет файлы формата json
* check-yaml - проверяет файлы формата yaml
* debug-statements - проверяет наличие импорта отладчика и вызовов py 37+ breakpoint() в исходном коде python.
* requirements-txt-fixer - сортирует записи в requirements.txt
* flake8 - обеспечивает согласованность стилей в проекте

---

Чек-лист команды:
+ [x] договорились о работе в ветках, наименование фича_бранч
+ [x] общение в канале 
+ [x] сообщаем о MR, 
+ [x] проходим и проводим ревью
+ [x] решаем конфликты

Чек-лист нашего проекта:
+ [ ] readMe, в процессе
+ [ ] добавить ci\cd
+ [x] добавить линтер
+ [ ] добавить логи
+ [ ] добавить отчеты

