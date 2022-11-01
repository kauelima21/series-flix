import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { SeriesRoutingModule } from './series-routing.module';
import { SeriesComponent } from './series/series.component';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    SeriesComponent
  ],
  imports: [
    BrowserModule,
    SeriesRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [SeriesComponent]
})

export class SeriesModule { }
