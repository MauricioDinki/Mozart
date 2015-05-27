(function() {
  'use strict';

  function validateDatesService() {
    /* jshint validthis:true */
    this.full_current_date = new Date();
    this.current_year = parseInt(this.full_current_date.getYear()) + 1900;
    this.current_month = parseInt(this.full_current_date.getMonth()) + 1;
    this.current_day = parseInt(this.full_current_date.getDate());
    this.current_date = new Date(this.current_year, this.current_month - 1, this.current_day);
    this.validDate = function(day, monthName, year, age){
      var month;
      if(isNaN(monthName)){
        month = this.getMonthNumber(monthName);
      }
      else{
        month = monthName;
      }
      var newDate = new Date(year, month, '0');
      if((day-0) <= parseInt(newDate.getDate()-0)){
        return this.validAge(day, month, year, age);
      }
      else{
        return 'La fecha que introduciste no es valida.';
      }
    };
    this.validAge = function(day, month, year, age){
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
      if(datesDifference >= age){
        return 'Ok';
      }
      else{
        return 'Lo sentimos, debes ser mayor de edad';
      }
    };
    this.futureDate = function(date) {
      var date_elements = date.split('-');
      var new_date = new Date(date_elements[0], date_elements[1] - 1, date_elements[2]);
      return new_date.getTime() - this.current_date.getTime() >= 86400000;
    };
    this.validDuration = function(start_time, finish_time) {
      var start_time_elements = String(start_time.$modelValue).split(':');
      var finish_time_elements = String(finish_time.$modelValue).split(':');

      var absolute_start_time = (parseInt(start_time_elements[0]) * 60) + parseInt(start_time_elements[1]);
      var absolute_finish_time = (parseInt(finish_time_elements[0]) * 60) + parseInt(finish_time_elements[1]);

      return absolute_finish_time >= absolute_start_time + 30;
    };
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
  }

  angular.module('mozArtApp')
    .service('validateDates', validateDatesService);
})();