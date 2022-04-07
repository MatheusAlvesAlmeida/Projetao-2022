import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AcsDataComponent } from './components/acs-data/acs-data.component';
import { HomePageComponent } from './pages/home-page.component';
import { HomeRoutingModule } from './home-routing.module';

@NgModule({
  declarations: [
    AcsDataComponent,
    HomePageComponent
  ],
  imports: [
    CommonModule,
    HomeRoutingModule
  ]
})
export class HomeModule { }
