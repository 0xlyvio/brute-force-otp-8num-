def gerar_wordlist_otp(nome_arquivo="wordlist_otp.txt"):
    with open(nome_arquivo, "w") as f:
        for i in range(1, 100000000):
            f.write(f"{i:08d}\n")
    print(f"Wordlist gerada com sucesso em: {nome_arquivo}")

if __name__ == "__main__":
    gerar_wordlist_otp()
