import { Injectable } from '@angular/core';
import { CalendarData } from '../types/calendar-data';
import { AngularFireDatabase } from '@angular/fire/compat/database';
import { Observable } from 'rxjs';


@Injectable()
export class CalendarService {
  angularfire: AngularFireDatabase;

  constructor(af: AngularFireDatabase) {
    this.angularfire = af;
  }

  getAll() {
    const result = this.angularfire.list('/weekCalendar').valueChanges() as any;
    return result;
  }
}