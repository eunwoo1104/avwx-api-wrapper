import avwx_api # place avwx_api folder to your project folder.

token = "Your Token Here" # https://account.avwx.rest/manage
metar = avwx_api.client.Client(token).get_metar("RKSI")
print(metar.altimeter) # Prints Altimeter Value of Incheon Intl Airport
