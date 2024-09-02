import cv2

# Inicializando a captura de vídeo da câmera (0 é a câmera padrão)
cap = cv2.VideoCapture(0)

# Verificando se a câmera foi aberta corretamente
if not cap.isOpened():
    print("Erro ao abrir a câmera")
    exit()

while True:
    # Capturando frame por frame
    ret, frame = cap.read()

    # Se a captura foi bem-sucedida, ret será True
    if not ret:
        print("Erro ao capturar o frame")
        break

    # Exibindo o frame capturado
    cv2.imshow('Câmera', frame)

    # Pressione 'q' para sair do loop e fechar a janela
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberando a captura e fechando todas as janelas
cap.release()
cv2.destroyAllWindows()
