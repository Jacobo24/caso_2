class PaymentProcessor:
    def __init__(self, api_key):
        self.api_key = api_key

    def process_payment(self, order_id, amount):
        print(f"Procesando pago de ${amount} para la orden {order_id} con la API {self.api_key}")
        # Lógica para procesar el pago con el API key