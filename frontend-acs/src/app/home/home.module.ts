import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeRoutingModule } from './home-routing.module';
import { MatCardModule } from '@angular/material/card';
import { MatTableModule } from '@angular/material/table';
import { MatTabsModule } from '@angular/material/tabs';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';


import { AcsDataComponent } from './components/acs-data/acs-data.component';
import { HomePageComponent } from './pages/home-page.component';
import { HomeOptionsComponent } from './components/home-options/home-options.component';

@NgModule({
  declarations: [
    AcsDataComponent,
    HomePageComponent,
    HomeOptionsComponent
  ],
  imports: [
    CommonModule,
    HomeRoutingModule,
    MatCardModule,
    MatTableModule,
    MatTabsModule,
    MatIconModule,
    MatButtonModule
  ]
})
export class HomeModule { }
