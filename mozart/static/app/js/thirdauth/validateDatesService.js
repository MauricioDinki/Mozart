(function () {
    'use strict';

    function validateDatesService() {
        /* jslint validthis:true */
        this.full_current_date = new Date();
        this.current_year = parseInt(this.full_current_date.getYear(), 10) + 1900;
        this.current_month = parseInt(this.full_current_date.getMonth(), 10) + 1;
        this.current_day = parseInt(this.full_current_date.getDate(), 10);
        this.current_date = new Date(this.current_year, this.current_month - 1, this.current_day);
        this.validDate = function (day, monthName, year, age) {
            var month, newDate;
            if (isNaN(monthName)) {
                month = this.getMonthNumber(monthName);
            } else {
                month = monthName;
            }
            newDate = new Date(year, month, '0');
            if (day <= parseInt(newDate.getDate(), 10)) {
                return this.validAge(day, month, year, age);
            }
            return 'La fecha que introduciste no es valida.';
        };
        this.validAge = function (day, month, year, age) {
            var datesDifference = this.current_year - year;
            if (this.current_month < month) {
                datesDifference += 1;
            }
            if ((month === this.current_month) && (this.current_day < day)) {
                datesDifference += 1;
            }
            if (datesDifference > 1900) {
                datesDifference -= 1900;
            }
            if (datesDifference >= age) {
                return 'Ok';
            }
            return 'Lo sentimos, debes ser mayor de edad';
        };
        this.futureDate = function (date) {
            var date_elements, new_date;
            date_elements = date.split('-');
            new_date = new Date(date_elements[0], date_elements[1] - 1, date_elements[2]);
            return new_date.getTime() - this.current_date.getTime() >= 86400000;
        };
        this.validDuration = function (start_time, finish_time) {
            var start_time_elements, finish_time_elements, absolute_start_time, absolute_finish_time;
            start_time_elements = String(start_time.$modelValue).split(':');
            finish_time_elements = String(finish_time.$modelValue).split(':');
            absolute_start_time = (parseInt(start_time_elements[0], 10) * 60) + parseInt(start_time_elements[1], 10);
            absolute_finish_time = (parseInt(finish_time_elements[0], 10) * 60) + parseInt(finish_time_elements[1], 10);
            return absolute_finish_time >= absolute_start_time + 30;
        };
        this.getMonthNumber = function (monthName) {
            switch (monthName) {
            case 'Enero':
                return 1;
            case 'Febrero':
                return 2;
            case 'Marzo':
                return 3;
            case 'Abril':
                return 4;
            case 'Mayo':
                return 5;
            case 'Junio':
                return 6;
            case 'Julio':
                return 7;
            case 'Agosto':
                return 8;
            case 'Septiembre':
                return 9;
            case 'Octubre':
                return 10;
            case 'Noviembre':
                return 11;
            case 'Diciembre':
                return 12;
            default:
                return 0;
            }
        };
    }

    angular.module('mozArtApp')
        .service('validateDates', validateDatesService);
}());