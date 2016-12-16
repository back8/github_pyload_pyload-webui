# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from pyload.network.requestfactory import get_url
from pyload.plugins.internal.multihoster import MultiHoster


class ZeveraCom(MultiHoster):
    __name__ = "ZeveraCom"
    __version__ = "0.02"
    __type__ = "hook"
    __config__ = [("activated", "bool", "Activated", False),
                  ("hosterListMode", "all;listed;unlisted", "Use for hosters (if supported)", "all"),
                  ("hosterList", "str", "Hoster list (comma separated)", "")]
    __description__ = """Real-Debrid.com hook plugin"""
    __author_name__ = "zoidberg"
    __author_mail__ = "zoidberg@mujmail.cz"

    def get_hoster(self):
        page = get_url("http://www.zevera.com/jDownloader.ashx?cmd=gethosters")
        return [x.strip() for x in page.replace("\"", "").split(",")]