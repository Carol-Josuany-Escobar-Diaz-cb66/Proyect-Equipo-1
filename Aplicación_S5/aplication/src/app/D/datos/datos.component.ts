import { Component, OnInit} from '@angular/core';
import { Chart, ChartConfiguration} from 'chart.js';
import { NgxChartsModule } from "@swimlane/ngx-charts";
import { DatosService } from '../datos-service.service';

@Component({
  selector: 'app-datos',
  templateUrl: './datos.component.html',
  styleUrls: ['./datos.component.css']
})
export class DatosComponent {
multi: any[] = [];
view:[number,number]=[700,300];

  constructor(private infoGraficas:DatosService){
  }

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

