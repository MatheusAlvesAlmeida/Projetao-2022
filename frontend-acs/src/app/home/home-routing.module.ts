import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomePageComponent } from './pages/home-page.component';

const routes: Routes = [
  {
    path: 'home',
    component: HomePageComponent,
    data: {
      id: 'home',
      title: 'Home',
      icon: 'home',
    }
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HomeRoutingModule { }