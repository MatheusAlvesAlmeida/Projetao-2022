import { Component, OnInit } from '@angular/core';
import { Pending } from '../../types/pending';

// TODO: refact with Pending atrributes
const ELEMENT_DATA: Pending[] = [
  {
    id: 1,
    date: new Date('04/05/2022'),
    address_number: 'Endereço',
    sus: '5165165165',
    cep: '56800000',
    chat_id: 1,
    service: 'Médico geral',
    name: 'Xuribas, o cara',
    phone_number: '8799966666',
  },
  {
    id: 2,
    date: new Date('05/05/2022'),
    address_number: 'Endereço',
    sus: '5165165165',
    cep: '56800000',
    chat_id: 1,
    service: 'Médico geral',
    name: 'Xuribas, o quase cara',
    phone_number: '22222222',
  },
];

@Component({
  selector: 'app-home-options',
  templateUrl: './home-options.component.html',
  styleUrls: ['./home-options.component.css'],
})
export class HomeOptionsComponent implements OnInit {
  constructor() { }

  ngOnInit(): void { }

  dataSource = [...ELEMENT_DATA];

  confirmAllSuggestions() { }

  cancelAllSuggestions() { }
}
