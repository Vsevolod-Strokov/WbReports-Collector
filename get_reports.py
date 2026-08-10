import pandas as pd
from dotenv import load_dotenv
import os
import httpx
import sys


wb_url="https://finance-api.wildberries.ru/api/finance/v1/sales-reports/detailed"

load_dotenv()
WB_API_KEY=os.getenv("WB_API_KEY")

if WB_API_KEY is None:
    print('Проверьте наличие файла .env и переменной WB_API_KEY в нем!')
    sys.exit()

wb_header = {"Authorization": WB_API_KEY}


from_date = sys.argv[1]
till_date = sys.argv[2]


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

response = httpx.post(url=wb_url, headers=wb_header, json=req)
reports = response.json()


rows = []


def add_rows_to_arr(current_row, search_data):
    row = []
    for data_unit in search_data:
        value = current_row.get(data_unit)
        row.append(value)

    return row


for record in reports:

    rows.append(add_rows_to_arr(record,[
            'vendorCode',
            'sellerOperName',
            'forPay',
            'deliveryService',
            'orderDt',
            'currency']
        ))

df = pd.DataFrame(rows, columns=["Артикул", "Обоснование", "Выплата", "Доставка", "Дата", "Валюта"])
# df.to_excel("data.xlsx", index=False)


df["Дата"] = (pd.to_datetime(df["Дата"], utc=True) + pd.Timedelta(hours=3)).dt.date


with pd.ExcelWriter("data.xlsx", engine="openpyxl", date_format="DD.MM.YYYY") as writer:
    df.to_excel(writer, index=False)


print('Данные записаны в data.xslx')
