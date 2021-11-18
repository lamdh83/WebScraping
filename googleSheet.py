# 1. https://console.cloud.google.com/ => tao project moi hoac su dung project cu
# 2. Tu Search products and resoureces tim theo:
    # Google Drive API => Enable
    # Google Sheets API => Enable
# 3. Tab APIs&Services => Credentials => CREATE CREDENTIALS => Services account
# 4. Chon du an moi tao o buoc 3 => KEYS => ADD KEY => Create new Key => Json => create

import gspread
from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'googlesheet.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)

url = 'https://docs.google.com/spreadsheets/d/10EkgU1h7l_W0j4c500na4yoN8WlEUsv_nzIxp_IRutQ/edit#gid=0'
workbook = gc.open_by_url(url)

sheet = workbook.worksheet('Trang tính1')
stt = sheet.col_values(1)[2:]
vnpt = sheet.col_values(3)[2:]

print(stt, '/ ', vnpt)