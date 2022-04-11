# Автотесты для сайта https://rss-litovsky.vercel.app/

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

Проверка кода
```
pre-commit https://pre-commit.com/
```angular2html
pip install pre-commit
pre-commit install
```

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
