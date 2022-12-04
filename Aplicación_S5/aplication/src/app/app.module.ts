import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { NgChartsModule } from 'ng2-charts';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DatosComponent } from './D/datos/datos.component';
import { InicioComponent } from './I/inicio/inicio.component';
import { BlogComponent } from './B/blog/blog.component';
import { LoginComponent } from './L/login/login.component';
import { PerfilComponent } from './P/perfil/perfil.component';


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
    NgChartsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
