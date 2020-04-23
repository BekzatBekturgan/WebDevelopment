import { Component, OnInit } from '@angular/core';
import { CompanyService } from '../services/company.service';
import { Company } from '../data/companies';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  companies: Company[] = [];
  constructor(private companyService:CompanyService) { }

  ngOnInit(): void {
    this.getCompanyList();
  }

  getCompanyList():void{
    this.companyService.getCompanyList().subscribe(companies=> this.companies = companies);
  }

}
