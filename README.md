WbReports-Colllector - это скрипт, который формирует отчёты о проданных товаров в удобном формате для расчёта прибыли.



# Инструкция по установке

```
# Загрузка репозитория
git clone https://github.com/Vsevolod-Strokov/WbReports-Colllector.git

# Активация виртуального окружения 
cd wbreports-colllector
python -m venv venv
source venv/bin/activate

# Установка необходимых библиотек
pip install -r requirements.txt


# Подставьте свой API ключ в .env
mv .env_sample .env
```


# Инструкция по использованию

```
#Необходимо запустить скрипт с аргументами начала и конца временного диапазона сбора отчётов, например:
python get_reports.py 06-30 07-15

# После этого будет сформирована выжимка из отчётов в файле data.xslx
```
