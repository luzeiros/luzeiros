#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
from requests.exceptions import BaseHTTPError, HTTPError


class Azura(object):
    def __init__(self):
        super(Azura, self).__init__()
        self.telegramChat = '@ekletikstudios'
        self.azura_endpoint = 'http://repaus.com/api'
        self.url = self.azura_endpoint

    def now(self):
        try:
            req = requests.get(f'{self.url}/nowplaying')
            res = req.json()
        except BaseHTTPError:
            print("An error occurred.")
            return

        output = """{"data": ["""

        for index in range(len(res)):

            # Station
            s = res[index]['station']
            id, name, url, shortcode = s['id'], s['name'], s['listen_url'], s['shortcode']
            is_live = res[index]['live']['is_live']
            listeners = res[index]['listeners']

            # Song
            song = res[index]['now_playing']['song']
            history = res[index]['song_history']
            last_0, last_1 = history[0]['song'], history[1]['song']

            mounts, remotes = s['mounts'], s['remotes']

            output += json.dumps({'type': 'station',
                                 'id': id,
                                 'attributes': {
                                    'name': name,
                                    'code': shortcode,
                                    'url': url,
                                    'is-live': is_live,
                                    'song': song,
                                    'listeners': listeners
                                 },
                                 'relationships': {
                                     'mounts': mounts,
                                     'remotes': remotes,
                                     'song-history': {
                                         'last': last_0,
                                         'before-last': last_1
                                     }
                                 }
                                 }, indent=4)

            if index < len(res)-1:
                output += ','
        output += "]}"

        return output

    def single(self, pk=None):
        try:
            req = requests.get(f'{self.url}/nowplaying/{pk}')
            res = req.json()
        except BaseHTTPError:
            raise BaseHTTPError('Error')

        if res == "Station not found.":
            return json.dumps({"errors": [
                {
                    'detail': 'Not found.',
                    'source': {
                        'pointer': '/data/attributes/detail'
                    },
                    'status': '404'
                }]
            }), 404

        # Station
        s = res['station']
        sid, name, url, shortcode = s['id'], s['name'], s['listen_url'], s['shortcode']
        is_live = res['live']['is_live']
        listeners = res['listeners']

        # Song
        song = res['now_playing']['song']
        history = res['song_history']
        last_0, last_1 = history[0]['song'], history[1]['song']

        mounts, remotes = s['mounts'], s['remotes']

        output = """{"data": """
        output += json.dumps({'type': 'station',
                              'id': sid,
                              'attributes': {
                                  'name': name,
                                  'code': shortcode,
                                  'url': url,
                                  'is-live': is_live,
                                  'song': song,
                                  'listeners': listeners
                              },
                              'relationships': {
                                  'mounts': mounts,
                                  'remotes': remotes,
                                  'song-history': {
                                      'last': last_0,
                                      'before-last': last_1
                                  }
                              }
                              }, indent=4)

        output += "}"
        return output, 200


if __name__ == '__main__':
    azura = Azura()
    # print(azura.now())
    print(azura.single(pk=2))
