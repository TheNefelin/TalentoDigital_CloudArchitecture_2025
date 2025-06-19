# Tarea 1: crear un entorno de AWS Lambda
# 1.Ingrese a su entorno del laboratorio de aprendizaje de AWS Academy y comience el laboratorio.
# 2.Abra la Consola de administración de AWS, elija el enlace de AWS sobre la ventana del terminal.
# 3.En la barra Buscar de la consola, escriba Lambday elija el servicio Lambda. Se abrirá la consola de AWS Lambda.
# 4.En la barra de navegación superior, verifique que la región de AWS se configure a N. Virginia(us-east-1).
# 5.Elija Crear una función y use la siguiente configuración:
#   •Nombre:escriba un nombre para la función de AWS Lambda, comomyFunction.
#   •Tiempo de ejecución:Python 3.13
#   •Arquitectura:x86_64
#   •Permisos: elija Cambiar el rol de ejecución predeterminado.
#   •Rol de ejecución: elija Uso de un rol existente.
#   •Rol existente: elija LabRole


import json

def lambda_handler(event, context):
  #Obtenga la dirección de correo electrónico del evento
  email = event['email']
  #Validar la dirección de correo electrónico
  if validate_email(email):
    #Devolver un mensaje de éxito
    return {
      'statusCode': 200,
      'body': json.dumps('Email address is valid!')
    }
  #Devolver un mensaje de error
  else:
    return {
      'statusCode': 400,
      'body': json.dumps('Email address is not valid!')
    }


#Funcion que valida el correo utilizando regex
def validate_email(email):
  import re
  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  if(re.fullmatch(regex, email)):
    return True
  else:
    return False

#Test: {'email': 'user@example.com'}
