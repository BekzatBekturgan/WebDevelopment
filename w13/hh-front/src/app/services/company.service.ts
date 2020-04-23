import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { LoginResponse, Company } from '../data/companies';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { Vacancy } from '../data/vacancies';


@Injectable({
  providedIn: 'root'
})
export class CompanyService {


  BASE_URL = 'http://localhost:8000'
  constructor(private http: HttpClient) { }
 
  getCompanyList(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.BASE_URL}/api/companies/`);
  }
  // getCompanyList(): Observable<Company[]>{
  //   return this.http.get<Company[]>(`${this.BASE_URL}/api/companies/`);
  //   //return of(COMPANIES); //конвертация в тип Observable
  // }
  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.BASE_URL}/api/login/`, {
      username,
      password
    })
  }
  getVacanciesByCompany(id):Observable<Vacancy[]>{
    return this.http.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${id}/vacancies`)
  }
}
