import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { PRODUCTS } from './products';
import { Product } from './product';
import { Category } from './category';
import {CATEGORY} from './categories';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor() { }

  getProducts(): Observable<Product[]> {
    return of(PRODUCTS);
  }
  getProduct(id: number): Observable<Product> {
    return of(PRODUCTS.find(product => product.id === id));
  }
  getCategory(): Observable<Category[]> {
    return of(CATEGORY);
  }
  getCategories(id: number): Observable<Category> {
    return of(CATEGORY.find(category => category.id === id));
  }
  getProductofC(categoryId: number): Observable<Product[]> {
    return of(PRODUCTS.filter(product => product.categoryId === categoryId));
  }
}