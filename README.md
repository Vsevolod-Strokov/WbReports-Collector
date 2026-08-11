WbReports-Colllector - это скрипт, который формирует отчёты о проданных товаров в удобном формате для расчёта прибыли.



# Инструкция по установке

```
# Загрузка репозитория
git clone https://github.com/Vsevolod-Strokov/WbReports-Collector.git

# Активация виртуального окружения 
cd WbReports-Colllector
python -m venv venv
source venv/bin/activate

# Установка необходимых библиотек
pip install -r requirements.txt


# Подставьте свой API ключ в .env
mv .env_sample .env
```


# Инструкция по использованию

```
# Необходимо запустить скрипт с аргументами 
# начала и конца временного диапазона сбора отчётов, например:
python get_reports.py 06-30 07-15

# После этого будет сформирована выжимка из отчётов в файле data.xlsx

```

# Документация 

Вы можете отредактировать поля под себя, опредилив их при помощи официальной документации wb:

[Ссылка на api wildberries](https://dev.wildberries.ru/docs/openapi/financial-reports-and-accounting#tag/financialReports/operation/postV1SalesReportsList)
