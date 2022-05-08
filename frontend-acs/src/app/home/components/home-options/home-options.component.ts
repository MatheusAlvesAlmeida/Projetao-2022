import { Component, OnInit } from '@angular/core';
import { apiFacade } from '../../home.facade';
import { Pending } from '../../types/pending';

@Component({
  selector: 'app-home-options',
  templateUrl: './home-options.component.html',
  styleUrls: ['./home-options.component.css'],
})
export class HomeOptionsComponent implements OnInit {
  dataSource: Pending[] = [];

  constructor(private readonly suggestionsFacade: apiFacade) {}

  ngOnInit(): void {
    const result = this.suggestionsFacade.getSuggestions();
    result.subscribe((data: Pending[]) => {
      console.log(data);
      this.dataSource = data;
      console.log(this.dataSource);
    });
    console.log(this.dataSource);
  }
}
