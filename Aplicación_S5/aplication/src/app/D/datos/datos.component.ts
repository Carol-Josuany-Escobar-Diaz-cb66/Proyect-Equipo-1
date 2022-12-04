import { Component, OnInit} from '@angular/core';
import { Chart, ChartConfiguration} from 'chart.js';
import { NgxChartsModule } from "@swimlane/ngx-charts";
import { DatosService } from '../datos-service.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-datos',
  templateUrl: './datos.component.html',
  styleUrls: ['./datos.component.css']
})
export class DatosComponent {
multi: any[] = [];
view:[number,number]=[700,300];
datos:any;

RegistroD:any;
DatosTraslados={
  'Mes':'',
  'Cantidad':0,
  'tipo':''
}
AddTraslado:boolean = true;
ActualizarTras:boolean = false;

DatosAmbulancias={
  'Identificacion':'',
  'TipoHerida':'',
  'CantidadH':0,
  'tipo':''
}
RegistroA:any;

AddAmbulancias:boolean = true;
ActualizarAmb:boolean = false;



  constructor(private infoGraficas:DatosService, private toastr:ToastrService){
  }

//------------------------------------------TRASLADOS------------------------------------------//
  AgregarTras(){
    if(this.DatosTraslados.Mes !='' && this.DatosTraslados.Cantidad > 0){
      this.DatosTraslados['tipo']= 'registroTraslados';
      this.infoGraficas.AnadirTras(this.RegistroD).subscribe((res)=> {
        if(res.message=='Dato registrado correctamente'){
          alert('Registrado')
        } else {
          alert('No hay registros')
        }
      })
    } else {
      alert('Los campos estan vacios')
    }
  }

  UpdateTras(visible:boolean){
    if(this.DatosTraslados.Mes !='' && this.DatosTraslados.Cantidad > 0){
      this.DatosTraslados['tipo']= 'actualizarTraslados';
      this.infoGraficas.ActuaTras(this.RegistroD).subscribe((res)=> {
        if(res.message=='Registro actualizado correctamente'){
          alert('Actualizar')
        } else {
          alert('No esta actualizado correctamente')
        }
      })
    }
    else {
      alert('No hay datos para actualizar')
    }
  }

  DelTras(Mes:string){
    let form={
      Mes: Mes,
      tipo:'borrarTraslados'
    }
    this.infoGraficas.EliminarTras(form).subscribe((res)=> {
      if(res.message=='Registro eliminado'){
        this.toastr.warning('Registro eliminado');
      }
    })
  }

  Editar(Mes:string, Cantidad:number){
    this.DatosTraslados.Mes = Mes;
    this.DatosTraslados.Cantidad = Cantidad;
    this.AddTraslado= false;
    this.ActualizarTras= true;
  }

//------------------------------------------Final Traslados------------------------------------------//

//------------------------------------------Ambulancias------------------------------------------//

AgregarAmb(){
  if(this.DatosAmbulancias. Identificacion!='' && this.DatosAmbulancias.TipoHerida!='' && this.DatosAmbulancias.CantidadH > 0){
    this.DatosAmbulancias['tipo']= 'registroAmbulancias';
    this.infoGraficas.AnadirAmb(this.RegistroA).subscribe((res)=> {
      if(res.message=='Dato registrado correctamente'){
        this.toastr.success('Registrado')
      } else {
        this.toastr.warning('No hay registros')
      }
    })
  } else {
    this.toastr.error('Los campos estan vacios')
  }
}

UpdateAmb(visible:boolean){
  if(this.DatosAmbulancias.Identificacion!='' && this.DatosAmbulancias.TipoHerida!='' && this.DatosAmbulancias.CantidadH > 0){
    this.DatosAmbulancias['tipo']= 'actualizarAmbulancias';
    this.infoGraficas.ActuaTras(this.RegistroA).subscribe((res)=> {
      if(res.message=='Datos modificados correctamente'){
        this.toastr.success('Actualizar datos')
      } else {
        this.toastr.warning('No esta actualizado correctamente')
      }
    })
  }
  else {
    this.toastr.error('No hay datos para actualizar','Faltan datos',{timeOut:2000})
  }
}

DelAmb(TipoHerida:string){
  let form={
    TipoHerida: TipoHerida,
    tipo:'borrarAmbulancias'
  }
  this.infoGraficas.EliminarAmb(form).subscribe((res)=> {
    if(res.message=='Registro eliminado'){
      this.toastr.warning('Registro eliminado');
    }
  })
}

EditarAmb(Identificacion:string,TipoHerida:string, CantidadH:number){
  this.DatosAmbulancias.Identificacion = Identificacion;
  this.DatosAmbulancias.TipoHerida = TipoHerida;
  this.DatosAmbulancias.CantidadH = CantidadH;
  this.AddAmbulancias= false;
  this.ActualizarAmb= true;
}

//------------------------------------------Final Ambulancias------------------------------------------//

  ngOnInit(){
    let form={
      tipo:"infoGraficas"
    }
    this.infoGraficas.infoGraficas(form).subscribe((res: any)=>{
      this.multi=res.datosgraficos;
    })
  }

  //options
  legend:boolean = true;
  showLabels:boolean = true;
  animations:boolean = true;
  xAxis:boolean = true;
  yAxis:boolean = true;
  showYAxisLabel:boolean = true;
  showXAxisLabel:boolean = true;
  xAxisLabel:string = '';
  yAxisLabel:string = '';
  timeline:boolean = true;

  colorScheme = {
    domain: ['#5AA454']
  };

  onSelect(event: any){
    console.log(event);
  }
}

