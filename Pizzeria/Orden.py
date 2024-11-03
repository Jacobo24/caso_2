from Pizzeria.Manager import DataBaseManager
from Pizzeria.Authenticator import Authenticator
from Pizzeria.Procesador_pagos import PaymentProcessor

class OrderManager:
    def __init__(self, database_manager: DataBaseManager, authenticator: Authenticator, payment_processor: PaymentProcessor):
        self.database_manager = database_manager
        self.authenticator = authenticator
        self.payment_processor = payment_processor

    def create_order(self, user_id, order_details):
        print(f"Creando orden para el usuario {user_id} con detalles: {order_details}")
        # Lógica para crear un pedido en la base de datos

    def update_order(self, order_id, order_details):
        print(f"Actualizando orden {order_id} con nuevos detalles: {order_details}")
        # Lógica para actualizar un pedido en la base de datos

    def delete_order(self, order_id):
        print(f"Eliminando orden {order_id}")
        # Lógica para eliminar un pedido en la base de datos

    def process_order_payment(self, order_id, user_id, amount):
        if self.authenticator.authenticate_user(user_id, "password"):
            self.payment_processor.process_payment(order_id, amount)
            print(f"Pago procesado para la orden {order_id}")