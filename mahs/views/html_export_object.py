from django.shortcuts import render
from arches.app.models.resource import Resource
from arches.app.utils.data_management.resources.exporter import ResourceExporter
from arches.app.utils import import_class_from_string
from arches.app.models.system_settings import settings
from arches.app.utils.data_management.resources.formats.htmlfile import HtmlWriter
from uuid import UUID


def html_export_object(request):

    html_writer = HtmlWriter()
    resource_list = html_writer.fetch_resource_objects_list(resourceinstanceids=['498960a5-ed96-4e95-ad30-b8d218518a74'],
                                                            allowed_graph_ids=['0340d04e-0801-11ed-9eef-0050568e7db6'])
    
    resource = resource_list["0340d04e-0801-11ed-9eef-0050568e7db6"][0]

    return render(
        request,
        'html_export/object.htm',
        {"resources": [resource]},
    )
