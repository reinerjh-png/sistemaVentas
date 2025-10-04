import requests
from django.http import JsonResponse
from .models import Cliente

def buscar_cliente_por_ruc(request):
    ruc = request.GET.get("ruc", "")
    if not ruc:
        return JsonResponse({"error": "No se envió RUC"}, status=400)

    # Primero buscar en la base de datos local
    cliente = Cliente.objects.filter(ruc=ruc).first()
    if cliente:
        return JsonResponse({
            "ruc": cliente.ruc,
            "nombre": cliente.nombre,
            "direccion": cliente.direccion or ""
        })

    # Si no está en la BD, consultar API SUNAT
    url = f"https://api.apis.net.pe/v1/ruc?numero={ruc}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            nombre = data.get("nombre", "")
            direccion = data.get("direccion", "")

            # Guardar en la BD para futuras consultas
            cliente = Cliente.objects.create(ruc=ruc, nombre=nombre, direccion=direccion)

            return JsonResponse({
                "ruc": ruc,
                "nombre": nombre,
                "direccion": direccion
            })
        else:
            return JsonResponse({"error": "No encontrado en SUNAT"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
