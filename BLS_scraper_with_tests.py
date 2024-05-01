import requests
from bs4 import BeautifulSoup
import os
import time
import unittest
from unittest.mock import patch, mock_open

# Download a single xlsx based on SeriesId
def DownloadTable(folder, Industry, SeriesId, maxRetryNum = 5):
    
    url = "https://data.bls.gov/pdq/SurveyOutputServlet"
    
    file_name = f"{folder}/{Industry}_{SeriesId}.xlsx"
    
    if os.path.exists(file_name):
        return
    
    payload = {
        "request_action": "get_data",
        "reformat": "true",
        "from_results_page": "true",
        "years_option": "specific_years",
        "delimiter": "comma",
        "output_type": "multi",
        "periods_option": "all_periods",
        "output_view": "data",
        "output_format": "excelTable",
        "original_output_type": "default",
        "annualAveragesRequested": "false",
        "series_id": SeriesId
    }

    headers = {
        "Host": "data.bls.gov",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
        "Origin": "https://data.bls.gov",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://data.bls.gov/pdq/SurveyOutputServlet",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "JSESSIONID=45F1806DBD17D2ACBC57D381AA064BD0._t4_08v; _ga=GA1.3.1064385307.1714021826; _gid=GA1.3.505043060.1714021826; nmstat=84319282-45f4-ed8f-18ba-eabd199264f0; _gid=GA1.2.1155707569.1714022122; _ga=GA1.1.1064385307.1714021826; _ga_CSLL4ZEK4L=GS1.1.1714021826.1.1.1714022878.0.0.0"
    }

    retry = 0
    while retry < maxRetryNum:
        try:
            response = requests.post(url, data=payload, headers=headers, timeout=10)
            if response.status_code == 200:
                with open(file_name, "wb") as f:
                    f.write(response.content)
                print(file_name,'Download Complete')
                return
            else:
                retry += 1
                print(f'Retrying {retry} / {maxRetryNum}...')
                time.sleep(5)
                
        except Exception as e:
            retry += 1
            print(f'Retrying {retry} / {maxRetryNum}... for {e}')
            time.sleep(5)

# Get the query page results under filter conditions -- get the corresponding SuperSector, SeriesId
def getTableInfos():
    cookies = {
        'JSESSIONID': 'E6BBDD7514B5B9D2F61E4F53854D2CC4._t4_08v',
        '_ga': 'GA1.3.590876299.1713971271',
        '_gid': 'GA1.3.1697168608.1713971271',
        'nmstat': '4128358f-b942-bea6-4d9a-8918ed073014',
        'touchpoints': 'true',
        '__gsas': 'ID=f0bf28e5a1716d10:T=1714013917:RT=1714013917:S=ALNI_Madda5URvD1tx4AAO62lJ6EFPUu7g',
        '_ga_CSLL4ZEK4L': 'GS1.1.1714061954.8.1.1714063651.0.0.0',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,be;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.bls.gov',
        'Referer': 'https://www.bls.gov/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = [
        ('series_id', 'CES0500000011'),
        ('series_id', 'CES0600000011'),
        ('series_id', 'CES1000000011'),
        ('series_id', 'CES2000000011'),
        ('series_id', 'CES3000000011'),
        ('series_id', 'CES3100000011'),
        ('series_id', 'CES3200000011'),
        ('series_id', 'CES0800000011'),
        ('series_id', 'CES4000000011'),
        ('series_id', 'CES4142000011'),
        ('series_id', 'CES4200000011'),
        ('series_id', 'CES4300000011'),
        ('series_id', 'CES4422000011'),
        ('series_id', 'CES5000000011'),
        ('series_id', 'CES5500000011'),
        ('series_id', 'CES6000000011'),
        ('series_id', 'CES6500000011'),
        ('series_id', 'CES7000000011'),
        ('series_id', 'CES8000000011'),
        ('survey', 'lf'),
        ('htmlpage', 'cesbtab3.htm'),
        ('format', ''),
        ('html_tables', ''),
        ('delimiter', ''),
        ('catalog', ''),
        ('print_line_length', ''),
        ('lines_per_page', ''),
        ('row_stub_key', ''),
        ('year', ''),
        ('date', ''),
        ('net_change_start', ''),
        ('net_change_end', ''),
        ('percent_change_start', ''),
        ('percent_change_end', ''),
    ]

    response = requests.post('https://data.bls.gov/pdq/SurveyOutputServlet', headers=headers, cookies=cookies, data=data, timeout=15)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    tables = soup.find_all('table',{'class':'catalog'})
    index = []
    for table in tables:
        Industry,SeriesId = None,None
        trs = table.find_all('tr')
        for tr in trs:
            if tr.find('th'):
                key = tr.find('th').text.strip()
                value = tr.find('td').text.strip()
                if key == 'Industry:':
                    Industry = value
                elif key == 'Series Id:':
                    SeriesId = value
        index.append((Industry,SeriesId))

    return index


def main():
    index = getTableInfos()
    folder = 'Average_Weekly_Earnings'
    os.makedirs(folder,exist_ok=True)
    for Industry,SeriesId in index:
        DownloadTable(folder,Industry,SeriesId)


if __name__ == '__main__':
    main()


# Unit tests for the DownloadTable function

class TestDownloadTable(unittest.TestCase):
    @patch('os.path.exists')
    def test_file_already_exists(self, mock_exists):
        mock_exists.return_value = True
        result = DownloadTable('test_folder', 'test_industry', '123456')
        self.assertIsNone(result, "Function should return None if file already exists")

    @patch('os.path.exists')
    @patch('requests.get')
    def test_download_success(self, mock_get, mock_exists):
        mock_exists.return_value = False
        response = requests.Response()
        response.status_code = 200
        mock_get.return_value = response
        with patch("builtins.open", mock_open()):
            result = DownloadTable('test_folder', 'test_industry', '123456')
            self.assertIsNone(result, "Function should successfully download and return None")

    @patch('os.path.exists')
    @patch('requests.get')
    def test_retry_logic(self, mock_get, mock_exists):
        mock_exists.return_value = False
        response = requests.Response()
        response.status_code = 404  # Not found
        mock_get.side_effect = [response] * 5  # Simulate retries
        with patch("builtins.open", mock_open()):
            result = DownloadTable('test_folder', 'test_industry', '123456', maxRetryNum=5)
            self.assertIsNone(result, "Function should retry 5 times and return None")

if __name__ == '__main__':
    unittest.main()
