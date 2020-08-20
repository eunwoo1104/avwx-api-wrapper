"""MIT License

Copyright (c) 2020 eunwoo1104

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import requests
import aiohttp
from . import error


class Connection:
    """
    Connection of this wrapper.
    I highly recommend not to use this but use via Client.
    :param token: Your AVWX REST API Token.
    """
    base_url = "https://avwx.rest/api"

    def __init__(self, token):
        self.token = token

    def request_avwx(self, report, location, options="info", airport: bool = True, reporting: bool = True, format="json", onfail="cache"):
        header = {"Authorization": self.token}
        params = {"options": options, "airport": airport, "reporting": reporting, "format": format, "onfail": onfail}
        resp = requests.get(self.base_url+f"/{report}/{location.upper()}", headers=header, params=params)
        if resp.status_code != 200:
            # Since info about resp code is not provided at docs, let's just raise exception for now.
            raise error.RequestFailed(resp, resp.status_code)
        if format == "json":
            return resp.json()
        else:
            return resp.text

    async def async_request_avwx(self, report, location, options="info", airport: bool = True, reporting: bool = True, format="json", onfail="cache"):
        header = {"Authorization": self.token}
        params = {"options": options, "airport": airport, "reporting": reporting, "format": format, "onfail": onfail}
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url+f"/{report}/{location.upper()}", headers=header, params=params) as resp:
                if resp.status != 200:
                    # Since info about resp code is not provided at docs, let's just raise exception for now.
                    raise error.RequestFailed(resp, resp.status)
                if format == "json":
                    return await resp.json()
                else:
                    return await resp.text()
