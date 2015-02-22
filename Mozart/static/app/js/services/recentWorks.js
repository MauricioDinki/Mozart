'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.service:getRecentWorks
 * @description
 * #getRecentWorks
 * Service of the mozArtApp
 */

app.service('recentWorks', ['$http',  function($http){
  this.get=function(fnOK,fnError, category, author, paginate) {
    $http({
      method: 'GET',
      url: 'http://mozart.com:8000/api/worksets/?' + 'category=' + category + '&author=' + author +  '&paginate=' + paginate
    })
    .success(function(data, status, headers, config) {
      fnOK(data);
    })
    .error(function(data, status, headers, config) {
      fnError(data,status);
    });
  };
}]);
