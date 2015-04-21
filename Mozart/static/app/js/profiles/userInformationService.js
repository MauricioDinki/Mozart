(function() {
  'use strict';

  function userInformationService($http) {
    this.get = function(fnOK,fnError, user, information_to_get) {
      $http({
        method: 'GET',
        url: '/api/' + information_to_get + '/?username=' + user
      })
      .success(function(data, status, headers, config) {
        fnOK(data);
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