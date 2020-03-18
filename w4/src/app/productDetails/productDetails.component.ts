import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import {ProductService} from '../product.service';
import {Product} from '../product';
@Component({
  selector: 'app-productDetails',
  templateUrl: './productDetails.component.html',
  styleUrls: ['./productDetails.component.css']
})
export class ProductDetailsComponent implements OnInit {
  product: Product;
  constructor(
    private location: Location,
    private route: ActivatedRoute,
    private productService: ProductService
    ){}

  ngOnInit(): void {
    this.getProduct();
  }

  getProduct(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.productService.getProduct(id)
      .subscribe(product => this.product = product);
  }
  goBack(): void {
    this.location.back();
  }

}