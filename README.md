# TPI_OE_TOMBEN
Chatbot de consola en Python para gestión de solicitudes de vacaciones. TPI — Organización Empresarial — TUP UTN
# TomBen Chatbot — Solicitud de Vacaciones

Chatbot de consola desarrollado en Python para automatizar el proceso de solicitud de vacaciones en la empresa **TomBen Soluciones Informáticas**.

Trabajo Práctico Integrador — Organización Empresarial — TUP (UTN)


## Descripción

El bot permite a un empleado solicitar días de vacaciones ingresando su número de legajo. El sistema verifica automáticamente su identidad y saldo de días disponibles, aprobando o rechazando la solicitud sin intervención humana.

## Estructura del proyecto

```
TPI_OE/
├── main.py       # Lógica principal del chatbot
├── db.csv        # Base de datos de empleados
└── README.md     # Este archivo

## Requisitos

- Python 3.6 o superior
- No requiere librerías externas

## Cómo ejecutar

```bash
python main.py


## Flujo del proceso

Inicio
  └─► Ingresá tu legajo
        ├─► Legajo inválido (no es número)     → Error, reintentá
        ├─► Legajo no encontrado               → Error, reintentá
        └─► Legajo OK
              └─► Ingresá días a solicitar
                    ├─► No es número           → Error, reintentá
                    ├─► Número negativo o 0    → Error, reintentá
                    ├─► Saldo insuficiente     → Solicitud rechazada
                    └─► Saldo OK               → Solicitud aprobada ✓

## Base de datos (db.csv)

| Legajo | Nombre   | Días disponibles |
|--------|----------|-----------------|
| 101    | Juan     | 15              |
| 102    | María    | 8               |
| 103    | Paco     | 12              |
| 104    | Tomás    | 5               |
| 105    | Joaquín  | 15              |
| 106    | Benjamín | 21              |
| 107    | Goran    | 12              |


## Ejemplo de uso

Bienvenido al sistema de solicitud de vacaciones de TomBen.
A continuación se verificará su saldo de días disponibles.
Legajo: 102
Bienvenido Maria, a continuación ingrese cuántos días de vacaciones le gustaría solicitar.
Dias solicitados: 5
Verificación exitosa. Usted cuenta con saldo suficiente para 5 día/s.
Su solicitud ha sido registrada. Días restantes: 3. Saludos, TomBen Chatbot.


## Tecnologías utilizadas

| Componente   | Tecnología     |
|--------------|----------------|
| Lenguaje     | Python 3        |
| Interfaz     | Consola (CLI)   |
| Persistencia | CSV             |
| IA utilizada | Claude (Anthropic) |


## Materia

Organización Empresarial — Tecnicatura Universitaria en Programación (TUP) — UTN  
