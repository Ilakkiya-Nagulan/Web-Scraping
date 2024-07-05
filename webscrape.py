import pandas as pd
from bs4 import BeautifulSoup

def read_and_parse_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'lxml')
    return soup

def extract_product_info(soup):
    products = []
    target_class = 'puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-vm4sjunze1lk62qzghq959ihey s-latency-cf-section puis-card-border'
    divs = soup.find_all('div', class_=target_class)
    
    for div in divs:
        product_name = div.find('span', class_='a-size-medium a-color-base a-text-normal')
        product_price = div.find('span', class_='a-price-whole')
        product_reviews = div.find('span', class_='a-icon-alt')

        product_info = {
            'Product Name': product_name.text.strip() if product_name else " ",
            'Product Price': product_price.text.strip() if product_price else " ",
            'Product Reviews': product_reviews.text.strip() if product_reviews else " "
        }
        products.append(product_info)
    
    return products

def save_to_excel(products, file_path='Products.xlsx'):
    df = pd.DataFrame(products)
    df.to_excel(file_path, index=False, engine='openpyxl')

def main():
    html_file_path = 'Amazon.html'
    soup = read_and_parse_html(html_file_path)
    products = extract_product_info(soup)
    save_to_excel(products)

if __name__ == "__main__":
    main()
