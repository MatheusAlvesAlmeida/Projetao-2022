import { Injectable } from '@angular/core';
import { Pending } from '../home/types/pending';
import { ConfirmedPatients } from '../home/types/confirmed-patients';
import {
  AngularFireDatabase,
  AngularFireList,
  AngularFireObject,
} from '@angular/fire/compat/database';
@Injectable({
  providedIn: 'root',
})


export class CrudService {
  patientsRef: AngularFireList<any> | undefined;
  patientRef: AngularFireObject<any> | undefined;

  constructor(private db: AngularFireDatabase) {}

  // Create Confirmed Patients List
  addConfirmedQueue(confirmedPatients: ConfirmedPatients) {
    this.patientsRef?.push({
      confirmedPatients
    });
  }

  // Fetch Pending Patients List
  getPendingList() {
    this.patientsRef = this.db.list('pendentes');
    return this.patientsRef;
  }

  // Delete Student Object
  deletePending(cadastro_sus: string) {
    this.patientRef = this.db.object('pendentes/' + cadastro_sus);
    this.patientRef.remove();
  }
}
