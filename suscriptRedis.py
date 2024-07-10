import redis
import os


#configuracion redis

redis_host= os.getenv(REDIS_HOST)
redis_port= os.getenv(REDIS_PORT)
redis_password= os.getenv(REDIS_PASSWORD)

#conexion a redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Suscriptor de redis
def subscriber():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('canal_prueba')

    print("Esperando mensaje...")
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Recibido: {message['data']}")

if __name__ == "__main__":
    subscriber()
