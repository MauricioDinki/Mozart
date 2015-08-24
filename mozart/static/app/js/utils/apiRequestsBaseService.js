(function () {
    'use strict';

    function baseRequestService($http, $filter) {
        /* jslint validthis:true */
        var apiBaseUrl = '/api/';
        /*jslint unparam: true*/
        this.get = function (fnOK, fnError, apiSection, parameters) {
            $http({
                method: 'GET',
                url: apiBaseUrl + apiSection + parameters
            })
                .success(function (data, status, headers, config) {
                    fnOK(data);
                })
                .error(function (data, status, headers, config) {
                    fnError(data, status);
                });
        };
        /*jslint unparam: false*/
        this.checkRepeatedItem = function (itemsArray, item) {
            return $filter('filter')(
                itemsArray,
                item,
                true
            )[0] ? true : false;
        };
    }

    baseRequestService.$inject = ['$http', '$filter'];

    angular.module('mozArtApp')
        .service('baseRequest', baseRequestService);
}());