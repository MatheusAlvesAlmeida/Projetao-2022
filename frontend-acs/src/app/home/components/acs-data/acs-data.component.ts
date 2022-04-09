import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-acs-data',
  templateUrl: './acs-data.component.html',
  styleUrls: ['./acs-data.component.css']
})
export class AcsDataComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  acsName = 'Xuribas'
  acsData = `Aqui ficam informações gerais: horário e dias de atendimento, etc etc etc`;
  acsCode = '123456789'

}
