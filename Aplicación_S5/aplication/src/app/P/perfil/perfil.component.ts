import { Component, OnInit } from '@angular/core';
import { RegiPerfilService } from '../regi-perfil.service';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrls: ['./perfil.component.css']
})
export class PerfilComponent implements OnInit {

  sign:any = {
    nombre: '',
    apellido:'',
    fechanacimiento: '',
    direccion:'',
    telefono: '',
    usuario: '',
    contrasena:''
  }

  constructor(private acceso: RegiPerfilService) { }

  ngOnInit(): void {
    
  }

  signup(){
    if(this.sign.usuario !=""){
      console.log(this.acceso.signup(this.sign));
      localStorage.setItem('sign',JSON.stringify(this.sign));
    }
  }

}
