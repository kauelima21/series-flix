import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';

import { GamesModule } from './games/games.module';
import { SeriesModule } from './series/series.module';
import { FilmsModule } from './films/films.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    GamesModule,
    SeriesModule,
    FilmsModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }