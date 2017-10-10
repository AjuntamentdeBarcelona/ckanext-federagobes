import ckan.lib.app_globals as app_globals
import ckan.lib.i18n as i18n
import ckan.model as model
import ckan.plugins.toolkit as t
import datetime as d
from ckan.lib.render import TemplateNotFound
from ckan.common import OrderedDict
from pylons import config

log = __import__('logging').getLogger(__name__)
namespace = 'ckanext.federagobes'

c = t.c


class RDFController(t.BaseController):

	def view(self):
		
		context = {'model': model, 'session': model.Session,
					'user': c.user, 'for_view': True,
					'auth_user_obj': c.userobj}
		
		# Get the plugin configuration
		site_url = config.get('ckan.site_url') + config.get('ckan.root_path').replace('{{LANG}}', '')
		date_created = config.get(namespace + '.create_date')
		date_modified = d.datetime.now().isoformat()
		publisher = config.get(namespace + '.publisher')
		theme_taxonomy = config.get(namespace + '.theme_taxonomy')
		license_url = config.get(namespace + '.license_url')
		catalog_title = {}
		catalog_desc = {}
		
		for locale in i18n.get_locales():
			catalog_title[locale] = config.get(namespace + '.catalog_title.' + locale)
			catalog_desc[locale] = config.get(namespace + '.catalog_desc.' + locale)
		
		# Get the dataset catalogue
		packages = t.get_action('package_search')(context, {
				'include_private': False,
				'rows': 1000
			})
		packages = packages['results']
		
		t.response.headers['Content-Type'] = 'application/rdf+xml; charset=utf-8'
		return t.render('federador.xml', extra_vars={
				'site_url': site_url,
				'date_created': date_created,
				'date_modified': date_modified,
				'publisher': publisher,
				'theme_taxonomy': theme_taxonomy,
				'license_url': license_url,
				'packages': packages,
				'catalog_title': catalog_title,
				'catalog_desc': catalog_desc
			})