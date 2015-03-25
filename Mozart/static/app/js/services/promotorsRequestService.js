'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.service:promotorsRequest
 * @description
 * #promotorsRequest
 * Service of the mozArtApp
 */

app.service('promotorsRequest', ['$http',  function($http){
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
}]);
