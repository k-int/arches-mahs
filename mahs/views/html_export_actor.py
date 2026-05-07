from django.shortcuts import render
from arches.app.models.resource import Resource
from arches.app.utils.data_management.resources.exporter import ResourceExporter
from arches.app.utils import import_class_from_string
from arches.app.models.system_settings import settings
from arches.app.utils.data_management.resources.formats.htmlfile import HtmlWriter
from uuid import UUID


def html_export_actor(request):

    html_writer = HtmlWriter()
    resource_list = html_writer.fetch_resource_objects_list(resourceinstanceids=['8b913bf0-8acb-45aa-9a9d-2f61d119bd4b'],
                                                            allowed_graph_ids=['c42a21b2-92ed-41f9-b670-64f02dee5f03'])
    
    resource = resource_list["c42a21b2-92ed-41f9-b670-64f02dee5f03"][0]

    return render(
        request,
        'html_export/actor.htm',
        {"resources": [resource]},
    )
