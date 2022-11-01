import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { GamesRoutingModule } from './games-routing.module';
import { GamesComponent } from './games/games.component';
import { HttpClientModule } from '@angular/common/http';


@NgModule({
  declarations: [
    GamesComponent
  ],
  imports: [
    CommonModule,
    GamesRoutingModule,
    HttpClientModule
  ]
})

export class GamesModule {}
