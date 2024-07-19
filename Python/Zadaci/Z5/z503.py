def main():
    proizvodi = {"Mleko": 2.30, "Hleb": 2.20, "Secer": 1.40}
    proizvodiSkuplji = {key:value*1.17 for key, value in proizvodi.items()}
    print(proizvodiSkuplji)

if __name__ == "__main__":
    main()
