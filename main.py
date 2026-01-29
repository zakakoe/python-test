import random

def generate_random_number():
    num = random.randint(1, 100)
    print(f"Random number: {num}")
    return num

if __name__ == "__main__":
    generate_random_number()
