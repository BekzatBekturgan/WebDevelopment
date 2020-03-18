import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ProductsComponent } from './products/products.component';
import { ProductDetailsComponent } from './productdetails/productdetails.component';
import {CategoriesComponent} from './category/category.component'

const routes: Routes = [
  {path: '', redirectTo: '/categories', pathMatch: 'full'},
  {path: 'categories', component:CategoriesComponent},
  {path: 'categories/:id', component: ProductsComponent },
  {path: 'products/:id', component: ProductDetailsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }