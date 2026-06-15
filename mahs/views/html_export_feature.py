from django.shortcuts import render
from arches.app.models.resource import Resource
from arches.app.utils.data_management.resources.exporter import ResourceExporter
from arches.app.utils import import_class_from_string
from arches.app.models.system_settings import settings
from arches.app.utils.data_management.resources.formats.htmlfile import HtmlWriter
from uuid import UUID


def html_export_feature(request):

    #f87a2d98-2d5d-4b0b-971b-dd8daecaa16a

    html_writer = HtmlWriter()
    resource_list = html_writer.fetch_resource_objects_list(resourceinstanceids=['6085b09c-4cda-4f4a-bc6f-9943175b4e4c'],
                                                            allowed_graph_ids=['8066c2dc-c40a-11ef-b90d-1b51b0144d8c'])
    
    resource = resource_list["8066c2dc-c40a-11ef-b90d-1b51b0144d8c"][0]

    return render(
        request,
        'html_export/feature.htm',
        {"resources": [resource]},
    )
