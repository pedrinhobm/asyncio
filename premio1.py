import asyncio
import random

async def participant(name):
    await asyncio.sleep(random.uniform(0, 10))
    price = random.randint(20000, 100000)  # Oferta aleatoria entre $20,000 y $100,000
    return name, price

async def main():
    participants = ['a', 'b', 'c', 'd', 'e']
    tasks = [participant(name) for name in participants]
    results = await asyncio.gather(*tasks)

    offers = {name: price for name, price in results}
    winner = max(offers, key=offers.get)

    print("Ofertas finales:", offers)
    print("El ganador es", winner)

if __name__ == "__main__":
    asyncio.run(main())
