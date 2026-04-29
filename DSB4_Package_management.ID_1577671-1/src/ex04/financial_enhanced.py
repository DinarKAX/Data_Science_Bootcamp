from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By    
from bs4 import BeautifulSoup
import sys

def init():
    """
    Инициализация веб-драйвера и загрузка страницы с финансовыми данными
    Returns:
        tuple: (html код страницы, тикер, аргумент) или (None, None, None) при ошибке
    """

    args = sys.argv
 
    if len(args) != 3:        
        return None, None, None
    tiker = args[1]  
    argum = args[2]  

    url = f"https://finance.yahoo.com/quote/{tiker}/financials"

    opts = Options()
    opts.headless = True  
    opts.add_argument("--disable-blink-features=AutomationControlled")  
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=opts)
    try:
        driver.get(url)                
    except:
        driver.quit()
        print("Uncorect tiker")
        return None, None, None
    
    try:
        agree = driver.find_element(By.CSS_SELECTOR, 'button[name="agree"]')
        agree.click()
    except: 
        pass 
    
    # Получаем HTML код загруженной страницы
    html = driver.page_source
    driver.quit()  
    
    # Возвращаем результаты если HTML получен успешно
    if html: 
        return html, tiker, argum
    return None, None, None
    
def get_values(soup: BeautifulSoup, arg:str):
    # Парсит финансовые данные из HTML страницы

    res = []  # Список для хранения результатов
    arg = arg.strip()  
    row = None  
    
    # Ищем все строки финансовой таблицы
    row_title = soup.find_all("div", class_="row lv-0 yf-t22klz")
    
    # Если строки не найдены, выводим сообщение и возвращаем пустой список
    if not row_title:
        print("Undefine argument")
        return res
    
    # Ищем строку с нужным финансовым показателем
    for i in row_title:
        if i.find("div", class_="rowTitle yf-t22klz").text.strip() == arg:
            row = i  # Сохраняем найденную строку
    
    if not row:
        return res
    
    columns_0 = row.find_all('div', class_ ="column yf-t22klz")
    columns_1 = row.find_all('div', class_ = "column yf-t22klz alt")

    for i in range(len(columns_0)):
        res.append(columns_0[i].text.strip())  
        res.append(columns_1[i].text.strip())   
    
    res.append(columns_0[-1].text.strip())
    return res

def main():
    # Инициализируем и получаем данные
    html, tiker, arg = init()
    if html == None: 
        return  
    
    soup = BeautifulSoup(html, 'html.parser')
    
    values = get_values(soup=soup, arg=arg)
    
    print(tuple([arg] + values))

if __name__=="__main__":
    main()