# Sistema de Gestión de Control de Plagas

Sistema de consola desarrollado en Python para administrar los servicios, clientes y facturación de una empresa de control de plagas. 

## Características Principales

*   **Registro de Servicios:** Carga de ubicaciones, tipos de contrato (Puntual o Trimestral con descuento) y múltiples tratamientos (Roedores, Cucarachas, Hormigas, etc.).
*   **Gestión de Clientes:** Búsqueda por dirección, barrio o monto exacto. Permite agregar nuevos servicios a clientes existentes y recalcular su deuda.
*   **Categoría Premium:** Asignación automática del estado "Premium" para facturaciones que superen los $25.000.
*   **Estadísticas del Día:** Cálculo automático de la recaudación total, cantidad de servicios y promedio de cobro por departamento.
*   **Reportes y Ranking:** Identificación de los pagos máximos y mínimos, y listado de clientes ordenado de mayor a menor facturación.

## Requisitos

*   Python 3.x

## Instalación y Uso

1. Cloná este repositorio.
2. Ejecutá el archivo principal desde tu terminal:

```bash
python "SistemaDeGestionDeControlDePlagas_Grupo1 3.py"
