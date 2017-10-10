# ckanext-federagobes - CKAN extension to federate data on datos.gob.es

`ckanext-federagobes` generates an RDF version of the dataset catalogue that can be used to federate its datasets on datos.gob.es.

This extension was developed for the Open Data BCN project, which heavily relies on custom dataset fields and multilanguage support provided by ckanext-scheming and ckanext-fluent, but the templating system allows the XML template to be adapted to any organization's dataset schema and disable the multilanguage support by modifying the [`federador.xml`](https://github.com/AjuntamentdeBarcelona/ckanext-federagobes/ckanext/federagobes/templates/federador.xml) file.

The resulting RDF file can be accessed from the URL **/federador.xml** of your CKAN installation.

## Requirements

This extension requires CKAN version **2.7**. It hasn't been tested on previous or later versions.

## Installation
To install ckanext-federagobes:
1. Activate your CKAN virtual environment, for example:
    `. /usr/lib/ckan/default/bin/activate`
	`cd /usr/lib/ckan/default/src`

2. Install the ckanext-federagobes Python package into your virtual environment:
    `pip install -e "git+https://github.com/AjuntamentdeBarcelona/ckanext-federagobes.git#egg=ckanext-federagobes"`

3. Add `federagobes` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/production.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:
     `sudo service apache2 reload`

## Configuration

The following configuration settings are required in order to generate a valid RDF file. These should be included on your CKAN config file (usually found at `/etc/ckan/default/production.ini`).

### `ckanext.federagobes.publisher`

URI that identifies the publisher organization. This is provided by datos.gob.es.

### `ckanext.federagobes.create_date`

Dataset catalogue creation date in ISO‑8601 format.

### `ckanext.federagobes.theme_taxonomy`

URI . This is usually `http://datos.gob.es/kos/sector-publico/sector/`

### `ckanext.federagobes.license_url`

URL for the dataset catalogue terms of use.

### `ckanext.federagobes.catalog_title.locale`

The catalog's title for each of the languages available in CKAN on the `ckan.locales_offered` configuration setting. For example, in order to set the english title, we would add the following configuration setting: `ckanext.federagobes.catalog_title.en`

### `ckanext.federagobes.catalog_title.locale`

The catalog's description for each of the languages available in CKAN.


Configuration example:
```ini
ckanext.federagobes.publisher = http://datos.gob.es/recurso/sector-publico/org/Organismo/L01080193
ckanext.federagobes.create_date = 2017-02-23T08:00:00
ckanext.federagobes.theme_taxonomy = http://datos.gob.es/kos/sector-publico/sector/
ckanext.federagobes.license_url = http://opendata-ajuntament.barcelona.cat/condicions-us
ckanext.federagobes.catalog_title.ca = Open Data BCN
ckanext.federagobes.catalog_title.es = Open Data BCN
ckanext.federagobes.catalog_title.en = Open Data BCN
ckanext.federagobes.catalog_desc.ca = Servei de dades obertes de l'Ajuntament de Barcelona
ckanext.federagobes.catalog_desc.es = Servicio de datos abiertos del Ayuntamiento de Barcelona
ckanext.federagobes.catalog_desc.en = Barcelona's City Hall Open Data Service
```

## Contributing

You are welcome to contribute to this repository, but please read the CONTRIBUTING guidelines.

## License

This extension is published under the GNU Affero General Public License v3 (see LICENSE).