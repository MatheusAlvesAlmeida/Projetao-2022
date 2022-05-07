import { Injectable } from '@angular/core';
import { acsDataService } from './api/acsData.service';
import { CalendarService } from './api/calendar.service';

@Injectable()
export class apiFacade {
  
  public constructor(
    private readonly calendarAPI: CalendarService,
    private readonly acsDataAPI: acsDataService,
  ) {}

  public getWeekCalendarPlanning(){
    return this.calendarAPI.getAll();
  }

  public getAcsDataBy(login: string){
    return this.acsDataAPI.getDataBy(login);
  }
}