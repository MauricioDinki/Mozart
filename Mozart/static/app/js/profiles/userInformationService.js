(function() {
  'use strict';

  function userInformationService($http) {
    /* jshint validthis:true */
    this.get = function(fnOK,fnError, user, information_to_get) {
      $http({
        method: 'GET',
        url: '/api/' + information_to_get + '/?user=' + user
      })
      .success(function(data, status, headers, config) {
        fnOK(data.results[0]);
      })
      .error(function(data, status, headers, config) {
        fnError(data,status);
      });
    };
  }

  userInformationService.$inject = ['$http'];

  angular.module('mozArtApp')
    .service('userInformation', userInformationService);
})();