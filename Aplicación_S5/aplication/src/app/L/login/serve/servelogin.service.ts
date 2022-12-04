import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { RouterState } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService{
private URL: string = 'http://localhost:8000';
  constructor(private servHTTP : HttpClient){
  }
  public login(form:any):Observable<any>{
    return this.servHTTP .post(`${this.URL}/AppAPI/usuarios/`,form);
  }
}
