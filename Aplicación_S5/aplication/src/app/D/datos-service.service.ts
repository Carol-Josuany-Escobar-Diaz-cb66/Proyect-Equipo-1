import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { RouterState } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DatosService {
  HTTP = 'http://localhost:8000'
  constructor(private rutas:HttpClient) { }

  obtenerDatos(form:any):Observable<any> {
    return this.rutas.post("http://localhost:8000",form);
  }
}
