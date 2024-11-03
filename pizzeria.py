from Pizzeria.Manager import DataBaseManager
from Pizzeria.Authenticator import Authenticator
from Pizzeria.Procesador_pagos import PaymentProcessor
from Pizzeria.Orden import OrderManager

def pizzeria():
    # Crear instancias centralizadas de las dependencias
    database_manager = DataBaseManager("my-database-connection-string")
    authenticator = Authenticator(database_manager)  # Dependencia inyectada
    payment_processor = PaymentProcessor("my-payment-api-key")
    # Crear una instancia de OrderManager, pasando las dependencias inyectadas
    order_manager = OrderManager(database_manager, authenticator, payment_processor)
    # Usar OrderManager para crear y procesar una orden
    order_manager.create_order(user_id=1, order_details={"pizza": "Margarita", "tamaño": "Grande"})
    order_manager.process_order_payment(order_id=123, user_id=1, amount=20.00)
