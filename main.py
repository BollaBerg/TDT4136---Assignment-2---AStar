from src.a_star import a_star

if __name__ == "__main__":
    for i in range(1, 6):
        print(F"Starting task {i}")
        a_star(i)
        print(F" - Finished task {i}")