import os
import pyaes

def decrypt_file(encrypted_file_name, key):
    """
    Descriptografa um arquivo criptografado e salva com o nome original.
    """
    # Verificar se o arquivo criptografado existe
    if not os.path.exists(encrypted_file_name):
        print(f"Arquivo '{encrypted_file_name}' não encontrado.")
        return

    # Ler o conteúdo do arquivo criptografado
    with open(encrypted_file_name, "rb") as encrypted_file:
        crypto_data = encrypted_file.read()

    # Descriptografar os dados
    aes = pyaes.AESModeOfOperationCTR(key)
    original_data = aes.decrypt(crypto_data)

    # Recuperar o nome original do arquivo (removendo a extensão '.encrypted')
    original_file_name = encrypted_file_name.replace(".encrypted", "")

    # Salvar o arquivo descriptografado
    with open(original_file_name, "wb") as original_file:
        original_file.write(original_data)

    # Opcionalmente, remover o arquivo criptografado
    os.remove(encrypted_file_name)

    print(f"Arquivo descriptografado com sucesso: '{original_file_name}'")

def main():
    # Nome do arquivo criptografado
    encrypted_file_name = "teste.txt.encrypted"

    # Chave de descriptografia (a mesma usada para criptografar)
    key = b"testeransomwares"  # Deve ser idêntica à usada na criptografia

    # Descriptografar o arquivo
    decrypt_file(encrypted_file_name, key)

if __name__ == "__main__":
    main()
