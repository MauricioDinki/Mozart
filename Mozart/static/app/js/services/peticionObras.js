'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.service:peticionObras
 * @description
 * #peticionObras
 * Service of the mozArtApp
 */

app.service('peticionObras', ['$http',  function($http){
  this.get=function(fnOK,fnError, modo, categoria, autor, cantidad) {
    console.log('http://mozart.com:8000/api/worksets/?' + 'category=' + categoria + '&author=' + autor +  '&paginate=' + cantidad);
    $http({
      method: 'GET',
      url: 'http://mozart.com:8000/api/worksets/?' + 'category=' + categoria + '&author=' + autor +  '&paginate=' + cantidad
    })
    .success(function(data, status, headers, config) {
      fnOK(data);
    })
    .error(function(data, status, headers, config) {
      fnError(data,status);
    });
  };
}]);
