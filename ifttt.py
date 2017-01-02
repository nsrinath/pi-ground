#!/usr/bin/env python3
import requests


class IFTTTMaker(object):

    def __init__(self):
        self.host = "maker.ifttt.com"
        self.secret_key = ""

    def _url_to_post(self, **kwargs):
        try:
            if not kwargs.get('event'):
                raise RuntimeError("No valid event to throw")
            ''' fill the data and build the url '''
            url_json = {"value1": kwargs.get('value1', 'No valid data here')}
            url = "%s://%s/trigger/%s/with/key/%s" % (kwargs.get(
                'protocol', "https"), self.host, kwargs.get('event'), self.secret_key)

            r = requests.post(url, json=url_json)
        except RuntimeError:
            import traceback
            trbk_data = traceback.format_exc()
            self._url_to_post(event="rpi01_error", value1=trbk_data)

    def post_rpi01_alive(self):
        ''' Tell Maker that I'm alive '''
        self._url_to_post(event="rpi01_alive")

if __name__ == "__main__":
    i = IFTTTMaker()
    i.post_rpi01_alive()
