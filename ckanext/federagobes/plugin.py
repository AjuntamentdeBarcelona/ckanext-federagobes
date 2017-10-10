import datetime as d
import mimetypes as m
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class FederagobesPlugin(plugins.SingletonPlugin):
	plugins.implements(plugins.IConfigurer)
	plugins.implements(plugins.IRoutes, inherit=True)
	plugins.implements(plugins.ITemplateHelpers) 

	# IConfigurer
	def update_config(self, config_):
		toolkit.add_template_directory(config_, 'templates')
		
		m.add_type('text/wms', '.wms')
		m.add_type('application/octet-stream', '.dat')
		m.add_type('application/x-zipped-shp', '.shx')
		m.add_type('application/x-zipped-shp', '.shp')
		
		
	def before_map(self, map):
		map.connect(
			'federador', '/federador.rdf',
			controller='ckanext.federagobes.controllers:RDFController',
			action='view'
		)
		return map
	
	# ITemplateHelpers
	def get_helpers(self):
		return {
			'get_mimetype': get_mimetype,
			'publish_date_isoformat': publish_date_isoformat
		}
		
# Helper methods
def get_mimetype(resource):
	mimetype = ''

	if 'mimetype' in resource and resource['mimetype']:
		mimetype = resource['mimetype']
	elif 'url' in resource and m.guess_type(resource['url'])[0]:
		mimetype = m.guess_type(resource['url'])[0]
	elif 'name' in resource and m.guess_type(resource['name'])[0]:
		mimetype = m.guess_type(resource['name'])[0]
	elif 'format' in resource and m.guess_type('filename.' + resource['format'])[0]:
		mimetype = m.guess_type('filename.' + resource['format'])[0]
	else:
		mimetype = 'text/plain'
	
	return mimetype
	
def publish_date_isoformat(date):
	return d.datetime.strptime(date, "%Y-%m-%d").isoformat()