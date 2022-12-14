import { Component, OnInit } from '@angular/core';
import { Chart, ChartConfiguration } from 'chart.js';
import { NgxChartsModule } from "@swimlane/ngx-charts";
import { DatosService } from '../datos-service.service';


@Component({
  selector: 'app-datos',
  templateUrl: './datos.component.html',
  styleUrls: ['./datos.component.css']
})
export class DatosComponent {
  multi: any[] = [];
  view: [number, number] = [700, 300];
  datos: any;

  RegistroD: any;
  DatosTraslados = {
    'Mes': '',
    'Cantidad': 0,
    'tipo': ''
  }
  AddTraslado: boolean = true;
  ActualizarTras: boolean = false;

  DatosAmbulancias = {
    'Identificacion': '',
    'TipoHerida': '',
    'CantidadH': 0,
    'tipo': ''
  }
  RegistroA: any;

  AddAmbulancias: boolean = true;
  ActualizarAmb: boolean = false;



  constructor(private infoGraficas: DatosService) {
  }

  //------------------------------------------TRASLADOS------------------------------------------//
  AgregarTras() {
    if (this.DatosTraslados.Mes != '' && this.DatosTraslados.Cantidad > 0) {
      this.DatosTraslados['tipo'] = 'registroTraslados';
      this.infoGraficas.AnadirTras(this.DatosTraslados).subscribe((res) => {
        if (res.message == 'Dato registrado correctamente') {

          this.ngOnInit();
        } else {
          alert('No hay registros')
        }
      })
    } else {
      alert('Los campos estan vacios')
    }
  }

  UpdateTras(visible: boolean) {
    if (visible) {
      if (this.DatosTraslados.Mes != '' && this.DatosTraslados.Cantidad > 0) {
        this.DatosTraslados['tipo'] = 'actualizarTraslados';
        this.infoGraficas.ActuaTras(this.DatosTraslados).subscribe((res) => {
          if (res.message == 'Registro actualizado correctamente') {

            this.ngOnInit();
          } else {
            alert('No esta actualizado correctamente')
          }
        })
      }
      else {
        alert('No hay datos para actualizar')
      }
    }
    this.AddTraslado = true;
    this.ActualizarTras = false;
  }

  DelTras(Mes: string) {
    let form = {
      Mes: Mes,
      tipo: 'borrarTraslados'
    }
    this.infoGraficas.EliminarTras(form).subscribe((res) => {
      if (res.message == 'Registro eliminado') {
        alert('Registro eliminado');
        this.ngOnInit();
      }
    })
  }

  Editar(Mes: string, Cantidad: number) {
    this.DatosTraslados.Mes = Mes;
    this.DatosTraslados.Cantidad = Cantidad;
    this.AddTraslado = false;
    this.ActualizarTras = true;
  }

  //------------------------------------------Final Traslados------------------------------------------//

  //------------------------------------------Ambulancias------------------------------------------//

  AgregarAmb() {
    if (this.DatosAmbulancias.Identificacion != '' && this.DatosAmbulancias.TipoHerida != '' && this.DatosAmbulancias.CantidadH > 0) {
      this.DatosAmbulancias['tipo'] = 'registroAmbulancias';
      this.infoGraficas.AnadirAmb(this.DatosAmbulancias).subscribe((res) => {
        if (res.message == 'Dato registrado correctamente') {
          alert('Registrado')
        } else {
          alert('No hay registros')
        }
      })
    } else {
      alert('Los campos estan vacios')
    }
  }

  UpdateAmb(visible: boolean) {
    if (this.DatosAmbulancias.Identificacion != '' && this.DatosAmbulancias.TipoHerida != '' && this.DatosAmbulancias.CantidadH > 0) {
      this.DatosAmbulancias['tipo'] = 'actualizarAmbulancias';
      this.infoGraficas.ActuaTras(this.DatosAmbulancias).subscribe((res) => {
        if (res.message == 'Datos modificados correctamente') {

        } else {
          alert('No esta actualizado correctamente')
        }
      })
    }
    else {
      alert('No hay datos para actualizar')
    }
  }

  DelAmb(TipoHerida: string) {
    let form = {
      TipoHerida: TipoHerida,
      tipo: 'borrarAmbulancias'
    }
    this.infoGraficas.EliminarAmb(form).subscribe((res) => {
      if (res.message == 'Registro eliminado') {
        alert('Registro eliminado');
      }
    })
  }

  EditarAmb(Identificacion: string, TipoHerida: string, CantidadH: number) {
    this.DatosAmbulancias.Identificacion = Identificacion;
    this.DatosAmbulancias.TipoHerida = TipoHerida;
    this.DatosAmbulancias.CantidadH = CantidadH;
    this.AddAmbulancias = false;
    this.ActualizarAmb = true;
  }

  //------------------------------------------Final Ambulancias------------------------------------------//

  ngOnInit() {
    let form = {
      tipo: "infoGraficas"
    }
    this.infoGraficas.infoGraficas(form).subscribe((res: any) => {
      this.multi = res.infoGraficas;
      console.log(this.multi)
    })

    form = {
      tipo: "ListadoTraslados"
    }
    this.infoGraficas.ListadoTras(form).subscribe((res: any) => {
      this.RegistroD = res.lista;
    });
    form = {
      tipo: "ListadoAmbulancias"
    }
    this.infoGraficas.ListadoAmb(form).subscribe((res: any) => {
      this.RegistroA = res.lista;
    });
  }

  //options
  legend: boolean = true;
  showLabels: boolean = true;
  animations: boolean = true;
  xAxis: boolean = true;
  yAxis: boolean = true;
  showYAxisLabel: boolean = true;
  showXAxisLabel: boolean = true;
  xAxisLabel: string = '';
  yAxisLabel: string = '';
  timeline: boolean = true;

  colorScheme = {
    domain: ['#5AA454']
  };

  onSelect(event: any) {
    console.log(event);
  }
}

