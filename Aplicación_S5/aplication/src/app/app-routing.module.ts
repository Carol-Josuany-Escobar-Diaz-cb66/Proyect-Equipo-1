import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BlogComponent } from './B/blog/blog.component';
import { DatosComponent } from './D/datos/datos.component';
import { FuncionComponent } from './D/funcion/funcion.component';
import { InicioComponent } from './I/inicio/inicio.component';
import { LoginComponent } from './L/login/login.component';
import { PerfilComponent } from './P/perfil/perfil.component';


const routes: Routes = [
 {
  path:'Inicio',
  component: InicioComponent
 },
 {
  path:'Login',
  component: LoginComponent
 },
 {
  path:'Datos',
  component: DatosComponent
 },
 {
  path:'Funcion',
  component: FuncionComponent
 },
 {
  path:'Blog',
  component: BlogComponent
 },
 {
  path:'Perfil',
  component: PerfilComponent
 }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
