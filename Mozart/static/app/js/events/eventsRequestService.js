(function() {
  'use strict';

  function eventsRequestService($http, $filter, validateDates) {
    /* jshint validthis:true */
    var apiBaseUrl = '/api/events/';
    this.get = function(fnOK,fnError, creator, pageNumber) {
        var requestUrl;
        if(creator==='all') {
          requestUrl = apiBaseUrl + '?page=' + pageNumber;
        }
        else {
          requestUrl = apiBaseUrl + '?user=' + creator + '&page=' + pageNumber;
        }
        $http({
          method: 'GET',
          url: requestUrl
        })
        .success(function(data, status, headers, config) {
          fnOK(data.results, data.next);
        })
        .error(function(data, status, headers, config) {
          fnError(data,status);
        });
    };
    this.checkRepeatedEvent = function(eventsArray, _event) {
      return $filter('filter')(
        eventsArray,
        _event,
        true
      )[0] ? true: false;
    };
    this.checkFinishedEvent = function(_event) {
      console.log(validateDates.futureDate(_event.date));
      return !validateDates.futureDate(_event.date);
    };
  }

  eventsRequestService.$inject = ['$http', '$filter', 'validateDates'];

  angular.module('mozArtApp')
    .service('eventsRequest', eventsRequestService);
})();