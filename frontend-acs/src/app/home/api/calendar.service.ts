import { Injectable } from '@angular/core';
import { CalendarData } from '../types/calendar-data';
import { AngularFireDatabase } from '@angular/fire/compat/database';


@Injectable()
export class CalendarService {
  angularfire: AngularFireDatabase;
  items: CalendarData[] = [];

  constructor(af: AngularFireDatabase) {
    this.angularfire = af;
  }

  getAll() {
    // Buscando todos os itens no no "/task"
    const result = this.angularfire.list('/weekCalendar');
    console.log(result);
    return result;
  }
}