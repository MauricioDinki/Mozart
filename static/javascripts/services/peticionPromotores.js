'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.service:peticionPromotores
 * @description
 * #peticionPromotores
 * Service of the mozArtApp
 */

app.service('peticionPromotores', ['$http',  function($http){
  this.get=function(fnOK,fnError, modo, inicial, cantidad) {
    $http({
      method: 'GET',
      url: 'data/promotores' + cantidad + '.json'
    })
    .success(function(data, status, headers, config) {
      fnOK(data);
    })
    .error(function(data, status, headers, config) {
      fnError(data,status);
    });
  };
}]);
