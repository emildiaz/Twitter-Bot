import random
import requests
from bs4 import BeautifulSoup  

def getSoup(page):
    url = f'https://www.goodreads.com/search?page={page}&q=quotes+harry+potter&qid=RgXERhQx6B&search%5Bfield%5D=on&search_type=quotes&tab=quotes&utf8=%E2%9C%93'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def getQuotes(soup):
    quotes = soup.find_all('div', {'class':'quoteText'})
    return quotes 

def formatAuthor(raw_author):
    try:
        name = raw_author[:raw_author.find('(')].strip()
        book = raw_author[raw_author.find('('):].strip()
        author = f'{name}\n\n{book}'
    except:
        author = raw_author
    finally:
        return author
    
def main():
    validQuote = False
    
    while not validQuote:
        page = random.randrange(1, 33)
        soup = getSoup(page)
        quotes = getQuotes(soup)
        raw_quote = random.choice(quotes).text
    
        quote = raw_quote[:raw_quote.rfind('"')+1].strip()
        raw_author = raw_quote[raw_quote.rfind('—')+1:].strip()
        author = formatAuthor(raw_author)
        
        q_and_a = f'{quote}\n{author}'

        #check to see if fit in twitter character limit
        if len(q_and_a) <= 280:
            validQuote = True
    
    return (q_and_a)

if __name__ == '__main__':
    main()
