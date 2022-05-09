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
      this.dataSource = data;
      let auxDate;
      this.dataSource?.forEach((patient) => {
        auxDate = new Date(patient.date_time);
        patient.date_time =
          String(auxDate.getDay() + 1).padStart(2, '0') +
          '/' +
          String(auxDate.getMonth()).padStart(2, '0') +
          '/' +
          auxDate.getFullYear() +
          ' - ' +
          auxDate.getHours() +
          ':' +
          auxDate.getMinutes();
      });
    });
  }

  confirm(patient: Pending) {
    this.suggestionsFacade.confirm(patient);
  }

  reject(patient: Pending) {
    this.suggestionsFacade.reject(patient);
  }
}
