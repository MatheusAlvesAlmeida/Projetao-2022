import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeRoutingModule } from './home-routing.module';
import { MatCardModule } from '@angular/material/card';
import { MatTableModule } from '@angular/material/table';
import { MatTabsModule } from '@angular/material/tabs';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { CalendarModule, DateAdapter } from 'angular-calendar';
import { adapterFactory } from 'angular-calendar/date-adapters/date-fns';
import { FormsModule } from '@angular/forms';
import { FlatpickrModule } from 'angularx-flatpickr';
import { NgbModalModule } from '@ng-bootstrap/ng-bootstrap';
import { MatExpansionModule } from '@angular/material/expansion';

import { AcsDataComponent } from './components/acs-data/acs-data.component';
import { HomePageComponent } from './pages/home-page.component';
import { HomeOptionsComponent } from './components/home-options/home-options.component';
import { CalendarComponent } from './components/calendar/calendar.component';
import { WeekCalendarComponent } from './components/week-calendar/week-calendar.component';

@NgModule({
  declarations: [
    AcsDataComponent,
    HomePageComponent,
    HomeOptionsComponent,
    CalendarComponent,
    WeekCalendarComponent
  ],
  imports: [
    CommonModule,
    HomeRoutingModule,
    MatCardModule,
    MatTableModule,
    MatTabsModule,
    MatIconModule,
    FormsModule,
    NgbModalModule,
    FlatpickrModule.forRoot(),
    MatButtonModule,
    MatExpansionModule,
    CalendarModule.forRoot({
      provide: DateAdapter,
      useFactory: adapterFactory,
    }),
  ]
})
export class HomeModule { }
