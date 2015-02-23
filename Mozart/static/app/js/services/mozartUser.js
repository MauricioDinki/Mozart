'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.service:mozartUser
 * @description
 * #mozartUser
 * Service of the mozArtApp
 */

app.service('mozartUser', ['$http',  function($http){
  this.get=function(fnOK,fnError, user) {
    $http({
      method: 'GET',
      url: 'http://mozart.com:8000/api/mozart_user/?username=' + user
    })
    .success(function(data, status, headers, config) {
      fnOK(data);
    })
    .error(function(data, status, headers, config) {
      fnError(data,status);
    });
  };
}]);

app.service('user', ['$http',  function($http){
  this.get=function(fnOK,fnError, user) {
    $http({
      method: 'GET',
      url: 'http://mozart.com:8000/api/users/?username=' + user
    })
    .success(function(data, status, headers, config) {
      fnOK(data);
    })
    .error(function(data, status, headers, config) {
      fnError(data,status);
    });
  };
}]);

app.service('contact', ['$http',  function($http){
  this.get=function(fnOK,fnError, user) {
    $http({
      method: 'GET',
      url: 'http://mozart.com:8000/api/user_contact/?username=' + user
    })
    .success(function(data, status, headers, config) {
      fnOK(data);
    })
    .error(function(data, status, headers, config) {
      fnError(data,status);
    });
  };
}]);
app.service('dateOfBirth', ['$http',  function($http){
  this.get=function(fnOK,fnError, user) {
    $http({
      method: 'GET',
      url: 'http://mozart.com:8000/api/user_dateofbirth/?username=' + user
    })
    .success(function(data, status, headers, config) {
      fnOK(data);
    })
    .error(function(data, status, headers, config) {
      fnError(data,status);
    });
  };
}]);
app.service('adress', ['$http',  function($http){
  this.get=function(fnOK,fnError, user) {
    $http({
      method: 'GET',
      url: 'http://mozart.com:8000/api/adress/?username=' + user
    })
    .success(function(data, status, headers, config) {
      fnOK(data);
    })
    .error(function(data, status, headers, config) {
      fnError(data,status);
    });
  };
}]);