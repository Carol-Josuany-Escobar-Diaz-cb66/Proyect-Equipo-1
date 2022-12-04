import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RegiPerfilService {

  private URL: string = 'http://localhost:8000';
  constructor(private servHTTP : HttpClient){
  }
  public signup(sign:any){
    return "Por fin se logró gracias a Dios";
  }
}
