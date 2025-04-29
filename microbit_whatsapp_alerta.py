import serial            
import pywhatkit         
import time              

puerto = "/dev/tty.usbmodem102" 
baudrate = 115200

# Número al que vas a mandar el mensaje (con código de país)
numero_whatsapp = "+525623697735"  

# Conectamos al micro:bit
microbit = serial.Serial(puerto, baudrate)
ultimo_mensaje = ""  # Para no repetir alertas

print("Conectado al micro:bit")

while True:
    try:
        # Leemos lo que mande el micro:bit
        data = microbit.readline().decode().strip()
        print(f"Micro:bit dice: {data}")

        if data and data != ultimo_mensaje:
            mensaje = f"Alerta: {data}"


            # Hora actual
            hora_actual = time.localtime()
            hora = hora_actual.tm_hour
            minuto = hora_actual.tm_min + 1
            if minuto >= 60:
                minuto = 0
                hora = (hora + 1) % 24

            print("Enviando mensaje a WhatsApp: {mensaje}")

            pywhatkit.sendwhatmsg_instantly(numero_whatsapp, mensaje)

            ultimo_mensaje = data  # Evitar duplicados

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(3)
    