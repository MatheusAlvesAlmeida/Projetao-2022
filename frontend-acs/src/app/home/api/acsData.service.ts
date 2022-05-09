import { Injectable } from '@angular/core';
import { AngularFireDatabase } from '@angular/fire/compat/database';


@Injectable()
export class acsDataService {
  angularfire: AngularFireDatabase;

  constructor(af: AngularFireDatabase) {
    this.angularfire = af;
  }

  getDataBy(login: string) {
    return this.angularfire.list('/acsData/' + login).valueChanges() as any;
  }
}