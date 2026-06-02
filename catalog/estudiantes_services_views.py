from rest_framework.views import APIView
from rest_framework.response import Response

class CalcularNotasView(APIView):
    def post(self, request):
        estudiantes = request.data.get('estudiantes', [])
        resultado = []
        aprobados_count = 0
        total_becas = 0

        for est in estudiantes:
            ponderada = (float(est['nota_parcial']) * 0.4) + (float(est['nota_final']) * 0.6)
            aprobado = ponderada >= 70
            if aprobado: aprobados_count += 1
            
            valor_beca = 0
            if ponderada >= 90: valor_beca = float(est['valor_matricula']) * 0.30
            elif ponderada >= 80: valor_beca = float(est['valor_matricula']) * 0.15
            
            total_becas += valor_beca
            resultado.append({
                "nombre": est['nombre'],
                "nota_ponderada": round(ponderada, 2),
                "aprobado": aprobado,
                "valor_beca": valor_beca
            })
        return Response({"aprobados": aprobados_count, "total_becas": total_becas, "detalle": resultado})

class ProgramarModulosView(APIView):
    def get(self, request):
        horas_disponibles = int(request.query_params.get('horas_disponibles', 0))
        duraciones = [int(x) for x in request.query_params.get('duraciones', '').split(',')]
        
        acumulado, programados = 0, []
        for d in duraciones:
            if acumulado + d <= horas_disponibles:
                acumulado += d
                programados.append(d)
            else: break
            
        return Response({
            "modulos_programados": len(programados),
            "horas_libres": horas_disponibles - acumulado,
            "detalle": programados
        })