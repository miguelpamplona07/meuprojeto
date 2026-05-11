
import cv2
import easyocr
import matplotlib.pyplot as plt
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

def processar_placa(nome_arquivo):
    # 1. Carregar a imagem da pasta local
    img = cv2.imread(nome_arquivo)
    
    if img is None:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado nesta pasta.")
        return

    # 2. Inicializar o leitor
    reader = easyocr.Reader(['pt', 'en'], gpu=False)

    # 3. Detectar texto
    resultados = reader.readtext(img, paragraph=False)

    encontrou = False
    for (bbox, texto, confidence) in resultados:
        if confidence > 0.2 and len(texto) > 4:
            encontrou = True
            ponto_superior_esquerdo = tuple(map(int, bbox[0]))
            ponto_inferior_direito = tuple(map(int, bbox[2]))

            # Desenhar o retângulo e o texto
            cv2.rectangle(img, ponto_superior_esquerdo, ponto_inferior_direito, (0, 255, 0), 5)
            posicao_texto = (ponto_superior_esquerdo[0], ponto_superior_esquerdo[1] - 15)
            cv2.putText(img, texto.upper(), posicao_texto, 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 4)
            
            print(f"Sucesso! Placa: {texto.upper()} | Confiança: {confidence:.2f}")

    if not encontrou:
        print("O OCR não conseguiu identificar a placa.")

    # 4. SALVAR na própria pasta
    cv2.imwrite('resultado_final.jpg', img)
    print("Imagem 'resultado_final.jpg' salva na pasta local!")
    
    # Exibir (opcional)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.axis('off')
    plt.show()

# --- EXECUÇÃO SIMPLIFICADA ---
# Aqui você só coloca o nome da imagem que está na pasta GLEN2
processar_placa('placa.jpg')