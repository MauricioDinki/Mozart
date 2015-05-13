(function() {
  'use strict';

  function validateDatesService() {
    /* jshint validthis:true */
    this.current_date = new Date();
    this.current_year = parseInt(this.current_date.getYear()) + 1900;
    this.current_month = parseInt(this.current_date.getMonth()) + 1;
    this.current_day = parseInt(this.current_date.getDate());
    this.validDate = function(day, month, year){
      var newDate = new Date(year, month, '0');
      if((day-0) <= parseInt(newDate.getDate()-0)){
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
    };
  }

  angular.module('mozArtApp')
    .service('validateDates', validateDatesService);
})();