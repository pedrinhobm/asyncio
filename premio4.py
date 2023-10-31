import asyncio
import random
import time

async def participant(name, blocks, prices, start_time):
    current_prices = prices.copy()
    
    while time.time() - start_time < 30:
        await asyncio.sleep(random.uniform(0, 5))
        block = random.choice(blocks)
        new_price = current_prices[block] + random.randint(1, 10)  # Incremento aleatorio
        current_prices[block] = new_price
        print(f"Participante {name} hizo oferta de ${new_price} para Bloque {block}")

async def main():
    blocks = [0, 1, 2]
    prices = {block: 15_000_000 for block in blocks}  # Precio base de cada bloque
    start_time = time.time()

    print("Bloques a subastar:")
    for block in blocks:
        print(f"Bloque {block}: 50 MHz")

    for round_number in range(1, 4):
        print(f"Ronda {round_number}:")
        print("Precios actuales:")
        for block in blocks:
            print(f"Bloque {block}: ${prices[block]} millones")

        tasks = [participant(name, blocks, prices, start_time) for name in ["Telefónica", "Claro", "Entel"]]
        await asyncio.gather(*tasks)

        print(f"Se cumplió el tiempo de 30 segundos. Ronda {round_number} finaliza.")
        if round_number < 3:
            for block in blocks:
                prices[block] = max(prices[block] for name in ["Telefónica", "Claro", "Entel"])
    
    print("Los ganadores son:")
    for block in blocks:
        winner = max(["Telefónica", "Claro", "Entel"], key=lambda name: prices[block])
        print(f"Bloque {block}: {winner} con ${prices[block]} millones")

if __name__ == "__main__":
    asyncio.run(main())
