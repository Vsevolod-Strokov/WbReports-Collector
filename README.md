# WbReports-Colllector 

Это скрипт, который формирует отчёты wildberries о проданных товарах в удобном формате (xslx) для расчёта прибыли.

### Пример:

<img width="1922" height="413" alt="image" src="https://github.com/user-attachments/assets/99f66f77-de99-4661-85e8-019aa726238a" />

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


# Формирование файла с API. После выполнения команды подставьте свой API ключ в .env
mv .env_sample .env
```


# Инструкция по использованию

```
# Необходимо запустить скрипт с двумя аргументами:
# начало и конец временного диапазона сбора отчётов, например:

python get_reports.py 06-30 07-15

# После этого будет сформирована выжимка из отчётов в файле data.xlsx

```

# Выбор своих полей в отчётов 

Вы можете отредактировать обрабатываемые поля под себя, опредилив их названия при помощи официальной документации wb:

[Ссылка на api wildberries](https://dev.wildberries.ru/docs/openapi/financial-reports-and-accounting#tag/financialReports/operation/postV1SalesReportsList)
