#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
from bs4 import BeautifulSoup

# for authentication
headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

def get_reviews(keyword, n):
    """
    Get product review info for top n products with the given keyword from Amazon (warning: n > 5 takes a long time)
    
    Args:
        keyword (str): product to search for
        n (int): number of products to get reviews from
    
    Returns:
        product_dict (dict[str:[str]]): product names (keys) mapped to lists review info (values)
    
    """
    # compile product names and review info here
    product_dict = {}

    
    # search for product on amazon and get html response
    url = f'https://www.amazon.com/s?k={keyword}'
    html = requests.get(url, headers=headers).text
    
    
    # get the first page of products returned by amazon search
    products = BeautifulSoup(html).find_all(class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
    
    
    # USE THIS CLASS FOR REVIEW TITLES
    titles = 'a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold'
    
    # USE THIS CLASS FOR REVIEW TEXT 
    # (doesn't get the entire review if it's too long, would have to visit each review's page making it way too slow)
    texts = 'a-size-base review-text'
    
    # get top n products
    i = 1
    for product in products:
        if i > n:
            break
            
        href = product.attrs['href']
        product_url = f'https://www.amazon.com/{href}'
        product_html = requests.get(product_url, headers=headers).text
        
        product_title = BeautifulSoup(product_html).find(id='productTitle').text.strip()
        review_data = []
        
        # pass either titles or texts to 'class_=' param
        reviews = BeautifulSoup(product_html).find_all(class_=titles)
        for r in reviews:
            review_data.append(r.text.strip())
            
        product_dict[product_title] = review_data
        
        i += 1
            
    return product_dict
        
    
get_reviews('keyboard', 5)

