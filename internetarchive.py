# VERSION: 1.0
# AUTHORS: RedMatter
# SPDX-License-Identifier: MIT
"""Search public Internet Archive torrents from qBittorrent (Python 3)."""

import json
import re
import sys
from urllib.error import URLError
from urllib.parse import unquote_plus, urlencode
from urllib.request import Request, urlopen

from novaprinter import prettyPrinter


class internetarchive:
    url = "https://archive.org"
    name = "Internet Archive"
    supported_categories = {
        "all": "",
        "books": "texts",
        "movies": "movies",
        "music": "audio",
        "pictures": "image",
        "software": "software",
    }

    def search(self, query, category="all"):
        query = unquote_plus(query).strip()
        if not query or category not in self.supported_categories:
            return

        
        query = '({}) AND format:"Archive BitTorrent"'.format(query)
        query += ' AND NOT access-restricted-item:true'
        media = self.supported_categories[category]
        if media:
            query += " AND mediatype:" + media
        
        params = urlencode({
            "q": query,
            "fl[]": ["identifier", "title"],
            "rows": 100,
            "page": 1,
            "output": "json",
        }, doseq=True)
        request = Request(self.url + "/advancedsearch.php?" + params, headers={
            "User-Agent": "qBittorrent-InternetArchive-Search/1.0",
            "Accept": "application/json",
        })
        try:
            
            with urlopen(request, timeout=25) as response:
                data = json.load(response)
            docs = data["response"]["docs"]
            if not isinstance(docs, list):
                raise ValueError("unexpected search response")
        except (URLError, OSError, ValueError, KeyError, TypeError) as error:
            
            print("Internet Archive search failed: {}".format(error), file=sys.stderr)
            return

        seen = set()
        for doc in docs:
            if not isinstance(doc, dict):
                continue
            identifier = doc.get("identifier", "")
            if not isinstance(identifier, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", identifier):
                continue
            if identifier in seen:
                continue
            seen.add(identifier)
            title = doc.get("title") or identifier
            if isinstance(title, list):
                title = " / ".join(str(part) for part in title)
            title = " ".join(str(title).replace("|", "-").split())
            prettyPrinter({
                "link": "{}/download/{}/{}_archive.torrent".format(self.url, identifier, identifier),
                "name": title,
                
                "size": -1,
                "seeds": -1,
                "leech": -1,
                "engine_url": self.url,
                "desc_link": self.url + "/details/" + identifier,
                "pub_date": -1,
            })
