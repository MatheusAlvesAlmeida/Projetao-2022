import { Component, OnInit } from '@angular/core';
import { CalendarData } from '../../types/calendar-data';
import { apiFacade } from '../../home.facade';

const ELEMENT_DATA: CalendarData[] = [];

@Component({
  selector: 'app-week-calendar',
  templateUrl: './week-calendar.component.html',
  styleUrls: ['./week-calendar.component.css']
})
export class WeekCalendarComponent implements OnInit {

  dataSource = [...ELEMENT_DATA];

  constructor(private readonly calendarFacade: apiFacade) {
    const result = this.calendarFacade.getWeekCalendarPlanning();
    this.dataSource = [];
    result.subscribe((data: any[]) => {
      data.forEach((element) => this.dataSource.push(element));
    });
  }

  ngOnInit(): void { }
}
