import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './films.component.html',
  styleUrls: ['./films.component.scss']
})

export class FilmsComponent implements OnInit {

  constructor(private http: HttpClient) { }

  film:any;

  ngOnInit(){
    this.http.get('http://localhost:4566/restapis/i44zkn06rn/local/_user_request_/games').subscribe(
      data => {
        this.film = data;
      }
    )
  }
}