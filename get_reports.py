import pandas as pd
from dotenv import load_dotenv
import os
import httpx
import sys
from enum import Enum


class TableHeader(Enum):
    SKU = 'Артикул'
    REASON = 'Обоснование'
    PAYMENT = 'Выплаты'
    DELIVERY = 'Доставка'
    DATE = 'Дата'
    CURRENCY = 'Валюта'


# Формирование переменных
load_dotenv()
WB_API_KEY=os.getenv("WB_API_KEY")

if WB_API_KEY is None:
    print('Проверьте наличие файла .env и переменной WB_API_KEY в нем!')
    sys.exit()


from_date = sys.argv[1]
till_date = sys.argv[2]

# Параметры для запроса к wb

wb_url="https://finance-api.wildberries.ru/api/finance/v1/sales-reports/detailed"
wb_header = {"Authorization": WB_API_KEY}

req = {
  "dateFrom": f"2026-{from_date}",
  "dateTo": f"2026-{till_date}",
  "limit": 21100,
  "rrdId": 0,
  "period": "weekly",
  # "fields": [
    # "rrdId",
    # "nmId",
    # "docTypeName",
    # "retailAmount",
    # "acquiringFee",
    # "srid"
  # ]
}

# Запрос данных, и их преобразование в объект python
response = httpx.post(url=wb_url, headers=wb_header, json=req)
reports = response.json()


rows = []


# Функция для изввлечения значений из словаря
def add_rows_to_arr(current_row, search_data):
    row = []

    for data_unit in search_data:
        row.append(current_row.get(data_unit))

    return row


for record in reports:

    rows.append(add_rows_to_arr(record,
            [
            'vendorCode',           # Артикул продавца
            'sellerOperName',       # Обоснование для выплаты
            'forPay',               # Выплата за товар продавцу
            'deliveryService',      # Плата за доставку
            'orderDt',              # Время создания заказа
            'currency']             # Валюта
        ))



df = pd.DataFrame(
    rows,
    columns=[
        TableHeader.SKU.value,
        TableHeader.REASON.value,
        TableHeader.PAYMENT.value,
        TableHeader.DELIVERY.value,
        TableHeader.DATE.value,
        TableHeader.CURRENCY.value,
    ],
)

df[TableHeader.DATE.value] = (pd.to_datetime(df[TableHeader.DATE.value], utc=True) + pd.Timedelta(hours=3)).dt.date

# Сохранение таблицы
with pd.ExcelWriter("data.xlsx", engine="openpyxl", date_format="DD.MM.YYYY") as writer:
    df.to_excel(writer, index=False)


print('Данные записаны в data.xslx')
