from pyramid import response, config, view
@view.view_config(route_name='add')
def add(request):
    x, y = (int(request.matchdict[c]) for c in "xy")
    return response.Response(str(x+y))
with config.Configurator() as _cfg:
    _cfg.add_route("add", "/add/{x}/{y}")
    _cfg.scan("e2e_k8s")
    application = _cfg.make_wsgi_app()
