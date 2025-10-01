"""
Cliente de Correo Electrónico - Entrega 1
Modelado de Clases y Encapsulamiento

Este módulo implementa las clases principales del sistema:
- Usuario: Gestiona la información del usuario
- Mensaje: Representa un email individual
- Carpeta: Contiene mensajes organizados
- ServidorCorreo: Gestiona usuarios y operaciones de correo
"""

from datetime import datetime
from typing import List, Optional
from enum import Enum


class EstadoMensaje(Enum):
    """Estados posibles de un mensaje"""
    NO_LEIDO = "no_leido"
    LEIDO = "leido"
    RESPONDIDO = "respondido"
    REENVIADO = "reenviado"


class PrioridadMensaje(Enum):
    """Niveles de prioridad de un mensaje"""
    BAJA = 1
    NORMAL = 2
    ALTA = 3
    URGENTE = 4


class Mensaje:
    """
    Representa un mensaje de correo electrónico.
    Encapsula toda la información relacionada con un email.
    """
    
    def __init__(self, remitente: str, destinatarios: List[str], asunto: str, 
                 cuerpo: str, prioridad: PrioridadMensaje = PrioridadMensaje.NORMAL):
        self.__id = id(self)  # ID único del mensaje
        self.__remitente = remitente
        self.__destinatarios = destinatarios.copy()
        self.__asunto = asunto
        self.__cuerpo = cuerpo
        self.__fecha_envio = datetime.now()
        self.__estado = EstadoMensaje.NO_LEIDO
        self.__prioridad = prioridad
        self.__adjuntos = []
    
    # Propiedades de solo lectura
    @property
    def id(self) -> int:
        """ID único del mensaje"""
        return self.__id
    
    @property
    def remitente(self) -> str:
        """Dirección del remitente"""
        return self.__remitente
    
    @property
    def destinatarios(self) -> List[str]:
        """Lista de destinatarios (copia para evitar modificaciones)"""
        return self.__destinatarios.copy()
    
    @property
    def asunto(self) -> str:
        """Asunto del mensaje"""
        return self.__asunto
    
    @property
    def cuerpo(self) -> str:
        """Cuerpo del mensaje"""
        return self.__cuerpo
    
    @property
    def fecha_envio(self) -> datetime:
        """Fecha y hora de envío"""
        return self.__fecha_envio
    
    @property
    def prioridad(self) -> PrioridadMensaje:
        """Prioridad del mensaje"""
        return self.__prioridad
    
    # Propiedades con setter
    @property
    def estado(self) -> EstadoMensaje:
        """Estado actual del mensaje"""
        return self.__estado
    
    @estado.setter
    def estado(self, nuevo_estado: EstadoMensaje):
        """Actualiza el estado del mensaje"""
        if isinstance(nuevo_estado, EstadoMensaje):
            self.__estado = nuevo_estado
        else:
            raise ValueError("El estado debe ser un valor de EstadoMensaje")
    
    def marcar_como_leido(self):
        """Marca el mensaje como leído"""
        self.__estado = EstadoMensaje.LEIDO
    
    def marcar_como_respondido(self):
        """Marca el mensaje como respondido"""
        self.__estado = EstadoMensaje.RESPONDIDO
    
    def agregar_adjunto(self, nombre_archivo: str):
        """Agrega un adjunto al mensaje"""
        if nombre_archivo not in self.__adjuntos:
            self.__adjuntos.append(nombre_archivo)
    
    def obtener_adjuntos(self) -> List[str]:
        """Retorna la lista de adjuntos"""
        return self.__adjuntos.copy()
    
    def __str__(self) -> str:
        return f"De: {self.remitente} | Asunto: {self.asunto} | Estado: {self.estado.value}"
    
    def __repr__(self) -> str:
        return f"Mensaje(id={self.id}, remitente='{self.remitente}', asunto='{self.asunto}')"


class Carpeta:
    """
    Representa una carpeta que contiene mensajes.
    Permite organizar y gestionar colecciones de mensajes.
    """
    
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__mensajes = []
        self.__fecha_creacion = datetime.now()
    
    @property
    def nombre(self) -> str:
        """Nombre de la carpeta"""
        return self.__nombre
    
    @property
    def cantidad_mensajes(self) -> int:
        """Número de mensajes en la carpeta"""
        return len(self.__mensajes)
    
    @property
    def fecha_creacion(self) -> datetime:
        """Fecha de creación de la carpeta"""
        return self.__fecha_creacion
    
    def agregar_mensaje(self, mensaje: Mensaje):
        """Agrega un mensaje a la carpeta"""
        if isinstance(mensaje, Mensaje):
            self.__mensajes.append(mensaje)
        else:
            raise ValueError("Solo se pueden agregar objetos de tipo Mensaje")
    
    def eliminar_mensaje(self, mensaje_id: int) -> bool:
        """Elimina un mensaje por su ID. Retorna True si se eliminó exitosamente"""
        for i, mensaje in enumerate(self.__mensajes):
            if mensaje.id == mensaje_id:
                del self.__mensajes[i]
                return True
        return False
    
    def buscar_por_remitente(self, remitente: str) -> List[Mensaje]:
        """Busca mensajes por remitente"""
        return [msg for msg in self.__mensajes if remitente.lower() in msg.remitente.lower()]
    
    def buscar_por_asunto(self, asunto: str) -> List[Mensaje]:
        """Busca mensajes por asunto"""
        return [msg for msg in self.__mensajes if asunto.lower() in msg.asunto.lower()]
    
    def listar_mensajes(self) -> List[Mensaje]:
        """Retorna una copia de la lista de mensajes"""
        return self.__mensajes.copy()
    
    def obtener_no_leidos(self) -> List[Mensaje]:
        """Retorna mensajes no leídos"""
        return [msg for msg in self.__mensajes if msg.estado == EstadoMensaje.NO_LEIDO]
    
    def __str__(self) -> str:
        return f"Carpeta '{self.nombre}' ({self.cantidad_mensajes} mensajes)"
    
    def __repr__(self) -> str:
        return f"Carpeta(nombre='{self.nombre}', mensajes={self.cantidad_mensajes})"


class Usuario:
    """
    Representa un usuario del sistema de correo electrónico.
    Gestiona la información personal y las carpetas del usuario.
    """
    
    def __init__(self, nombre: str, email: str, contraseña: str):
        self.__nombre = nombre
        self.__email = email
        self.__contraseña = contraseña  # En un sistema real, esto debería estar hasheado
        self.__carpetas = {}
        self.__fecha_registro = datetime.now()
        
        # Crear carpetas predeterminadas
        self._crear_carpetas_predeterminadas()
    
    def _crear_carpetas_predeterminadas(self):
        """Crea las carpetas básicas del sistema de correo"""
        carpetas_basicas = ["Entrada", "Enviados", "Borradores", "Papelera"]
        for nombre_carpeta in carpetas_basicas:
            self.__carpetas[nombre_carpeta] = Carpeta(nombre_carpeta)
    
    @property
    def nombre(self) -> str:
        """Nombre del usuario"""
        return self.__nombre
    
    @property
    def email(self) -> str:
        """Dirección de email del usuario"""
        return self.__email
    
    @property
    def fecha_registro(self) -> datetime:
        """Fecha de registro del usuario"""
        return self.__fecha_registro
    
    def verificar_contraseña(self, contraseña: str) -> bool:
        """Verifica si la contraseña es correcta"""
        return self.__contraseña == contraseña
    
    def cambiar_contraseña(self, contraseña_actual: str, contraseña_nueva: str) -> bool:
        """Cambia la contraseña del usuario"""
        if self.verificar_contraseña(contraseña_actual):
            self.__contraseña = contraseña_nueva
            return True
        return False
    
    def crear_carpeta(self, nombre: str) -> bool:
        """Crea una nueva carpeta"""
        if nombre not in self.__carpetas:
            self.__carpetas[nombre] = Carpeta(nombre)
            return True
        return False
    
    def eliminar_carpeta(self, nombre: str) -> bool:
        """Elimina una carpeta (excepto las predeterminadas)"""
        carpetas_protegidas = ["Entrada", "Enviados", "Borradores", "Papelera"]
        if nombre in self.__carpetas and nombre not in carpetas_protegidas:
            del self.__carpetas[nombre]
            return True
        return False
    
    def obtener_carpeta(self, nombre: str) -> Optional[Carpeta]:
        """Obtiene una carpeta por nombre"""
        return self.__carpetas.get(nombre)
    
    def listar_carpetas(self) -> List[str]:
        """Lista los nombres de todas las carpetas"""
        return list(self.__carpetas.keys())
    
    def mover_mensaje(self, mensaje_id: int, carpeta_origen: str, carpeta_destino: str) -> bool:
        """Mueve un mensaje entre carpetas"""
        origen = self.obtener_carpeta(carpeta_origen)
        destino = self.obtener_carpeta(carpeta_destino)
        
        if not origen or not destino:
            return False
        
        # Buscar el mensaje en la carpeta origen
        for mensaje in origen.listar_mensajes():
            if mensaje.id == mensaje_id:
                origen.eliminar_mensaje(mensaje_id)
                destino.agregar_mensaje(mensaje)
                return True
        return False
    
    def __str__(self) -> str:
        return f"Usuario: {self.nombre} ({self.email})"
    
    def __repr__(self) -> str:
        return f"Usuario(nombre='{self.nombre}', email='{self.email}')"


class ServidorCorreo:
    """
    Simula un servidor de correo que gestiona usuarios y operaciones de email.
    Actúa como el núcleo del sistema de correo electrónico.
    """
    
    def __init__(self, nombre_servidor: str):
        self.__nombre_servidor = nombre_servidor
        self.__usuarios = {}  # email -> Usuario
        self.__mensajes_globales = {}  # id -> Mensaje (para tracking global)
        self.__fecha_inicio = datetime.now()
    
    @property
    def nombre_servidor(self) -> str:
        """Nombre del servidor"""
        return self.__nombre_servidor
    
    @property
    def cantidad_usuarios(self) -> int:
        """Número de usuarios registrados"""
        return len(self.__usuarios)
    
    def registrar_usuario(self, nombre: str, email: str, contraseña: str) -> bool:
        """Registra un nuevo usuario en el servidor"""
        if email not in self.__usuarios:
            nuevo_usuario = Usuario(nombre, email, contraseña)
            self.__usuarios[email] = nuevo_usuario
            return True
        return False
    
    def autenticar_usuario(self, email: str, contraseña: str) -> Optional[Usuario]:
        """Autentica un usuario y retorna el objeto Usuario si es válido"""
        usuario = self.__usuarios.get(email)
        if usuario and usuario.verificar_contraseña(contraseña):
            return usuario
        return None
    
    def enviar_mensaje(self, remitente_email: str, destinatarios: List[str], 
                      asunto: str, cuerpo: str, prioridad: PrioridadMensaje = PrioridadMensaje.NORMAL) -> bool:
        """Envía un mensaje desde un usuario a uno o más destinatarios"""
        remitente = self.__usuarios.get(remitente_email)
        if not remitente:
            return False
        
        # Crear el mensaje
        mensaje = Mensaje(remitente_email, destinatarios, asunto, cuerpo, prioridad)
        self.__mensajes_globales[mensaje.id] = mensaje
        
        # Agregar a la carpeta "Enviados" del remitente
        carpeta_enviados = remitente.obtener_carpeta("Enviados")
        if carpeta_enviados:
            carpeta_enviados.agregar_mensaje(mensaje)
        
        # Entregar a los destinatarios que están en este servidor
        for dest_email in destinatarios:
            destinatario = self.__usuarios.get(dest_email)
            if destinatario:
                carpeta_entrada = destinatario.obtener_carpeta("Entrada")
                if carpeta_entrada:
                    # Crear una copia del mensaje para el destinatario
                    mensaje_copia = Mensaje(remitente_email, [dest_email], asunto, cuerpo, prioridad)
                    carpeta_entrada.agregar_mensaje(mensaje_copia)
        
        return True
    
    def listar_usuarios(self) -> List[str]:
        """Lista los emails de todos los usuarios registrados"""
        return list(self.__usuarios.keys())
    
    def obtener_usuario(self, email: str) -> Optional[Usuario]:
        """Obtiene un usuario por su email"""
        return self.__usuarios.get(email)
    
    def obtener_estadisticas(self) -> dict:
        """Retorna estadísticas del servidor"""
        total_mensajes = len(self.__mensajes_globales)
        return {
            "nombre_servidor": self.nombre_servidor,
            "usuarios_registrados": self.cantidad_usuarios,
            "mensajes_totales": total_mensajes,
            "fecha_inicio": self.fecha_inicio
        }
    
    @property
    def fecha_inicio(self) -> datetime:
        """Fecha de inicio del servidor"""
        return self.__fecha_inicio
    
    def __str__(self) -> str:
        return f"Servidor '{self.nombre_servidor}' ({self.cantidad_usuarios} usuarios)"
    
    def __repr__(self) -> str:
        return f"ServidorCorreo(nombre='{self.nombre_servidor}', usuarios={self.cantidad_usuarios})"


# Ejemplo de uso y testing básico
if __name__ == "__main__":
    # Crear servidor
    servidor = ServidorCorreo("MiServidor.com")
    
    # Registrar usuarios
    servidor.registrar_usuario("Juan Pérez", "juan@miservidor.com", "123456")
    servidor.registrar_usuario("María García", "maria@miservidor.com", "abcdef")
    
    # Autenticar usuario
    juan = servidor.autenticar_usuario("juan@miservidor.com", "123456")
    if juan:
        print(f"Usuario autenticado: {juan}")
        
        # Enviar un mensaje
        servidor.enviar_mensaje(
            "juan@miservidor.com",
            ["maria@miservidor.com"],
            "Hola María",
            "¿Cómo estás? Espero que tengas un buen día.",
            PrioridadMensaje.NORMAL
        )
        
        # Ver carpetas de Juan
        print(f"Carpetas de Juan: {juan.listar_carpetas()}")
        
        # Ver mensajes en Enviados
        enviados = juan.obtener_carpeta("Enviados")
        if enviados:
            print(f"Mensajes enviados: {enviados.cantidad_mensajes}")
            for mensaje in enviados.listar_mensajes():
                print(f"  - {mensaje}")
    
    # Autenticar María y ver sus mensajes
    maria = servidor.autenticar_usuario("maria@miservidor.com", "abcdef")
    if maria:
        entrada = maria.obtener_carpeta("Entrada")
        if entrada:
            print(f"\nMensajes en la entrada de María: {entrada.cantidad_mensajes}")
            for mensaje in entrada.listar_mensajes():
                print(f"  - {mensaje}")
                mensaje.marcar_como_leido()
    
    # Estadísticas del servidor
    print(f"\nEstadísticas del servidor:")
    stats = servidor.obtener_estadisticas()
    for key, value in stats.items():
        print(f"  {key}: {value}")
