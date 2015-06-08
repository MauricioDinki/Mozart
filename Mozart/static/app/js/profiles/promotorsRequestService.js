(function() {
  'use strict';

  function promotersRequestService($http, $filter) {
    /* jshint validthis:true */
    var apiBaseUrl = '/api/mozart/?user_type=Promotor';
    // this.get=function(fnOK,fnError, nameFirstLetter, paginate) {
    //   $http({
    //     method: 'GET',
    //     url: apiBaseUrl + '?' + 'nameFirstLetter=' + nameFirstLetter +  '&paginate=' + paginate
    //   })
    this.get=function(fnOK,fnError, paginate) {
      $http({
        method: 'GET',
        url: apiBaseUrl + '&paginate=' + paginate
      })
      .success(function(data, status, headers, config) {
        fnOK(data.results);
      })
      .error(function(data, status, headers, config) {
        fnError(data,status);
      });
    };
    this.checkRepeatedUser = function(usersArray, user) {
      return $filter('filter')(
        usersArray,
        user
      )[0];
    };
  }

  promotersRequestService.$inject = ['$http', '$filter'];

  angular.module('mozArtApp')
    .service('promotersRequest', promotersRequestService);
})();