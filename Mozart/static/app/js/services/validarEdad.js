'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.service:validateAge
 * @description
 * # validateAge
 * Service of the mozArtApp
 */

app.service('validateAge', function(){
  this.current_date = new Date();
  this.current_year = parseInt(this.current_date.getYear()) + 1900;
  this.current_month = parseInt(this.current_date.getMonth()) + 1;
  this.current_day = parseInt(this.current_date.getDate());
  this.validDate = function(day, monthName, year){
    var month;
    if(isNaN(monthName)){
      month = this.getMonthNumber(monthName);
    }
    else{
      month = monthName;
    }
    var newDate = new Date(year, month, '0');
    if(!((day-0) > (newDate.getDate()-0))){
      return this.validAge(day, month, year);
    }
    else{
      return 'La fecha que introduciste no es valida.';
    }
  };
  this.validAge = function(day, month, year){
    var datesDifference = this.current_year - year;
    if(this.current_month < month){
      datesDifference--;
    }
    if((month === this.current_month) && (this.current_day < day)){
      datesDifference--;
    }
    if(datesDifference > 1900){
      datesDifference -= 1900;
    }
    if(datesDifference >= 18){
      return 'Ok';
    }
    else{
      return 'Lo sentimos, debes ser mayor de edad';
    }
  }
  this.getMonthNumber = function(monthName){
    if(monthName === 'Enero'){
      return 1;
    }
    else if(monthName === 'Febrero'){
      return 2;
    }
    else if(monthName === 'Marzo'){
      return 3;
    }
    else if(monthName === 'Abril'){
      return 4;
    }
    else if(monthName === 'Mayo'){
      return 5;
    }
    else if(monthName === 'Junio'){
      return 6;
    }
    else if(monthName === 'Julio'){
      return 7;
    }
    else if(monthName === 'Agosto'){
      return 8;
    }
    else if(monthName === 'Septiembre'){
      return 9;
    }
    else if(monthName === 'Octubre'){
      return 10;
    }
    else if(monthName === 'Noviembre'){
      return 11;
    }
    else if(monthName === 'Diciembre'){
      return 1;
    }
    else{
      return 0;
    }
  };
});

