import { Injectable } from '@angular/core';
import { AngularFireDatabase } from '@angular/fire/compat/database';


@Injectable()
export class CalendarService {
  angularfire: AngularFireDatabase;

  constructor(af: AngularFireDatabase) {
    this.angularfire = af;
  }

  getAll() {
    return this.angularfire.list('/weekCalendar').valueChanges() as any;
  }
}