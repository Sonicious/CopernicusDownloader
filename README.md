# Copernicus Downloader

## Installation

Use the `environment.yaml` to get an environment ready

```bash
conda env create -f environment.yml
conda activate CopernicusDownloader
```

Then install the OpenSearch API

```bash
pip install --index-url=https://artifactory.vgt.vito.be/api/pypi/python-packages/simple terracatalogueclient==0.1.16
```

## Usage

List available catalogues with `list_catalogues.py`

Afterwards you can download the datasets to the local directory with 

```bash
python downloader clms_global_tocr_1km_v1_10daily_netcdf
```

you can also just list the dataset size with

```bash
python datasize.py clms_global_tocr_1km_v1_10daily_netcdf
```

## Credits
<pre>
Martin Reinhardt
Earth System Data Science
Remote Sensing Centre for Earth System Research (RSC4Earth)
Institute for Earth System Science and Remote Sensing
University of Leipzig 
</pre>
