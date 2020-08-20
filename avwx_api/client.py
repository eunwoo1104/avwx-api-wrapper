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
from . import connection, model


class Client:
    """
    Client of this wrapper.
    :param token: Your AVWX REST API Token.
    """
    def __init__(self, token):
        self.conn = connection.Connection(token)

    def get_metar(self, location, options="info", airport: bool = True, reporting: bool = True, format="json", onfail="cache") -> model.BasicModel:
        """
        Returns parsed response. Information about params is available at https://avwx.docs.apiary.io/#reference/0/metar/get-metar-report.
        :param location: ICAO Airport Code.
        :param options: info, translate, summary, speech | Default `info`.
        :param airport: Default `True`.
        :param reporting: Default `True`.
        :param format: json, xml, yaml | Default `json`.
        :param onfail: cache, error | Default `cache`.
        :return: avwx_api.model.BasicModel
        """
        resp = self.conn.request_avwx("metar", location, options, airport, reporting, format, onfail)
        raw_resp = resp
        raw = resp["raw"]
        timestamp = resp["meta"]["timestamp"]
        altimeter = resp["altimeter"]["value"]
        clouds = resp["clouds"]
        visibility = resp["visibility"]["value"]
        wind_dir = resp["wind_direction"]["value"]
        wind_spd = resp["wind_speed"]
        wind_gust = resp["wind_gust"]
        remarks = resp["remarks"]
        drewpoint = resp["dewpoint"]["value"]
        temp = resp["temperature"]["value"]
        units = resp["units"]
        result = model.BasicModel(raw_resp, raw, timestamp, altimeter, clouds, visibility, wind_dir, wind_spd, wind_gust, remarks, drewpoint, temp, units)
        return result

    async def async_get_metar(self, location, options="info", airport: bool = True, reporting: bool = True, format="json", onfail="cache") -> model.BasicModel:
        """
        Async version of get_metar. Returns parsed response. Information about params is available at https://avwx.docs.apiary.io/#reference/0/metar/get-metar-report.
        :param location: ICAO Airport Code.
        :param options: info, translate, summary, speech | Default `info`.
        :param airport: Default `True`.
        :param reporting: Default `True`.
        :param format: json, xml, yaml | Default `json`.
        :param onfail: cache, error | Default `cache`.
        :return: avwx_api.model.BasicModel
        """
        resp = await self.conn.async_request_avwx("metar", location, options, airport, reporting, format, onfail)
        raw_resp = resp
        raw = resp["raw"]
        timestamp = resp["meta"]["timestamp"]
        altimeter = resp["altimeter"]["value"]
        clouds = resp["clouds"]
        visibility = resp["visibility"]["value"]
        wind_dir = resp["wind_direction"]["value"]
        wind_spd = resp["wind_speed"]["value"]
        wind_gust = resp["wind_gust"]
        remarks = resp["remarks"]
        drewpoint = resp["dewpoint"]["value"]
        temp = resp["temperature"]["value"]
        units = resp["units"]
        result = model.BasicModel(raw_resp, raw, timestamp, altimeter, clouds, visibility, wind_dir, wind_spd, wind_gust, remarks, drewpoint, temp, units)
        return result
