from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario, Traslados, Ambulancias
import json
# Create your views here.
class UsuarioView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) 
    
    def post(self, request):
        usr = json.loads(request.body)
        if usr['tipo']=="datosUsuarios":
            print("Resultado Usuarios")
            datos = list(Usuario.objects.values())
            listNombreUsuario = []
            listApellidoUsuario = []
            listFechaNacimiento = []
            listDireccion = []
            listTelefono = []
            listUsuario = []
            listContrasena = []
            for users in datos:
                for campo, valor in users.items():
                    if campo == "NombreUsuario":
                        listNombreUsuario.append(valor)
                    if campo == "ApellidoUsuario":
                       listApellidoUsuario.append(valor)
                    if campo == "FechaNacimiento":
                        listFechaNacimiento.append(valor)
                    if campo == "Direccion":
                        listDireccion.append(valor)
                    if campo == "Telefono":
                        listTelefono.append(valor)
                    if campo == "Usuario":
                        listUsuario.append(valor)
                    if campo == "Contrasena":
                        listContrasena.append(valor)
            dato={
                "NombreUsuario": listNombreUsuario,
                "ApellidoUsuario": listApellidoUsuario,
                "FechaNacimiento": listFechaNacimiento,
                "Direccion": listDireccion,
                "Telefono": listTelefono,
                "Usuario": listUsuario,
                "Contrasena":listContrasena
            }    
            print (dato)
            return JsonResponse(dato)
        
#Ingresar datos:
        if usr['tipo'] == "registroUsuarios":
            jd = json.loads(request.body)
            Usuario.objects.create(NombreUsuario=jd['NombreUsuario'],ApellidoUsuario=jd['ApellidoUsuario'],
                               FechaNacimiento=jd['FechaNacimiento'],Direccion=jd['Direccion'],Telefono=jd['Telefono'],
                               Usuario=jd['Usuario'],Contrasena=jd['Contrasena'])
            return JsonResponse({'message':'Dato Registrado'})
    
    def put(self,request,id):
        jd=json.loads(request.body)
        usuarios=list(Usuario.objects.filter(id=id).values())
        if len(usuarios) > 0:
            usuario=Usuario.objects.get(id=id)
            usuario.NombreUsuario=jd['NombreUsuario']
            usuario.ApellidoUsuario=jd['ApellidoUsuario']
            usuario.FechaNacimiento=jd['FechaNacimiento']
            usuario.Direccion=jd['Direccion']
            usuario.Telefono=jd['Telefono']
            usuario.Usuario=jd['Usuario']
            usuario.Contrasena=jd['Contrasena']
            usuario.save()
            datos = {'message': "Success"}
        else:  
            datos={'message':"User not found..."}
        return JsonResponse(datos)
    
    def delete(self,request,id):
        usuarios=list(Usuario.objects.filter(id=id).values())
        if len(usuarios) > 0:
            Usuario.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos={'message':"User not found..."}
        return JsonResponse(datos)

class GraficaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) 
    def post(self, request):
        tras = json.loads(request.body)
        if tras['tipo'] == 'infoGraficas':
            RegistrosTraslados = list(Traslados.objects.values())
            # RegistrosAmbulancias = list(Ambulancias.objects.all().values('TipoHerida')
            # .annotate(totTipoHerida=Sum(I('CantidadH'),output_field=models.IntegerField())))
            RegistrosAmbulancias = (Ambulancias.objects.raw('select id, TipoHerida, sum(CantidadH) as Cantidad from appapi_ambulancias group by TipoHerida'))
            print(RegistrosAmbulancias)
            # for reg in RegistrosAmbulancias:
            #     print(reg.TipoHerida + ' ' + str(reg.Cantidad))
            
            DatosTraslados=[]
            DatosAmbulancias = []
            for RegistroD in RegistrosTraslados:
                DatosTraslados.append({'name':RegistroD['Mes'],'value':RegistroD['Cantidad']})
            for RegAmb in RegistrosAmbulancias:
                DatosAmbulancias.append({'name':RegAmb.TipoHerida,'value':RegAmb.Cantidad})
            tras = {'infoGraficas':[{
                                 'name': "Traslados",
                                 'series': DatosTraslados
                                 },
                                    {
                                 'name': "Ambulancias",
                                 'series': DatosAmbulancias
                                 }  
                                     ]
                    }
           
            return JsonResponse(tras)
        
        
    
    

class TrasladosView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) 
    def post(self, request):
        tras = json.loads(request.body)
        if (tras['tipo'] == 'agTraslados'):
            Mes = tras['Mes']
            Cantidad = tras['Cantidad']
            Traslados.objects.create(Mes=tras['Mes'],Cantidad=tras['Cantidad'])
            return JsonResponse({'message':'Dato registrado correctamente'})
        
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
"""#Mostrar datos:
    def post(self, request):
        tras = json.loads(request.body)
        
        if tras['tipo']=="DatosTraslados":
            print("Resultado Traslados")
            datos = list(Traslados.objects.values())
            listmes = []
            listcantidad = []
            for traslate in datos:
                for campo, valor in traslate.items():
                    if campo == "Mes":
                        listmes.append(valor)
                    if campo == "Cantidad":
                       listcantidad.append(valor)
            dato={
                "Mes": listmes,
                "Cantidad": listcantidad
            }    
            print(dato)
            return JsonResponse(dato)
#Ingresar datos:
        if tras['tipo'] == "agregarTraslados":
            jd = json.loads(request.body)
            Traslados.objects.create(Mes=jd['Mes'],Cantidad=jd['Cantidad'])
            return JsonResponse({'message':'Dato Registrado'})
        
#Actualizar datos:
        if tras['tipo'] == "actualizarTraslados":
            jd = json.loads(request.body)
            ActDatos=(Traslados.objects.filter(Mes=jd['Mes']).values())
            if len(ActDatos) > 0:
                TrasladosAct=TrasladosAct.objects.get(Mes=jd['Mes'])
                TrasladosAct.Mes = jd['Mes']
                TrasladosAct.Cantidad = jd['Cantidad']
                TrasladosAct.save()
                dato={'message':"Datos editados"}
            return JsonResponse(dato)
#Eliminar datos:   
        if tras['tipo'] == "borrarTraslados":
            jd = json.loads(request.body)
            ActDatos=(Traslados.objects.filter(Mes=jd['Mes']).values())
            if len (ActDatos) > 0:
                TrasladosAct=TrasladosAct.objects.get(Mes=jd['Mes'])
                TrasladosAct.delete()
                dato = {'message':"Dato eliminado"}
            return JsonResponse(dato)"""
            
            
class AmbulanciasView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) 
#Mostrar dato:
    def post(self, request):
        amb = json.loads(request.body)
        if amb['tipo']=="datosAmbulancias":
            print("Resultado Ambulancias")
            datos = list(Traslados.objects.values())
            listIdentificacion = []
            listTipoHerida = []
            listCantidadH = []
            
            for ambulance in datos:
                for campo, valor in ambulance.items():
                    if campo == "Identificacion":
                        listIdentificacion.append(valor)
                    if campo == "TipoHerida":
                       listTipoHerida.append(valor)
                    if campo == "CantidadH":
                        listCantidadH.append(valor)
            dato={
                "Identificacion": listIdentificacion,
                "TipoHerida": listTipoHerida,
                "CantidadH": listCantidadH
            }    
            print (dato)
            return JsonResponse(dato)
#Ingresar datos:
        if amb['tipo'] == "registroAmbulancias":
            jd = json.loads(request.body)
            Ambulancias.objects.create(Identificacion=jd['Identificacion'],TipoHerida=jd['TipoHerida'],CantidadH=jd['CantidadH'])
            return JsonResponse({'message':'Dato Registrado'})
        