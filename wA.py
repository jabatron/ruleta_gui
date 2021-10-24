from openpyxl.workbook import workbook
import whatsapp as w
from datetime import datetime
from openpyxl import load_workbook
from openpyxl.styles import colors
from openpyxl.styles import Font, Color
from time import time
from time import sleep
import re
import argparse
import os.path


def unsolonumero (sheet):
    messenger = w.WhatsApp()
    print (f"1.- envio de 10 mensajes al mismo número")

    una_vez = True
    time_star=time()
    
    for i in range (2, sheet.max_row + 1):
        cell_numero =  'A' + str(i)
        cell_mensaje = 'B' + str(i)
        numero = str(sheet[cell_numero].value)[:-2]
        mensaje = sheet[cell_mensaje].value
        print (numero, mensaje)

        if una_vez:
            pattern = re.compile("^34\d{9}")
            if pattern.fullmatch(numero):
                print (f'el numero {pattern} es correcto')
            else:
                print (f'el numero {pattern} es incorrecto')
                break
     
            una_vez = False
            messenger.find_user(numero)

        messenger.send_message(f'Enviando mensaje: {mensaje} al numero {numero}')

    time_end=time()

    messenger.send_message(("FIN"))
    messenger.send_message(f"Tiempo ejecuación: {time_end-time_star}")

    print(f"Tiempo ejecuación: {time_end-time_star}")
    sleep(5)
    del messenger


def multiplesnumeros ():
    messenger = w.WhatsApp()
    print (f"2.- envio de 10 mensajes al mismo número")

    una_vez = True

    for i in range (2, sheet.max_row + 1):
        if una_vez:
            time_star=time()
            una_vez = False

        cell_numero =  'A' + str(i)
        cell_mensaje = 'B' + str(i)
        numero = str(sheet[cell_numero].value)[:-2]
        mensaje = sheet[cell_mensaje].value
        print (numero, mensaje)
        messenger.find_user(numero)

        messenger.send_message(f'Enviando mensaje: {mensaje} al numero {numero}')

    time_end=time()

    messenger.send_message(("FIN"))
    messenger.send_message(f"Tiempo ejecuación: {time_end-time_star}")

    print(f"Tiempo ejecuación: {time_end-time_star}")
    sleep(5)
    del messenger

def chek_file(file):
    try:
        libro = load_workbook(file)
        return file
    except:
        msg = f'{file} No existe o no es Excel.'
        raise argparse.ArgumentTypeError(msg)


def main():
    
    parser = argparse.ArgumentParser (description="Envio de mensajes por WhastApp/web", epilog="@jabaselga")
    
    parser.add_argument("-f", metavar="moviles.xlsx", help="Fichero de Excel con los datos.", type=chek_file)
    parser.add_argument("-m", help="Enviar mensaje", action="store_true")
    parser.add_argument("-s", help="Enviar imagen/video/fichero", action="store_true")
    parser.add_argument("-q", metavar="string", help="Quien soy")
    parser.add_argument("-d", help="Simulación, no enviar mensajes ni archivos", action="store_true")
    parser.add_argument("-v", help="Extra info", action="store_true")
    
    args = parser.parse_args()   
    
    if not (args.m or args.s):
        parser.error('Ninguna tarea por hacer.')

    enviar_mensaje = args.m
    enviar_fichero = args.s

    if args.f:
        file = args.f
    else:
        file = 'moviles.xlsx'

    # Abrir excel
    wb = load_workbook(file)
    sheet = wb.active

    #unsolonumero(sheet)
    #multiplesnumeros()

    messenger = w.WhatsApp()

    t1 = time()

    for i in range (2, sheet.max_row + 1):
        cell_numero  = 'A' + str(i)
        cell_mensaje = 'B' + str(i)
        cell_fichero = 'C' + str(i)
        cell_qsoy    = 'D' + str(i)
        cell_status  = 'G' + str(i)
        numero  = '34' + str(sheet[cell_numero].value)[:]
        pattern = re.compile("^34\d{9}")
        mensaje = sheet[cell_mensaje].value
        fichero = sheet[cell_fichero].value
        qsoy    = sheet[cell_qsoy].value
        
        
        if qsoy != args.q and args.q != None :
            print (f"no soy yo {qsoy}")
            continue
        
               
        if pattern.fullmatch(numero):
            
            if enviar_mensaje:

                if not args.d:
                    messenger.find_user(numero)
                    messenger.send_message(f'Enviando mensaje: -{mensaje}- al numero {numero}')

                print (f'Enviando mensaje: -{mensaje}- al numero {numero}')

            if enviar_fichero:
                # comprobar si ha fichero para enviar y existe
                # sacar tipo de fichero
                # enviar segun tipo de fichero
                if fichero and os.path.isfile(fichero): 
                    name, ext = os.path.splitext(fichero)
                    
                    if not args.d:
                        messenger.find_user(numero)
                    
                    if ext in [".tiff", ".pjp", ".jfif", ".gif", ".svg", ".bmp", ".png", ".jpeg", ".svgz", ".jpg", ".webp", ".ico", ".xbm", ".dib", ".tif", ".pjpeg", ".avif", ".m4v", ".mp4", ".3gpp", ".mov"]:
                        if not args.d:
                            messenger.send_picture(fichero)
                        print (f'Enviando imagen/video {fichero} al número: {numero}')
                    else:
                        if not args.d:
                            messenger.send_file(fichero)
                        print (f'Enviando fichero {fichero} al número: {numero}')
                else:
                    print (f'No hay fichero pare enviar al numero {numero}')

            sheet[cell_status].font = Font(color="00F000")
            sheet[cell_status] = 'Enviado'
            if not args.d:
                wb.save(file)

        else:
            print (f'el numero {numero} es incorrecto')
            sheet[cell_status].font = Font(color="FF0000")
            sheet[cell_numero].font = Font(color="FF0000")
            sheet[cell_status] = 'ERROR'
            if not args.d:
                wb.save(file)

        #print (numero, mensaje, fichero)
    sleep(2)
    t2 = time()

    print (f'El proceso ha durado {t2-t1} segundos.')

if __name__=='__main__':
    main ()



