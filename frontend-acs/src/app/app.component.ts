import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: []
})
export class AppComponent implements OnInit {
  title = 'Gestão ACS';

  constructor(private router: Router) { }

  ngOnInit () { 
    this.router.navigate(['/home'])
  }
}