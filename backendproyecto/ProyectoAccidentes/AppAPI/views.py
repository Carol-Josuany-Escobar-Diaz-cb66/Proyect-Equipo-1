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
#Mostrar Usuario
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
#Ingresar Usuario
        if usr['tipo'] == "registroUsuarios":
            jd = json.loads(request.body)
            Usuario.objects.create(NombreUsuario=jd['NombreUsuario'],ApellidoUsuario=jd['ApellidoUsuario'],
                               FechaNacimiento=jd['FechaNacimiento'],Direccion=jd['Direccion'],Telefono=jd['Telefono'],
                               Usuario=jd['Usuario'],Contrasena=jd['Contrasena'])
            return JsonResponse({'message':'Usuario Registrado'})
#Actualizar Usuario
        if usr['tipo'] == "actualizarUsuario":
            jd = json.loads(request.body)
            ActUser=(Usuario.objects.filter(NombreUsuario=jd['NombreUsuario']).values())
            if len(ActUser) > 0:
                UsersAct=Usuario.objects.get(NombreUsuario=jd['NombreUsuario'])
                UsersAct.ApellidoUsuario = jd['ApellidoUsuario']
                UsersAct.FechaNacimiento = jd['FechaNacimiento']
                UsersAct.Direccion = jd['Direccion']
                UsersAct.Telefono = jd['Telefono']
                UsersAct.Usuario = jd['Usuario']
                UsersAct.Contrasena = jd['Contrasena']
                UsersAct.save()
                dato={'message':"Usuario actualizado correctamente"}
            return JsonResponse(dato)
#Eliminar Usuario
        if usr['tipo'] == "borrarUsuario":
            jd = json.loads(request.body)
            ActUser=(Usuario.objects.filter(NombreUsuario=jd['NombreUsuario']).values())
            if len (ActUser) > 0:
                UserEli=Usuario.objects.get(NombreUsuario=jd['NombreUsuario'])
                UserEli.delete()
                dato = {'message':"Usuario eliminado"}
            return JsonResponse(dato)
        
        
#---------------------------------------------------------------------------------------------------------------------
#GRAFICA
class GraficaView(View):
    #Mostrar datos en la gráfica:
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
        
        
#----------------------------------------------------------------------------------------------------------------------
#TRASLADOS:
class TrasladosView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request):
    #Mostrar datos de Traslados
        if tras['tipo'] == 'datosTraslados':
            RegistrosTraslados = list(Traslados.objects.values())
            DatosTraslados=[]
            for RegistroD in RegistrosTraslados:
                DatosTraslados.append({'name':(RegistroD['Mes']),'value':(RegistroD['Cantidad'])})
            tras = {'datosTraslados':[{
                                 'name': "Traslados",
                                 'series': DatosTraslados
                                 }
                                     ]
                    }
            return JsonResponse(tras)
#Actualizar datos de Traslados:
        if tras['tipo'] == "actualizarTraslados":
            jd = json.loads(request.body)
            ActDatos=(Traslados.objects.filter(Mes=jd['Mes']).values())
            if len(ActDatos) > 0:
                TrasladosAct=Traslados.objects.get(Mes=jd['Mes'])
                TrasladosAct.Mes = jd['Mes']
                TrasladosAct.Cantidad = jd['Cantidad']
                TrasladosAct.save()
                dato={'message':"Registro actualizado correctamente"}
            return JsonResponse(dato)
#Eliminar datos de Traslados:
        if tras['tipo'] == "borrarTraslados":
            jd = json.loads(request.body)
            ActDatos=(Traslados.objects.filter(Mes=jd['Mes']).values())
            if len (ActDatos) > 0:
                TrasladosEli=Traslados.objects.get(Mes=jd['Mes'])
                TrasladosEli.delete()
                dato = {'message':"Registro eliminado"}
            return JsonResponse(dato)
        
#Listar datos
        if tras['tipo'] == "ListadoTraslados":
            Cantidad = list(Traslados.objects.values().order_by('Mes'))
            lista = {"lista":Cantidad}
            return JsonResponse(lista)
#Registrar datos 
        if (tras['tipo'] == 'registroTraslados'):
            jd = json.loads(request.body)
            Traslados.objects.create(Mes=tras['Mes'],Cantidad=tras['Cantidad'])
            return JsonResponse({'message':'Dato registrado correctamente'})
        
        
#-------------------------------------------------------------------------------------------------------------------------
#AMBULANCIAS
class AmbulanciasView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request):
#Mostrar datos de Ambulancias
        amb = json.loads(request.body)
        if amb['tipo'] == 'datosAmbulancias':
            RegistrosAmbulancias = (Ambulancias.objects.raw('select id, TipoHerida, sum(CantidadH) as Cantidad from appapi_ambulancias group by TipoHerida'))
            print(RegistrosAmbulancias)
            DatosAmbulancias = []
            for RegAmb in RegistrosAmbulancias:
                DatosAmbulancias.append({'name':RegAmb.TipoHerida,'value':RegAmb.Cantidad})
            amb = {'datosAmbulancias':[{
                                 'name': "Ambulancias",
                                 'series': DatosAmbulancias
                                 }
                                     ]
                    }
            return JsonResponse(amb)
#Actualizar datos de Ambulancias
        if amb['tipo'] == "actualizarAmbulancias":
            jd = json.loads(request.body)
            ActDatosAmb=(Ambulancias.objects.filter(TipoHerida=jd['TipoHerida']).values())
            if len(ActDatosAmb) > 0:
                AmbulanciasAct=Ambulancias.objects.get(TipoHerida=jd['TipoHerida'])
                AmbulanciasAct.TipoHerida = jd['TipoHerida']
                AmbulanciasAct.CantidadH = jd['CantidadH']
                AmbulanciasAct.save()
                dato={'message':"Datos modificados correctamente"}
            return JsonResponse(dato)
#Eliminar datos de Ambulancias
        if amb['tipo'] == "borrarAmbulancias":
            jd = json.loads(request.body)
            ActDatosAmb=(Ambulancias.objects.filter(TipoHerida=jd['TipoHerida']).values())
            if len (ActDatosAmb) > 0:
                AmbulanciasEli=Ambulancias.objects.get(TipoHerida=jd['TipoHerida'])
                AmbulanciasEli.delete()
                dato = {'message':"Registro eliminado"}
            return JsonResponse(dato)
#Listar datos
        if amb['tipo'] == "ListadoAmbulancias":
            CantidadH = list(Ambulancias.objects.values().order_by('TipoHerida'))
            lista = {"lista":CantidadH}
            return JsonResponse(lista)
#Registrar datos 
        if (amb['tipo'] == 'registroAmbulancias'):
            jd = json.loads(request.body)
            Ambulancias.objects.create(TipoHerida=amb['TipoHerida'],CantidadH=amb['CantidadH'])
            return JsonResponse({'message':'Dato registrado correctamente'})