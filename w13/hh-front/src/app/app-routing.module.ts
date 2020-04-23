import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { VacanciesComponent } from './vacancies/vacancies.component';
import { MainComponent } from './main/main.component';
import { AppComponent } from './app.component';


const routes: Routes = [
  {path: 'companies', component: MainComponent},
  {path:'companies/:id/vacancies', component:VacanciesComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
