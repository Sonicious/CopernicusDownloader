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

product_list = list(catalogue.get_products(args.catalogue))

catalogue.download_products(product_list, './')

