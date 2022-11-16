import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, smtplib, cv2, webbrowser
from datetime import datetime

# para configurar el asistente con reconocimiento de voz
name="juanita"
listener=sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

# para tomar los datos de la hora de la pc
now=datetime.now()

# para tomar fotos
camera_port = 0   
ramp_frames=30
camera=cv2.VideoCapture(camera_port)

# metodo para enviar correo
def enviar_correo():
   message='Hola, un mensaje con el asistente virtual'
   subject="Prueba de correo"
   message = 'Subject: {}\n\n{}'.format(subject, message)
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login('chiauzzianna@gmail.com', '************')        # aqui omito de poner contrasegna generada por google 
   server.sendmail('chiauzzianna@gmail.com','jormanescor@gmail.com', message)
   server.quit()
   print("Correo enviado exitosamente!")

# metodos para tomar las fotos
def get_image():
   retval, im = camera.read()
   return im

def tomar_foto():
   for i in range(ramp_frames):
      temp=get_image()
   print("Capturando Cara")
   camera_capture = get_image ()
   file = "test_image.png"
   cv2.imwrite(file, camera_capture)
   # del camera
   print("Foto Tomada")

# metodo para hablar
def talk(text):
	engine.say(text)
	engine.runAndWait()

# metodo para escuchar instrucciones
def listen():
   try:
      with sr.Microphone() as source:
         print("Escuchando...")
         rec = ''
         pc = listener.listen(source)
         rec = listener.recognize_google(pc,language='es')
         rec=rec.lower()
         if name in rec:
            rec= rec.replace(name,'')
   except:
      pass
   return rec

# metodo principal
def run_Juanita():
   while (1==1):
      rec= listen()
      if 'reproduce' in rec:
         music = rec.replace ('reproduce', '')
         print("Reproduciendo"+ music)
         talk("Reproduciendo" + music)
         pywhatkit.playonyt(music)
      if 'hora' in rec:
         hora = now.strftime("%H:%M")
         talk("La hora es" + hora)
         print(hora)
      if 'busca' in rec:
         search = rec.replace('busca','')
         wikipedia.set_lang("es")
         wiki = wikipedia.summary(search,1)
         print(search+": "+wiki)
         talk(wiki)
      if 'correo' in rec: 
         enviar_correo()
      if 'foto' in rec:
         talk("say cheese")
         print("tomando foto")
         tomar_foto()
      if 'navegador' in rec:
         talk("abriendo el navegador")
         print("abriendo el navegador")
         webbrowser.open("https://google.com")
      if 'chao' in rec:
         print("hasta luego")
         talk("bye")
         break

if __name__== '__main__':
   run_Juanita()