import { Component, OnInit } from '@angular/core';
import { LoginService } from './serve/servelogin.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  user = {
    NombreUsuario:'',
    Usuario: '',
    Contrasena:''
  };

  constructor(private acceso: LoginService) { }

  ngOnInit(): void {
    let formulario={
      tipo : "login"
    }
    this.acceso.login(formulario).subscribe((res)=>{
        if(res!=null){

        }
    });
  }

  login(){
    if(this.user.NombreUsuario !=""){
      console.log(this.acceso.login(this.user));
      localStorage.setItem('user',JSON.stringify(this.user));
    }
  }

}
