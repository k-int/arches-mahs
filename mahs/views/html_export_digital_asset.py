from django.shortcuts import render
from arches.app.models.resource import Resource
from arches.app.utils.data_management.resources.exporter import ResourceExporter
from arches.app.utils import import_class_from_string
from arches.app.models.system_settings import settings
from arches.app.utils.data_management.resources.formats.htmlfile import HtmlWriter
from uuid import UUID


def html_export_digital_asset(request):

    html_writer = HtmlWriter()
    resource_list = html_writer.fetch_resource_objects_list(resourceinstanceids=['fc917524-e317-4eea-b43e-a49acedd3f54'],
                                                            allowed_graph_ids=['aaab9bcb-4ec1-4b6a-8af8-71b6fa17b934'])
    
    resource = resource_list["aaab9bcb-4ec1-4b6a-8af8-71b6fa17b934"][0]

    return render(
        request,
        'html_export/digital_asset.htm',
        {"resources": [resource]},
    )
