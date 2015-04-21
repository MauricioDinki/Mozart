// 'use strict';

// /**
//  * @ngdoc function
//  * @name mozArtApp.controller:imagenPerfilCtrl
//  * @description
//  * # imagenPerfilCtrl
//  * Controller of the mozArtApp
//  */

// app.controller('imagenPerfilCtrl', ['$scope','mozartUser', function($scope, mozartUser){
//   $scope.cargar = function(){
//     mozartUser.get(
//       function(usuario) {
//         if(usuario[0].profile_picture == null){
//           $scope.imagen = '/static/img/default.png'
//         }
//         else{
//           $scope.imagen = usuario[0].profile_picture;
//         }
//       },
//       function(data, status) {
//         alert('Ha fallado la petición. Estado HTTP:' + status);
//       },
//       $scope.usuario
//     );
//   };
//   $scope.cargar();
// }]);