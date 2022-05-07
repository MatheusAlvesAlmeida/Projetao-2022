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
    // Buscando todos os itens no no "/task"
    const result = this.angularfire.list('/weekCalendar').valueChanges() as any;
    console.log(result);
    return result;
  }
}