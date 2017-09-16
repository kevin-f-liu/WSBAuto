from InvestopediaApi import ita

client = ita.Account('kevin.f.liu2012@gmail.com', '789kevv789')

print(client.get_portfolio_status())
