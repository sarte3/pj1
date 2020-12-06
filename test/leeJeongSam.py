import requests
from bs4 import BeautifulSoup

url = 'https://www.alexa.com/topsites'
recvd = requests.get(url)
dom = BeautifulSoup(recvd.text, 'lxml')
for i in range(2, 52, 1):
    ranks = dom.select('#alx-content > div.row-fluid.TopSites.Alexarest > section.page-product-content.summary > span > span > div > div > div.listings.table > div:nth-child({}) > div:nth-child(1)'.format(i))
    sites = dom.select('#alx-content > div.row-fluid.TopSites.Alexarest > section.page-product-content.summary > span > span > div > div > div.listings.table > div:nth-child({}) > div:nth-child(2) a'.format(i))
    dtoss = dom.select('#alx-content > div.row-fluid.TopSites.Alexarest > section.page-product-content.summary > span > span > div > div > div.listings.table > div:nth-child({}) > div:nth-child(3)'.format(i))
    dppvs = dom.select('#alx-content > div.row-fluid.TopSites.Alexarest > section.page-product-content.summary > span > span > div > div > div.listings.table > div:nth-child({}) > div:nth-child(4)'.format(i))
    otfss = dom.select('#alx-content > div.row-fluid.TopSites.Alexarest > section.page-product-content.summary > span > span > div > div > div.listings.table > div:nth-child({}) > div:nth-child(5)'.format(i))
    tslis = dom.select('#alx-content > div.row-fluid.TopSites.Alexarest > section.page-product-content.summary > span > span > div > div > div.listings.table > div:nth-child({}) > div:nth-child(6)'.format(i))


    for r, s, d, p, o, t in zip(ranks, sites, dtoss, dppvs, otfss, tslis):
        rank = r.text
        site = s.text
        dtos = d.text
        dppv = p.text
        otfs = o.text
        tsli = t.text
        print(rank, site, dtos, dppv, otfs, tsli)
