import { Injectable } from '@angular/core';
import { AngularFireDatabase } from '@angular/fire/compat/database';
import { CalendarData } from '../types/calendar-data';
import { Pending } from '../types/pending';

@Injectable()
export class SuggestionsService {
  angularfire: AngularFireDatabase;

  constructor(af: AngularFireDatabase) {
    this.angularfire = af;
  }

  getAll() {
    return this.angularfire.list('/pendentes').valueChanges() as any;
  }

  confirm(patient: CalendarData, chat_id: number) {
    this.angularfire.list('/weekCalendar').push(patient);
    this.angularfire.list('/pendentes/' + chat_id).remove();
  }

  reject(patient: Pending) {
    this.angularfire.list('/pendentes/' + patient.chat_id).remove();
  }
}
