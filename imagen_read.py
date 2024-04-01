from deepface import DeepFace
import cv2
import mediapipe as mp
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Función para analizar y mostrar información del rostro
def analizar_mostrar_info(frame):
    # Inicialización de MediaPipe para la detección de rostros
    detros = mp.solutions.face_detection
    rostros = detros.FaceDetection(min_detection_confidence=0.8, model_selection=0)

    # Corrección de color a RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesamiento de detección de rostros
    resrostros = rostros.process(rgb)

    # Si se detectan rostros, proceder con el análisis
    if resrostros.detections is not None:
        for rostro in resrostros.detections:
            al, an, c = frame.shape
            box = rostro.location_data.relative_bounding_box
            xi, yi, w, h = int(box.xmin * an), int(box.ymin * al), int(box.width * an), int(box.height * al)
            xf, yf = xi + w, yi + h

            # Dibujo del rectángulo alrededor del rostro
            cv2.rectangle(frame, (xi, yi), (xf, yf), (255, 255, 0), 1)

            # Análisis del rostro con DeepFace
            try:
                info = DeepFace.analyze(frame, actions=['age', 'gender', 'race', 'emotion'], enforce_detection=False)

                # Muestra la información obtenida en la imagen
                cv2.putText(frame, f"Gender: {info['gender']}", (xi, yi-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
                cv2.putText(frame, f"Age: {info['age']}", (xi, yi-30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.putText(frame, f"Emotion: {info['dominant_emotion']}", (xi, yi-50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

                # Traducimos
                if gen == 'Man':
                    gen = 'Hombre'

                    # Emociones
                    if emociones == 'angry':
                        emociones = 'enojado'
                    if emociones == 'disgust':
                        emociones = 'disgustado'
                    if emociones == 'fear':
                        emociones = 'miedoso'
                    if emociones == 'happy':
                        emociones = 'feliz'
                    if emociones == 'sad':
                        emociones = 'triste'
                    if emociones == 'surprise':
                        emociones = 'sorprendido'
                    if emociones == 'neutral':
                        emociones = 'neutral'

                    # Race
                    if race == 'asian':
                        race = 'asiatico'
                    if race == 'indian':
                        race = 'indio'
                    if race == 'black':
                        race = 'negro'
                    if race == 'white':
                        race = 'blanco'
                    if race == 'middle eastern':
                        race = 'oriente medio'
                    if race == 'latino hispanic':
                        race = 'latino'

                elif gen == 'Woman':
                    gen = 'Mujer'

                    # Emociones
                    if emociones == 'angry':
                        emociones = 'enojada'
                    if emociones == 'disgust':
                        emociones = 'disgustada'
                    if emociones == 'fear':
                        emociones = 'miedosa'
                    if emociones == 'happy':
                        emociones = 'feliz'
                    if emociones == 'sad':
                        emociones = 'triste'
                    if emociones == 'surprise':
                        emociones = 'sorprendida'
                    if emociones == 'neutral':
                        emociones = 'neutral'

                    # Race
                    if race == 'asian':
                        race = 'asiatica'
                    if race == 'indian':
                        race = 'india'
                    if race == 'black':
                        race = 'negra'
                    if race == 'white':
                        race = 'blanca'
                    if race == 'middle eastern':
                        race = 'oriente medio'
                    if race == 'latino hispanic':
                        race = 'latina'

            except Exception as e:
                print("Ocurrio un error en el analisis:", e)




    # Muestra la imagen con la información
    cv2.imshow("Analysis Result", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Inicializa Tkinter y oculta la ventana principal
Tk().withdraw()
# Muestra el diálogo de selección de archivos y obtiene la ruta del archivo seleccionado
nombre_imagen = askopenfilename(title="Seleccione una imagen para analizar", filetypes=[("Image files", "*.jpg *.jpeg *.png")])

# Verifica si se seleccionó un archivo
if nombre_imagen:
    frame = cv2.imread(nombre_imagen)
    # Verifica si la imagen se cargó correctamente
    if frame is not None:
        analizar_mostrar_info(frame)
    else:
        print("No se pudo cargar la imagen. Por favor, verifica el archivo seleccionado.")
else:
    print("No se seleccionó ningún archivo.")