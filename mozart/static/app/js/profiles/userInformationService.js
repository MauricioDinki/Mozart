(function() {
  'use strict';

  function userInformationService($http) {
    /* jshint validthis:true */
    this.get = function(fnOK,fnError, user, information_to_get) {
      var userParameterName = 'user';
      if(information_to_get === 'users') {
        userParameterName = 'username';
      }
      $http({
        method: 'GET',
        url: '/api/v1/' + information_to_get + '/?' + userParameterName + '=' + user
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
