(function() {
  'use strict';

  function promotorsRequestService($http) {
    var apiBaseUrl = '/api/promotors/';
    this.get=function(fnOK,fnError, nameFirstLetter, paginate) {
      $http({
        method: 'GET',
        url: apiBaseUrl + '?' + 'nameFirstLetter=' + nameFirstLetter +  '&paginate=' + paginate
      })
      .success(function(data, status, headers, config) {
        fnOK(data);
      })
      .error(function(data, status, headers, config) {
        fnError(data,status);
      });
    };
  }

  promotorsRequestService.$inject =  ['$http'];

  angular.module('mozArtApp')
    .service('promotorsRequest', promotorsRequestService);
})();