from django.shortcuts import render
from arches.app.models.resource import Resource
from arches.app.utils.data_management.resources.exporter import ResourceExporter
from arches.app.utils import import_class_from_string
from arches.app.models.system_settings import settings
from arches.app.utils.data_management.resources.formats.htmlfile import HtmlWriter
from uuid import UUID


def html_export_site(request):

    html_writer = HtmlWriter()
    resource_list = html_writer.fetch_resource_objects_list(resourceinstanceids=['5e106bab-8993-4f84-9f81-852d30fd07ad'],
                                                            allowed_graph_ids=['5b144ae2-fc19-11ec-9eef-0050568e7db6'])
    
    resource = resource_list["5b144ae2-fc19-11ec-9eef-0050568e7db6"][0]

    return render(
        request,
        'html_export/site.htm',
        {"resources": [resource]},
    )
