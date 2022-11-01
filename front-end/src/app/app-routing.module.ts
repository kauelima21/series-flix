import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { GamesComponent } from './games/games/games.component';
import { SeriesComponent } from './series/series/series.component';
import { FilmsComponent } from './films/films/films.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';

const routes: Routes = [
  { path: 'games', component: GamesComponent },
  { path: 'series', component: SeriesComponent },
  { path: 'films', component: FilmsComponent },
  { path: '404', component: PageNotFoundComponent},
  { path: '', redirectTo: '/series', pathMatch: 'full' },
  { path: '**', redirectTo: '/404' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
export const routingComponents = [GamesComponent, SeriesComponent, FilmsComponent]