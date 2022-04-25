import { Component, OnInit } from '@angular/core';
import { SuggestionDates } from '../../types/suggestion-dates';


const ELEMENT_DATA: SuggestionDates[] = [
  {
    id: 1,
    name: 'Gabriel',
    service: 'Médico',
    sus: '123456789',
    queuePosition: 1,
    appointment: '09:00 - 04/05/2022',
  },
  {
    id: 2,
    name: 'Pietro',
    service: 'Dentista',
    sus: '123456789',
    queuePosition: 2,
    appointment: '09:30 - 04/05/2022',
  },
];

@Component({
  selector: 'app-home-options',
  templateUrl: './home-options.component.html',
  styleUrls: ['./home-options.component.css'],
})
export class HomeOptionsComponent implements OnInit {
  constructor() { }

  ngOnInit(): void { }

  dataSource = [...ELEMENT_DATA];

  confirmAllSuggestions() { }

  cancelAllSuggestions() { }
}
