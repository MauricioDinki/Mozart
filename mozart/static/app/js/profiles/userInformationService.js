(function () {
    'use strict';

    function userInformationService(baseRequest, $window) {
        /* jslint validthis:true */
        this.get = function (fnOK, user, information_to_get) {
            var parameters, userParameterName;
            function getParameters() {
                return '?' + userParameterName + '=' + user;
            }
            userParameterName = 'user';
            if (information_to_get === 'users') {
                userParameterName = 'username';
            }
            parameters = getParameters();
            baseRequest.get(
                fnOK,
                function (status) {
                    $window.alert('Ha fallado la petición. Estado HTTP:' + status);
                },
                information_to_get,
                parameters
            );
        };
    }

    userInformationService.$inject = ['baseRequest', '$window'];

    angular.module('mozArtApp')
        .service('userInformation', userInformationService);
}());