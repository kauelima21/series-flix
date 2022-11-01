import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-root',
  templateUrl: './games.component.html',
  styleUrls: ['./games.component.scss']
})

export class GamesComponent implements OnInit {

  constructor(private http: HttpClient) { }

  game:any;

  ngOnInit(){
    this.http.get('http://localhost:4566/restapis/i44zkn06rn/local/_user_request_/games').subscribe(
      data => {
        this.game = data;
      }
    )
  }
}
