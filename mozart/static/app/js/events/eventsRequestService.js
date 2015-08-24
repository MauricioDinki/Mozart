(function () {
    'use strict';

    function eventsRequestService(baseRequest, validateDates, $window) {
    /* jslint validthis:true */
        var apiSectionName = 'events';
        function getParameters(creator, pageNumber) {
            var parameters;
            if (creator === 'all') {
                parameters = '?page=' + pageNumber;
            } else {
                parameters = '?user=' + creator + '&page=' + pageNumber;
            }
            return parameters;
        }
        this.get = function (fnOK, parameters, pageNumber) {
            var creator, requestParameters;
            creator = parameters[0];
            requestParameters = getParameters(creator, pageNumber);
            /*jslint unparam: true*/
            baseRequest.get(
                fnOK,
                function (data, status) {
                    $window.alert('Ha fallado la petición. Estado HTTP:' + status);
                },
                apiSectionName,
                requestParameters
            );
            /*jslint unparam: false*/
        };
        this.checkRepeatedEvent = function (events, mzEvent) {
            return baseRequest.checkRepeatedItem(events, mzEvent);
        };
        this.checkFinishedEvent = function (mzEvent) {
            return !validateDates.futureDate(mzEvent.date);
        };
    }

    eventsRequestService.$inject = ['baseRequest', 'validateDates', '$window'];

    angular.module('mozArtApp')
        .service('eventsRequest', eventsRequestService);
}());