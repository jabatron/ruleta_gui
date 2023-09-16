import pywhatkit as pwk


try:
    pwk.sendwhatmsg_instantly("+34616366188", "Mensaje de prueba", 37)
    print ('mensaje enviado')
except:
    print ('error')
    