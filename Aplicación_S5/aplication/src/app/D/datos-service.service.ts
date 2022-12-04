import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DatosService {
  HTTP = 'http://localhost:8000'
  constructor(private info:HttpClient) { }

  infoGraficas(form:any):Observable<any> {
    return this.info.post("http://localhost:8000/AppAPI/grafica/",form);
  }
  AnadirTras(form:any):Observable<any> {
    return this.info.post("http://localhost:8000/AppAPI/traslados/",form);
  }
  AnadirAmb(form:any):Observable<any> {
    return this.info.post("http://localhost:8000/AppAPI/ambulance/",form);
  }
  ListadoTras(form:any):Observable<any> {
    return this.info.post("http://localhost:8000/AppAPI/traslados/",form);
  }
  ListadoAmb(form:any):Observable<any> {
    return this.info.post("http://localhost:8000/AppAPI/ambulance/",form);
  }
  ActuaTras(form:any):Observable<any> {
    return this.info.post("http://localhost:8000/AppAPI/traslados/",form);
  }
  ActuaAmb(form:any):Observable<any> {
    return this.info.post("http://localhost:8000/AppAPI/ambulance/",form);
  }
  EliminarTras(form:any):Observable<any> {
    return this.info.post("http://localhost:8000/AppAPI/traslados/",form);
  }
  EliminarAmb(form:any):Observable<any> {
    return this.info.post("http://localhost:8000/AppAPI/ambulance/",form);
  }
}
