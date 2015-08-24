(function () {
    'use strict';

    function promotersRequestService(baseRequest, $window) {
        /* jslint validthis:true */
        var apiSectionName = 'extendedusers';
        function getParameters(pageNumber) {
            var parameters;
            parameters = '?user_type=Promoter&page=' + pageNumber;
            return parameters;
        }
        /*jslint unparam: true*/
        this.get = function (fnOK, parameters, pageNumber) {
            var requestParameters = getParameters(pageNumber);
            baseRequest.get(
                fnOK,
                function (status) {
                    $window.alert('Ha fallado la petición. Estado HTTP:' + status);
                },
                apiSectionName,
                requestParameters
            );
        };
        /*jslint unparam: false*/
        this.checkRepeatedUser = function (usersArray, user) {
            return baseRequest.checkRepeatedItem(usersArray, user);
        };
    }

    promotersRequestService.$inject = ['baseRequest', '$window'];

    angular.module('mozArtApp')
        .service('promotersRequest', promotersRequestService);
}());