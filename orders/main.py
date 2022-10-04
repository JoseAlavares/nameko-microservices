import json
from nameko.rpc import rpc
from models.order_model import OrderModel

class HttpService:
    name = "orders"

    @rpc
    def status(self, request):
        return json.dumps({ "message": "API REST ready" })

    @rpc
    def create_roder(self, name):
        orders = [word for word in name]
        return orders

    @rpc
    def get_orders(self):
        try:
            query = (OrderModel.select().where(OrderModel.id == 1))
            orders = [{ "id": order.id, "description": order.description } for order in query]
            return orders
        except Exception as e:
            print(e)
            return "error"