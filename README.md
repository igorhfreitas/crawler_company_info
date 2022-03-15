# crawler_company_info

This project intend to search over wikipedia or goggle Knowledge Painel for a company and extract the information existent in the knowledge painel, like CEO, founder, Address, Size and so on.

The idea first was to use Wikipedia with BeautifulSoup4 as crawler engine, but was discorvered that pandas provide a good abstraction to extract tables from html and this simplified the work a lot. Then the wikipedia do not have information for many companies since the infos comes as crowd based, so the best alternative was to look over Google Knowledge Painel, but even with the code working, it was unlikely to use in a production environmet (as a CRM side service to update customers info) with millions of clients for obvious reasons.
