import json
from werkzeug.wrappers import Response
from nameko.web.handlers import http
from nameko.rpc import RpcProxy

class HttpService:
    name = "api-rest"
    order_proxy = RpcProxy("orders")

    @http("GET", "/api/status")
    def status(self, request):
        return json.dumps({ "message": "API REST ready" })

    @http("POST", "/api/order")
    def create_roder(self, request):
        print(request.get_json()["name"])
        result = self.order_proxy.create_roder(request.get_json()["name"])

        # return json.dumps({ "message": "OK", "data": result })
        res = Response("OK")
        res.data = json.dumps({ "message": "OK", "data": result })
        res.headers["content-type"] = "application/json"
        return res

    @http("GET", "/api/order")
    def get_orders(self, request):
        orders = self.order_proxy.get_orders()
        res = Response("OK")
        res.data = json.dumps({ "message": "ok", "data": orders })
        res.headers["content-type"] = "application/json"
        return res