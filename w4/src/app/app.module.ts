import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CategoriesComponent } from './category/category.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ReactiveFormsModule } from '@angular/forms';
import { ProductDetailsComponent } from './productDetails/productDetails.component';
import { ProductsComponent } from './products/products.component';
import { SliderComponent } from './slider/slider.component';


@NgModule({
   declarations: [
      AppComponent,
      CategoriesComponent,
      ProductsComponent,
      ProductDetailsComponent,
      SliderComponent
   ],
   imports: [
      BrowserModule,
      AppRoutingModule,
      BrowserAnimationsModule,
      ReactiveFormsModule,
      
   ],
   providers: [],
   bootstrap: [
      AppComponent
   ]
})
export class AppModule { }