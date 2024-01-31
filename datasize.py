#!/usr/bin/env python3

import argparse
import pandas as pd
import datetime as dt

from terracatalogueclient import Catalogue
from terracatalogueclient.config import CatalogueConfig, CatalogueEnvironment

msg = "Script to calculate the size of the dataset"
parser = argparse.ArgumentParser(description = msg)
parser.add_argument("catalogue")
args = parser.parse_args()

config = CatalogueConfig.from_environment(CatalogueEnvironment.CGLS)
catalogue = Catalogue(config)

products = catalogue.get_products(args.catalogue)

rows = []

for product in products:
    rows.append([product.id, product.data[0].href, (product.data[0].length/(1024*1024))])

df = pd.DataFrame(data = rows, columns = ['Identifier', 'URL', 'Size (MB)'])

total = df['Size (MB)'].sum()

print(f'Full dataset size: {total/1024} GB')
