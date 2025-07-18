from django.urls import path

from affiliates.views import (
    empleado_solicitudes_afiliacion,
    detalles_solicitud_api,
    aprobar_solicitud,
    rechazar_solicitud,
)
from users.views import (
    gestionar_usuarios,
    crear_usuario,
    editar_usuario,
    desactivar_usuario,
)
from . import views

urlpatterns = [
    path("socio/", views.dashboard_socio, name="dashboard_socio"),
    path("socio/reservas/", views.socio_reservas, name="socio_reservas"),
    path("socio/convenios/", views.socio_convenios, name="socio_convenios"),
    path("socio/noticias/", views.socio_noticias, name="socio_noticias"),
    path(
        "socio/notificaciones/", views.socio_notificaciones, name="socio_notificaciones"
    ),
    path("socio/configuracion/", views.socio_configuracion, name="socio_configuracion"),
    path("socio/soporte/", views.socio_soporte, name="socio_soporte"),
    path("empleado/", views.dashboard_empleado, name="dashboard_empleado"),
    path(
        "empleado/usuarios/",
        gestionar_usuarios,
        name="gestion_usuarios",
    ),
    path("empleado/usuarios/crear", crear_usuario, name="crear_usuario"),
    path("empleado/usuarios/<int:pk>/editar/", editar_usuario, name="editar_usuario"),
    path(
        "empleado/usuarios/<int:pk>/desactivar/",
        desactivar_usuario,
        name="desactivar_usuario",
    ),
    path(
        "empleado/afiliaciones/",
        empleado_solicitudes_afiliacion,
        name="gestion_afiliaciones",
    ),
    path(
        "api/solicitud/<int:pk>/",
        detalles_solicitud_api,
        name="detalles_solicitud_api",
    ),
    path(
        "empleado/afiliacion/<int:pk>/aprobar/",
        aprobar_solicitud,
        name="aprobar_solicitud",
    ),
    path(
        "empleado/afiliacion/<int:pk>/rechazar/",
        rechazar_solicitud,
        name="rechazar_solicitud",
    ),
    path("empleado/convenios/", views.empleado_convenios, name="empleado_convenios"),
    path(
        "empleado/espacios-servicios/",
        views.empleado_espacios_servicios,
        name="empleado_espacios_servicios",
    ),
    path(
        "empleado/noticias-eventos/",
        views.empleado_noticias_eventos,
        name="empleado_noticias_eventos",
    ),
    path("empleado/metricas/", views.empleado_metricas, name="empleado_metricas"),
    path(
        "empleado/configuracion/",
        views.empleado_configuracion,
        name="empleado_configuracion",
    ),
    path("empleado/soporte/", views.empleado_soporte, name="empleado_soporte"),
]
