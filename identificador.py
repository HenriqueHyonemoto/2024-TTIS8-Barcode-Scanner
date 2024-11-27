import cv2
import numpy as np 
from pyzbar.pyzbar import decode

# Função para ler e exibir código de barras
def ler_codigo_barras(image_path):
    # Carregar a imagem
    img = cv2.imread(image_path)

    # Decodificar os códigos de barras presentes na imagem
    codigos = decode(img)

    # Iterar sobre os códigos de barras detectados
    for codigo in codigos:
        # Extrair as coordenadas do código de barras
        pontos = codigo.polygon
        if len(pontos) == 4:
            pts = pontos
        else:
            pts = cv2.convexHull(np.array([pontos], dtype=np.float32))

        # Desenhar o contorno do código de barras na imagem
        cv2.polylines(img, [np.int32(pts)], True, (0, 255, 0), 3)

        # Decodificar e exibir o valor do código de barras
        valor = codigo.data.decode('utf-8')
        print(f"Código de barras detectado: {valor}")

        # Exibir o texto no código de barras
        x, y, w, h = codigo.rect
        cv2.putText(img, valor, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Exibir a imagem com o código de barras detectado
    cv2.imshow("Imagem com Código de Barras", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Chamada da função com o caminho da imagem
ler_codigo_barras("barcodes/barcode1.jpg")
