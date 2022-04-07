import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AcsDataComponent } from './acs-data.component';

describe('AcsDataComponent', () => {
  let component: AcsDataComponent;
  let fixture: ComponentFixture<AcsDataComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AcsDataComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AcsDataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
