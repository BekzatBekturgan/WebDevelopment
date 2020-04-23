import { Component, OnInit } from '@angular/core';
import { VacanciesService  } from '../services/vacancies.service';
import { CompanyService } from '../services/company.service';
import { ActivatedRoute } from '@angular/router';
import { Vacancy } from '../data/vacancies';
@Component({
  selector: 'app-vacancies',
  templateUrl: './vacancies.component.html',
  styleUrls: ['./vacancies.component.css']
})
export class VacanciesComponent implements OnInit {
  vacancies: Vacancy[] = [];

  constructor(private vacanciesService:VacanciesService, private route: ActivatedRoute,
    private companyService:CompanyService) { }

  ngOnInit(): void {
    this.getVacanciesByCompany();
  }
  getVacanciesByCompany():void{
    const id =+this.route.snapshot.paramMap.get('id');
    this.companyService.getVacanciesByCompany(id).subscribe(res=>this.vacancies = res);
  }
}
