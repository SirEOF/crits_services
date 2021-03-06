import json

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponse, render_to_response
from django.template import RequestContext
#from django.template.loader import render_to_string

from crits.core.user_tools import user_can_view_data
from . import handlers

@user_passes_test(user_can_view_data)
def main(request):
    return render_to_response('pt_main.html',
                              {},
                              RequestContext(request))

@user_passes_test(user_can_view_data)
def campaign_heatmap(request):
    if request.method == "POST" and request.is_ajax():
        results = handlers.campaign_heatmap(request)
        return HttpResponse(json.dumps(results),
                            content_type="application/json")
    else:
        return render_to_response('pt_campaign_heatmap.html',
                                  {},
                                  RequestContext(request))
