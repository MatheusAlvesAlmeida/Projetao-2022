import { Component, OnInit } from '@angular/core';
import { ViewChild } from '@angular/core';
import { MatTable } from '@angular/material/table';
import { MatDialog } from '@angular/material/dialog';

export interface suggestionDates {
  name: string;
  id: number;
  service: string;
  timestamp: string;
}

const ELEMENT_DATA: suggestionDates[] = [
  { id: 1, name: 'Gabriel', service: "Urologista", timestamp: '09:00 - 05/05/2022' },
  { id: 2, name: 'Pietro', service: "Dentista", timestamp: '09:00 - 04/05/2022' },
  { id: 3, name: 'João Plácido', service: "Dentista", timestamp: '10:00 - 06/05/2022' },
  { id: 4, name: 'Luisa', service: "Dentista", timestamp: '10:00 - 08/05/2022' },
];

@Component({
  selector: 'app-home-options',
  templateUrl: './home-options.component.html',
  styleUrls: ['./home-options.component.css']
})

export class HomeOptionsComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }


  displayedColumns: string[] = ['name', 'service', 'timestamp', 'actions'];
  columnsToDisplay: string[] = this.displayedColumns.slice();
  dataSource = [...ELEMENT_DATA];

  confirmAllSuggestions() {

  }

  cancelAllSuggestions() {
  }

}
