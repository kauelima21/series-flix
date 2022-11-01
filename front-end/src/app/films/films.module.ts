import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { FilmsRoutingModule } from './films-routing.module';
import { FilmsComponent } from './films/films.component';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    FilmsComponent
  ],
  imports: [
    BrowserModule,
    FilmsRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [FilmsComponent]
})

export class FilmsModule { }
