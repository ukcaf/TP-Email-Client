📧 Cliente de Correo Electrónico
Sistema orientado a objetos que simula un cliente de correo electrónico completo, desarrollado en Python como proyecto académico para la materia Estructuras de Datos.
📋 Descripción del Proyecto
Este proyecto implementa un sistema de correo electrónico funcional que permite gestionar usuarios, mensajes, carpetas y operaciones típicas de un entorno de email. El desarrollo se realiza en 4 entregas progresivas, cada una agregando funcionalidades más avanzadas.
Objetivos

Aplicar conceptos de Programación Orientada a Objetos (POO)
Implementar y analizar estructuras de datos complejas
Desarrollar algoritmos eficientes para operaciones de correo
Crear un sistema escalable y mantenible

🚀 Estado del Proyecto
✅ Entrega 1: Modelado de Clases y Encapsulamiento (COMPLETADO)

 Definición de clases principales: Usuario, Mensaje, Carpeta, ServidorCorreo
 Encapsulamiento completo con propiedades y métodos de acceso
 Interfaces para enviar, recibir y listar mensajes
 Documentación completa con diagramas de clases

🔄 Entrega 2: Estructuras de Datos y Recursividad (EN DESARROLLO)

 Gestión de carpetas y subcarpetas como estructura de árbol
 Operaciones recursivas de búsqueda
 Análisis de eficiencia de operaciones

📅 Entrega 3: Algoritmos y Funcionalidades Avanzadas (PENDIENTE)

 Filtros automáticos con reglas personalizadas
 Cola de prioridades para mensajes urgentes
 Red de servidores modelada como grafo
 Simulación de envío entre servidores (BFS/DFS)

📅 Entrega 4: Integración y Presentación Final (PENDIENTE)

 Interfaz de línea de comandos (CLI)
 Integración completa de todas las funcionalidades
 Documentación final
 Defensa oral del proyecto

🛠️ Tecnologías Utilizadas

Lenguaje: Python 3.8+
Paradigma: Programación Orientada a Objetos
Librerías estándar:

datetime - Manejo de fechas y timestamps
typing - Type hints para mejor documentación
enum - Enumeraciones tipadas



📦 Instalación
Requisitos Previos

Python 3.8 o superior
Git

Clonar el Repositorio
bashgit clone https://github.com/tu-usuario/cliente-correo-electronico.git
cd cliente-correo-electronico
Verificar Instalación
bashpython --version  # Debe mostrar Python 3.8 o superior
python cliente_correo.py  # Ejecuta el ejemplo de demostración
💻 Uso del Sistema
Ejemplo Básico
pythonfrom cliente_correo import ServidorCorreo, PrioridadMensaje

# 1. Crear servidor
servidor = ServidorCorreo("empresa.com")

# 2. Registrar usuarios
servidor.registrar_usuario("Ana López", "ana@empresa.com", "password123")
servidor.registrar_usuario("Carlos Ruiz", "carlos@empresa.com", "password456")

# 3. Autenticar usuario
ana = servidor.autenticar_usuario("ana@empresa.com", "password123")

# 4. Enviar mensaje
if ana:
    servidor.enviar_mensaje(
        remitente_email="ana@empresa.com",
        destinatarios=["carlos@empresa.com"],
        asunto="Reunión de equipo",
        cuerpo="Hola Carlos, ¿podemos reunirnos mañana?",
        prioridad=PrioridadMensaje.ALTA
    )

# 5. Verificar mensajes recibidos
carlos = servidor.obtener_usuario("carlos@empresa.com")
entrada = carlos.obtener_carpeta("Entrada")
mensajes = entrada.listar_mensajes()

for mensaje in mensajes:
    print(f"De: {mensaje.remitente}")
    print(f"Asunto: {mensaje.asunto}")
    mensaje.marcar_como_leido()
Funcionalidades Disponibles
Gestión de Usuarios

✉️ Registro de nuevos usuarios
🔐 Autenticación con contraseña
👤 Perfil de usuario con información personal

Gestión de Mensajes

📤 Envío de mensajes a uno o múltiples destinatarios
📥 Recepción automática en bandeja de entrada
🏷️ Estados: No leído, Leído, Respondido, Reenviado
⚡ Prioridades: Baja, Normal, Alta, Urgente
📎 Soporte para adjuntos

Organización

📁 Carpetas predeterminadas: Entrada, Enviados, Borradores, Papelera
➕ Creación de carpetas personalizadas
🔄 Movimiento de mensajes entre carpetas
🗑️ Eliminación de mensajes y carpetas

Búsqueda y Filtrado

🔍 Búsqueda por remitente
🔍 Búsqueda por asunto
📊 Filtro de mensajes no leídos
📈 Estadísticas del servidor

📁 Estructura del Proyecto
cliente-correo-electronico/
│
├── cliente_correo.py          # Código principal del sistema
├── README.md                  # Este archivo
├── requirements.txt           # Dependencias del proyecto
│
├── docs/                      # Documentación
│   ├── diagrama_clases.svg    # Diagrama de clases visual
│   ├── diagrama_clases.puml   # Código PlantUML
│   ├── justificacion_diseno.md # Decisiones de diseño
│   └── documentacion_tecnica.md # Documentación técnica completa
│
├── tests/                     # Tests unitarios
│   ├── test_mensaje.py
│   ├── test_carpeta.py
│   ├── test_usuario.py
│   └── test_servidor.py
│
└── ejemplos/                  # Ejemplos de uso
    ├── ejemplo_basico.py
    ├── ejemplo_avanzado.py
    └── demo_completa.py
🏗️ Arquitectura del Sistema
Clases Principales
Mensaje
Representa un email individual con toda su información asociada.
Atributos principales:

id, remitente, destinatarios, asunto, cuerpo
fecha_envio, estado, prioridad, adjuntos

Características:

Inmutable (excepto estado y adjuntos)
Generación automática de ID único
Timestamp de envío automático

Carpeta
Contenedor para organizar mensajes.
Funcionalidades:

Agregar/eliminar mensajes
Búsquedas por remitente y asunto
Filtrado de mensajes no leídos
Listado completo de mensajes

Usuario
Gestiona la identidad del usuario y sus carpetas.
Funcionalidades:

Autenticación con contraseña
Gestión de carpetas personalizadas
Movimiento de mensajes entre carpetas
Carpetas predeterminadas protegidas

ServidorCorreo
Núcleo del sistema que coordina todas las operaciones.
Responsabilidades:

Registro y autenticación de usuarios
Coordinación de envío de mensajes
Tracking global de mensajes
Generación de estadísticas

Principios de Diseño
El sistema está construido siguiendo los principios SOLID:

Single Responsibility: Cada clase tiene una responsabilidad única
Open/Closed: Abierto para extensión, cerrado para modificación
Liskov Substitution: Subtipos intercambiables
Interface Segregation: Interfaces específicas y cohesivas
Dependency Inversion: Dependencia de abstracciones

🧪 Tests
Ejecutar Tests Unitarios
bash# Ejecutar todos los tests
python -m unittest discover tests

# Ejecutar test específico
python -m unittest tests.test_mensaje
Cobertura de Tests

✅ Creación y manipulación de mensajes
✅ Operaciones de carpetas
✅ Gestión de usuarios
✅ Envío y recepción de emails
✅ Búsquedas y filtros
✅ Casos límite y errores

📊 Análisis de Complejidad
Complejidad Temporal
OperaciónComplejidadJustificaciónCrear mensajeO(1)Asignación directaAgregar a carpetaO(1)Append a listaBuscar por remitenteO(n)Búsqueda linealAutenticar usuarioO(1)Acceso a diccionarioEnviar mensajeO(k)k = destinatarios
Complejidad Espacial

Por mensaje: O(1) - Tamaño fijo
Por carpeta con n mensajes: O(n)
Sistema completo: O(u × k × n) donde u=usuarios, k=carpetas, n=mensajes

👥 Equipo de Desarrollo

[Tu Nombre] - [tu-email@example.com]
[Compañero 1] - [email@example.com]
[Compañero 2] - [email@example.com] (opcional)

📚 Referencias y Recursos

Documentación oficial de Python
PEP 8 - Style Guide for Python Code
Type Hints - PEP 484
Apuntes de la materia Estructuras de Datos - UNaB 2025

📄 Licencia
Este proyecto es de carácter académico y está desarrollado para la materia Estructuras de Datos de la Universidad Nacional de Buenos Aires (UNaB).
🤝 Contribuciones
Este es un proyecto académico cerrado. No se aceptan contribuciones externas durante el desarrollo de la materia.
📞 Contacto y Soporte
Para consultas sobre el proyecto:

Docente de la materia: [email-docente@unab.edu.ar]
Issues: Utilizar la sección de Issues de GitHub para reportar problemas

🔄 Historial de Versiones
v1.0.0 - Entrega 1 (Fecha)

✨ Implementación de clases base
📝 Documentación completa
🎨 Diagrama de clases
🧪 Tests unitarios básicos

v2.0.0 - Entrega 2 (Pendiente)

🌳 Estructura de árbol para carpetas
🔁 Operaciones recursivas
📊 Análisis de eficiencia

v3.0.0 - Entrega 3 (Pendiente)

🔍 Sistema de filtros
⚡ Cola de prioridades
🌐 Red de servidores con grafos

v4.0.0 - Entrega 4 (Pendiente)

💻 Interfaz CLI
🔗 Integración completa
🎓 Presentación final


⭐ Si te gusta este proyecto, dale una estrella en GitHub!
📌 Última actualización: [30/09/2025]
