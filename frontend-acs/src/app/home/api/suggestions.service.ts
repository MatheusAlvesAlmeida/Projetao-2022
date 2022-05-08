import { Injectable } from '@angular/core';
import { AngularFireDatabase } from '@angular/fire/compat/database';

@Injectable()
export class SuggestionsService {
  angularfire: AngularFireDatabase;

  constructor(af: AngularFireDatabase) {
    this.angularfire = af;
  }

  getAll() {
    return this.angularfire.list('/pendentes').valueChanges() as any;
  }

  confirm(chat_id: number) {
    //this.angularfire.createPushId('/weekCalendar/' + chat_id)
  }

  reject() {}
}
