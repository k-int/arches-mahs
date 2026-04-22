from django.shortcuts import render
from arches.app.models.resource import Resource
from arches.app.utils.data_management.resources.exporter import ResourceExporter
from arches.app.utils import import_class_from_string
from arches.app.models.system_settings import settings
from arches.app.utils.data_management.resources.formats.htmlfile import HtmlWriter
from uuid import UUID


def html_export_collection(request):

    html_writer = HtmlWriter()
    resource_list = html_writer.fetch_resource_objects_list(resourceinstanceids=['57b65dc3-f6bf-4359-adc1-a3f4b391e0bd'],
                                                            allowed_graph_ids=['53f5cd56-0bd4-11ed-9eef-0050568e7db6'])
    
    resource = resource_list["53f5cd56-0bd4-11ed-9eef-0050568e7db6"][0]

    return render(
        request,
        'html_export/collection.htm',
        {"resources": [resource]},
    )
