import { Component, OnInit } from '@angular/core';
import { apiFacade } from '../../home.facade';
import { acsData } from '../../types/acs-data';
import { ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-acs-data',
  templateUrl: './acs-data.component.html',
  styleUrls: ['./acs-data.component.css'],
})
export class AcsDataComponent implements OnInit {
  dataSource: acsData = {
    cpf: '68795443223',
    desc: 'Trabalha de segunda à sexta, das 8:00 às 17:00',
    image:
      'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fclaudia.abril.com.br%2Fwp-content%2Fuploads%2F2020%2F04%2Fianara-araujo-fernandes-enfermeira-em-dublin-e1585762335607.jpg&f=1&nofb=1',
    name: 'Maria Aparecida',
  };

  constructor(
    private changeDetectorRefs: ChangeDetectorRef,
    private readonly acsDataFacade: apiFacade
  ) {}

  ngOnInit(): void {
    // const result = this.acsDataFacade.getAcsDataBy('acs1');
    // result.subscribe((data: acsData) => {
    //   this.dataSource = data;
    // });
    // console.log('acs', this.dataSource);
    // this.changeDetectorRefs.detectChanges();
  }
}
