from InvestopediaApi import ita

#Everything done through the Account
client = ita.Account('kevin.f.liu2012@gmail.com', '789kevv789')
status = client.get_portfolio_status()
print(status)

# Important function:
# ita.Account.get_portfolio_status
# ita.Account.get_current_securities
# ita.Account.get_open_trades
# ita.get_quote("Stringticker")
# Trading:
# client.trade("ticker", action, INTamount)