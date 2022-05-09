import { Injectable } from '@angular/core';
import { acsDataService } from './api/acsData.service';
import { CalendarService } from './api/calendar.service';
import { SuggestionsService } from './api/suggestions.service';
import { Pending } from './types/pending';

@Injectable()
export class apiFacade {
  public constructor(
    private readonly calendarAPI: CalendarService,
    private readonly acsDataAPI: acsDataService,
    private readonly suggestionsAPI: SuggestionsService
  ) {}

  public getWeekCalendarPlanning() {
    return this.calendarAPI.getAll();
  }

  public getAcsDataBy(login: string) {
    return this.acsDataAPI.getDataBy(login);
  }

  public getSuggestions() {
    return this.suggestionsAPI.getAll();
  }

  public confirm(patient: Pending) {
    const newPatient = {
      username: patient.name,
      service: patient.chosen_specialty,
      sus: patient.cadastro_sus,
      queuePosition: 0,
      date: patient.date_time,
    };
    this.suggestionsAPI.confirm(newPatient, patient.chat_id);
  }

  public reject(patient: Pending) {
    this.suggestionsAPI.reject(patient);
  }
}
