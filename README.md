# avwx-api-wrapper
> Unofficial AVWX REST API Wrapper

Both normal and async version is included.  
Feel free to create PR or Issue.

## Example
```python
import avwx_api # place avwx_api folder to your project folder.

token = "Your Token Here" # https://account.avwx.rest/manage
metar = avwx_api.client.Client(token).get_metar("RKSI")
print(metar.altimeter) # Prints Altimeter Value of Incheon Intl Airport
```

## Some Notes
- Docs not available for now.  
- Since I couldn't find information about response code, this wrapper will raise exception if status code is not 200.
- This is the first time I created API Wrapper, so some of the codes might have problems. If so, please report via Issue or PR.
