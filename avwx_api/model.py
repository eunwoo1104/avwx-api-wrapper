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


class BasicModel:
    """
    Model of this wrapper.
    Description of params are valid only if you get this via Client.
    :param raw_resp: Raw response. dict.
    :param raw: `raw` From response. str.
    :param timestamp: `timestamp` From response. str.
    :param altimeter: `altimeter` From response. int.
    :param clouds: `clouds` From response. list.
    :param visibility: `visibility` From response. int.
    :param wind_dir: `wind_direction` From response. int.
    :param wind_spd: `wind_speed` From response. int.
    :param wind_gust: `raw` From response. dict or can be None.
    :param remarks: `remarks` From response. String.
    :param drewpoint: `drewpoint` From response. int.
    :param temp: `temperature` From response. int.
    :param units: `units` From response. dict.
    """
    def __init__(self, raw_resp, raw, timestamp, altimeter, clouds, visibility, wind_dir, wind_spd, wind_gust, remarks, drewpoint, temp, units):
        self.raw_resp = raw_resp
        self.raw = raw
        self.timestamp = timestamp
        self.altimeter = altimeter
        self.clouds = clouds
        self.visibility = visibility
        self.wind_dir = wind_dir
        self.wind_spd = wind_spd
        self.wind_gust = wind_gust
        self.remarks = remarks
        self.drewpoint = drewpoint
        self.temp = temp
        self.units = units

    def __dict__(self) -> dict:
        return self.raw_resp
