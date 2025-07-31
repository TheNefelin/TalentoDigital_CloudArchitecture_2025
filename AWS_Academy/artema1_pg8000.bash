pip install pg8000 -t python

# python -> python.zip

#   subir python.zip a layer para lambda (py-pg8000-layer)
#     - **Name**: py-pg8000-layer
#     - **Description**: Capa para conexión a PostgreSQL desde Lambda usando pg8000 
#     - **Upload a .zip file**: python.zip
#     - **Compatible architectures**: x86_64
#     - **Compatible runtimes**: Python 3.13
#   agregar layer a lambda (py-pg8000-layer)
#     - **Custom layers**: py-pg8000-layer
#     - **Version**: 1