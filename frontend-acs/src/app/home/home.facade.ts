import { Injectable } from '@angular/core';
import { CalendarService } from './api/calendar.service';

@Injectable()
export class apiFacade {
  
  public constructor(
    private readonly calendarApi: CalendarService
  ) {}

  public getWeekCalendarPlanning(){
    return this.calendarApi.getAll();
  }
}