import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProductService} from '../product.service'
import {Product} from '../product'
import { Location } from '@angular/common';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {
  products: Product[];
  constructor(
    private location: Location,
    private productService: ProductService,
    private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getProducts();
  }
  getProducts(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.productService.getProductofC(id)
      .subscribe(products => this.products = products);
  }
  }