import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { NgxChartsModule } from "@swimlane/ngx-charts";

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DatosComponent } from './D/datos/datos.component';
import { InicioComponent } from './I/inicio/inicio.component';
import { BlogComponent } from './B/blog/blog.component';
import { LoginComponent } from './L/login/login.component';
import { PerfilComponent } from './P/perfil/perfil.component';
import { FuncionComponent } from './D/funcion/funcion.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations'



@NgModule({
  declarations: [
    AppComponent,
    DatosComponent,
    InicioComponent,
    BlogComponent,
    LoginComponent,
    PerfilComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    NgxChartsModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
