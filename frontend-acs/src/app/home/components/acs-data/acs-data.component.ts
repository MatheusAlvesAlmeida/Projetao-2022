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
    cpf: '',
    desc: '',
    image: '',
    name: 0,
  };

  constructor(
    private changeDetectorRefs: ChangeDetectorRef,
    private readonly acsDataFacade: apiFacade
  ) {}

  ngOnInit(): void {
    const result = this.acsDataFacade.getAcsDataBy('acs1');
    console.log(result);
    result.subscribe((data: acsData) => {
      console.log(data);
      this.dataSource = data;
      console.log(this.dataSource);
    });
    console.log(this.dataSource);
    this.changeDetectorRefs.detectChanges();
  }
}
