headlines = [
"Local Bear Eaten by Man"
"Legislature Announce new law",
"Peasant Discovers Violence Inherent in System",
" Cat Rescues Fireman Stuck in Tree",
"Brave Knight Runs Away",
"Paperbook Review: Totally Triffic"]

news_ticker = ""

 
for news in headlines:
	news_ticker += news + " "
	if len(news_ticker) > 140:
		news_ticker = news_ticker[:140]
print(news_ticker)
print(len(news_ticker))
