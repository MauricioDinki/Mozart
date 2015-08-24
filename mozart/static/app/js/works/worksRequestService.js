(function () {
    'use strict';

    function worksRequestService(baseRequest, $window) {
        /* jslint validthis:true */
        var apiSectionName = 'worksets';
        function getParameters(category, author, pageNumber) {
            var parameters;
            if (category === 'all' && author === 'all') {
                parameters = '?page=' + pageNumber;
            } else if (category === 'all') {
                parameters = '?user=' + author + '&page=' + pageNumber;
            } else if (author === 'all') {
                parameters = '?category=' + category + '&page=' + pageNumber;
            } else {
                parameters = '?user=' + author +  '&category=' + category + '&page=' + pageNumber;
            }
            return parameters;
        }
        this.recentWorks = function (fnOK, parameters, pageNumber) {
            var category, author, requestParameters;
            category = parameters[0];
            author = parameters[1];
            requestParameters = getParameters(category, author, pageNumber);
            baseRequest.get(
                fnOK,
                function (status) {
                    $window.alert('Ha fallado la petición. Estado HTTP:' + status);
                },
                apiSectionName,
                requestParameters
            );
        };
        // this.randomWorks = function(fnOK, category, author, pageNumber){
        // };
        this.checkRepeatedWork = function (works, work) {
            return baseRequest.checkRepeatedItem(works, work);
        };
    }

    worksRequestService.$inject = ['baseRequest', '$window'];

    angular.module('mozArtApp')
        .service('worksRequest', worksRequestService);
}());