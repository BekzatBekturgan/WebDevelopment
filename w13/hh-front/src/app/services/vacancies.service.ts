import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Vacancy} from '../data/vacancies'
import { HttpClientModule, HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class VacanciesService {
  BASE_URL = 'http://localhost:8000'
  constructor(private http:HttpClient) { }

  getVacanciesByCompany(companyId:number):Observable<Vacancy[]>{
    return this.http.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${companyId}/vacancies/`);
  }

  // getVacanciesByCompany(companyId:number): Observable<any>{
   //return of(VACANCIES.filter(vacancy=>vacancy.company === companyId));
  // }
}
