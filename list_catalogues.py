#!/usr/bin/env python3

import pandas as pd
import datetime as dt

from terracatalogueclient import Catalogue
from terracatalogueclient.config import CatalogueConfig, CatalogueEnvironment


config = CatalogueConfig.from_environment(CatalogueEnvironment.CGLS)
catalogue = Catalogue(config)

collections = catalogue.get_collections()
rows = []
for c in collections:
    rows.append([c.id, c.properties['title']])

df = pd.DataFrame(data = rows, columns = ['Identifier', 'Description'])
df.style.set_properties(**{'text-align': 'left'})

print(df.to_markdown())

