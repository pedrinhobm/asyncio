import asyncio
import random
import time

async def participant(name, offers, start_time):
    current_price = 20000
    while time.time() - start_time < 60:
        await asyncio.sleep(random.uniform(0, 10))
        new_offer = current_price + random.randint(500, 5000)
        offers[name] = new_offer
        print(f"Participante {name} hizo reoferta de {new_offer}")

        for other_name, other_offer in offers.items():
            if other_name != name and new_offer > other_offer:
                if random.random() < 0.5:
                    nuevo_minimo = new_offer + 500
                    nuevo_maximo = nuevo_minimo * 1.20
                    reoffer = random.randint(int(nuevo_minimo), int(nuevo_maximo))
                    if reoffer > current_price:
                        current_price = reoffer
                        offers[name] = reoffer
                        print(f"Participante {name} hizo reoferta de {reoffer}")

async def main():
    offers = {'a': 20000, 'b': 20000, 'c': 20000, 'd': 20000, 'e': 20000}
    participants = ['a', 'b', 'c', 'd', 'e']
    start_time = time.time()
    tasks = [participant(name, offers, start_time) for name in participants]
    await asyncio.gather(*tasks)

    print("Se cumplió el tiempo de 60 segundos")
    print("Ofertas finales:", offers)
    winner = max(offers, key=offers.get)
    print("El ganador es", winner)

if __name__ == "__main__":
    asyncio.run(main())

