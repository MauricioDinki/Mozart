'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.service:mozartUser
 * @description
 * #mozartUser
 * Service of the mozArtApp
 */

app.service('userInformation', ['$http',  function($http){
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
}]);