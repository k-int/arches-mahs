from django.shortcuts import render
from arches.app.models.resource import Resource
from arches.app.utils.data_management.resources.exporter import ResourceExporter
from arches.app.utils import import_class_from_string
from arches.app.models.system_settings import settings
from arches.app.utils.data_management.resources.formats.htmlfile import HtmlWriter
from uuid import UUID


def html_export_oral_history(request):

    html_writer = HtmlWriter()
    resource_list = html_writer.fetch_resource_objects_list(resourceinstanceids=['5a6ad569-950c-4349-ad06-33b8e1d6fd99'],
                                                            allowed_graph_ids=['ed64662d-13e8-4f9e-8b4f-34b69dc39fdd'])
    
    resource = resource_list["ed64662d-13e8-4f9e-8b4f-34b69dc39fdd"][0]

    return render(
        request,
        'html_export/oral_history.htm',
        {"resources": [resource]},
    )
