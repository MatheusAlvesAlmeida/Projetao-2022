import { Component, OnInit } from '@angular/core';
import { CalendarData } from '../../types/calendar-data';
import { CalendarService } from '../../api/calendar.service';

const ELEMENT_DATA: CalendarData[] = [];


@Component({
  selector: 'app-week-calendar',
  templateUrl: './week-calendar.component.html',
  styleUrls: ['./week-calendar.component.css']
})
export class WeekCalendarComponent implements OnInit {

  dataSource = [...ELEMENT_DATA];

  constructor(private calendarService: CalendarService) {
    
  }

  ngOnInit(): void {
    const result = this.calendarService.getAll();
    this.dataSource = [];
    result.subscribe((data: any[]) => {
      data.forEach((element) => this.dataSource.push(element));
    });
  }
}
