import { Component, OnInit } from '@angular/core';
import { CalendarData } from '../../types/calendar-data';

const ELEMENT_DATA: CalendarData[] = [
  {
    username: 'Matheus',
    service: 'Médico clínico geral',
    sus: '123465',
    queuePosition: 1,
    date: new Date("2000-12-17T03:24:00"),
  },
  {
    username: 'Matheus',
    service: 'Dentista',
    sus: '123465',
    queuePosition: 1,
    date: '24/04/2022',
  },
  {
    username: 'Pietro',
    service: 'Médico clínico geral',
    sus: '123465',
    queuePosition: 1,
    date: '24/04/2022',
  }
];

@Component({
  selector: 'app-week-calendar',
  templateUrl: './week-calendar.component.html',
  styleUrls: ['./week-calendar.component.css']
})
export class WeekCalendarComponent implements OnInit {

  dataSource = [...ELEMENT_DATA];

  constructor() { }

  ngOnInit(): void {
  }



}
