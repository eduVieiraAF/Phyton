import http.client

conn = http.client.HTTPSConnection("investing-cryptocurrency-markets.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "5375f1194amshb057f0fe5663137p14cc2bjsna7ae5ec520d1",
    'X-RapidAPI-Host': "investing-cryptocurrency-markets.p.rapidapi.com"
    }

conn.request("GET", "/coins/list?edition_currency_id=12&time_utc_offset=28800&lang_ID=1&sort=PERC1D_DN&page=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



