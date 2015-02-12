'use strict';

/**
 * @ngdoc overview
 * @name mozArtApp
 * @description
 * # mozArtApp
 *
 * Main module of the application.
 */
var app = angular.module('mozArtApp', ['ng.django.forms']);

app.config(['$interpolateProvider', '$httpProvider', function($interpolateProvider, $httpProvider){
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
}]);
app.directive('fileUpload', [function () {
	return {
    restrict: 'A',
		scope: {
			fileBind : '='
		},
		link: function (scope, el, attrs) {
			el.bind('change', function (event) {
				var files = event.target.files;
				for (var i = 0;i<files.length;i++) {
					scope.$emit(scope.fileBind, { file: files[i] });
				}
			});
		}
	};
}]);

app.directive('offClick', ['$document', '$timeout', function ($document, $timeout) {
	function targetInFilter(target,filter){
        		if(!target || !filter) return false;
        		var elms = angular.element(document.querySelectorAll(filter));
        		var elmsLen = elms.length;
        		for (var i = 0; i< elmsLen; ++i)
            			if(elms[i].contains(target)) return true;
        		return false;
   	}
	return {
        		restrict: 'A',
        		scope: {
            			offClick: '&',
            			offClickIf: '&'
        		},
       		link: function (scope, elm, attr) {
			if (attr.offClickIf) {
                			scope.$watch(scope.offClickIf, function (newVal, oldVal) {
                        				if (newVal && !oldVal) {
	                            				$timeout(function() {
	                                				$document.on('click', handler);
	                            				});
                        				} else if(!newVal){
                            					$document.off('click', handler);
                        				}
                   			}
                		);
            			} else {
              				$document.on('click', handler);
            			}

            			scope.$on('$destroy', function() {
                			$document.off('click', handler);
            			});

            			function handler(event) {
                // This filters out artificial click events. Example: If you hit enter on a form to submit it, an
                // artificial click event gets triggered on the form's submit button.
               				if (event.pageX == 0 && event.pageY == 0) return;
				var target = event.target || event.srcElement;
                			if (!(elm[0].contains(target) || targetInFilter(target, attr.offClickFilter))) {
                    				scope.$apply(scope.offClick());
                			}
            			}
        		}
   	};
}]);

app.directive('modalDialog', function() {
	return {
		restrict: 'E',
		scope: {
			show: '=',
			tituloVentana: '@'
		},
		replace: true,
		transclude: true,
		link: function(scope, element, attrs) {
			scope.hideModal = function() {
				scope.show = false;
			};
		},
		templateUrl: 'scripts/directives/ventanaModal.html'
	};
});
app.directive('comparar', function() {
  return {
  	restrict: 'A',
    require: 'ngModel',
    scope: {
    	compareTo: '=comparar'
    },
    link: function(scope, elem, attrs, ctrl) {
    	scope.validar = function(){
    		return scope.compareTo === ctrl.$modelValue;
    	};
      	scope.$watch(
      		scope.validar, 
      		function(currentValue) {
        		ctrl.$setValidity('noIguales', currentValue);
      		}
      	);
    }
  };
});
app.directive('mzField', function() {
  return {
  	restrict: 'C',
    link: function(scope, elem, attrs, ctrl) {
    	var elemento = '#' + attrs.id;
    	angular.element(elemento).focus(function(){
        angular.element(elemento).prev('label').css('width', '0%'); 
        angular.element(elemento).prev('label').css('padding', '5px 0');
    		angular.element(elemento).css('width', '90%');
    	});
    	angular.element(elemento).blur(function(){
    		angular.element(elemento).prev('label').css('padding', '5px 10px');
        angular.element(elemento).prev('label').css('width', '30%');
        angular.element(elemento).css('width', '60%');
    	});
    }
  };
});'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:cargarObrasCtrl
 * @description
 * # cargarObrasCtrl
 * Controller of the mozArtApp
 */

//Falta opcion de mostrar mensajes
app.controller('cargarObrasCtrl', ['$scope', /*'$routeParams', */'peticionObras', function($scope,/*$routeParams,*/ peticionObras){
  $scope.cantidad = 5;
  $scope.categoria = 'a'/*$routeParams.categoria*/;
  $scope.cargar = function(nuevaCantidad){
    peticionObras.get(
      function(obras) {
        $scope.obras = obras;
      },
      function(data, status) {
        alert('Ha fallado la petición. Estado HTTP:' + status);
      },
      'recientes',
      $scope.categoria,
      'todos',
      nuevaCantidad
    );
    $scope.cantidad += 4;
  };
  $scope.cargar($scope.cantidad);
  $scope.prueba = 'http://www.google.com';
}]);
'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:editarInformacionCtrl
 * @description
 * # editarInformacionCtrl
 * Controller of the mozArtApp
 */

//Aun falta agregar la peticion ajax para mostrar barra de progreso
app.controller('editarInformacionCtrl', ['$scope', function($scope){
  $scope.videoValido = true;
  $scope.portadaValida = true;
  $scope.imagenValida = true;
  $scope.video = {
    name: ''
  };
  $scope.portada = {
    name: ''
  };
  $scope.imagen = {
    name: ''
  };
  $scope.$on('archivoVideo', function (event, args) {
    $scope.$apply(function () { //add the file object to the scope's files collection
      $scope.video = args.file;
      divisiones = $scope.video.name.split('.');
      $scope.formatoVideo = divisiones[divisiones.length - 1];
      $scope.videoValido = $scope.verificarVideo($scope.formatoVideo);
    });
  });
  $scope.$on('archivoPortada', function (event, args) {
    $scope.$apply(function () { //add the file object to the scope's files collection
      $scope.portada = args.file;
      divisiones = $scope.portada.name.split('.');
      $scope.formatoPortada = divisiones[divisiones.length - 1];
      $scope.portadaValida = $scope.verificarImagen($scope.formatoPortada);
    });
  });
  $scope.$on('archivoImagen', function (event, args) {
    $scope.$apply(function () { //add the file object to the scope's files collection
      $scope.imagen = args.file;
      divisiones = $scope.imagen.name.split('.');
      $scope.formatoImagen = divisiones[divisiones.length - 1];
      $scope.imagenValida = $scope.verificarImagen($scope.formatoImagen);
    });
  });
  $scope.verificarVideo = function(formato){
    formatosVideo = ['mp4', 'mpeg', 'avi', '3gp'];
    for(i = 0; i < formatosVideo.length; i++){
      if(formato == formatosVideo[i]){
        return true;
      }
    }
    return false;
  };
  $scope.verificarImagen = function(formato){
    formatosImagen = ['png', 'gif', 'jpg', 'jpeg', 'bmp', 'tiff'];
    for(i = 0; i < formatosImagen.length; i++){
      if(formato == formatosImagen[i]){
        return true;
      }
    }
    return false;
  };
}]);
'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:errorCtrl
 * @description
 * # errorCtrl
 * Controller of the mozArtApp
 */

app.controller('errorCtrl', ['$scope', '$routeParams', 'peticionObras', function($scope, $routeParams, peticionObras){
  $scope.cantidad = 3;
  $scope.cargar = function(){
    peticionObras.get(
      function(obras) {
        $scope.obras = obras;
      },
      function(data, status) {
        alert('Ha fallado la petición. Estado HTTP:' + status);
      },
      'aleatorio',
      'todas',
      'todos',
      $scope.cantidad
    );
  };
  $scope.cargar();
}]);
'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:formularioRegistroCtrl
 * @description
 * # formularioRegistroCtrl
 * Controller of the mozArtApp
 */
//Aun falta agregar la peticion ajax para mostrar barra de progreso
app.controller('formularioRegistroCtrl', ['$scope', 'validateAge', function($scope, validateAge){
  $scope.acepto = false;
  $scope.fechaValida = true;
  $scope.mensaje = true;
  var month = 1;
  $scope.validarFecha = function(){
    $scope.mensaje = validateAge.validDate($scope.signup.day_of_birth, $scope.signup.month_of_birth, $scope.signup.year_of_birth);
    $scope.fechaValida = ($scope.mensaje === 'Ok');
  };
  $scope.validar = function(){
    return !(!$scope.fechaValida || $scope.signupform.$invalid);
  };
}]);
/**
 * @ngdoc function
 * @name mozArtApp.controller:menuCtrl
 * @description
 * # menuCtrl
 * Controller of the mozArtApp
 */
app.controller('menuCtrl', ['$scope', function($scope){
  $scope.visible = false;
  $scope.posicion1 = {
    'right' : '-305px'
  };
  $scope.posicion2 = {
    'right' : '0'
  };
  $scope.posicionDerecha = $scope.posicion1;
  $scope.mostrarMenu= function(){
    if($scope.visible == true){
      $scope.posicionDerecha = $scope.posicion1;
      $scope.visible = false;
    }
    else{
      $scope.posicionDerecha = $scope.posicion2
      $scope.visible = true;
    }
  };
}]);
'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:modalCtrl
 * @description
 * # modalCtrl
 * Controller of the mozArtApp
 */

app.controller('modalCtrl', ['$scope', function($scope) {
  $scope.modalShown = false;
  $scope.toggleModal = function() {
    $scope.modalShown = !$scope.modalShown;
  };
}]);
'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:otros
 * @description
 * # otros
 * Controller of the mozArtApp
 */

//Este controlador aun no esta escrito
app.controller('perfilArtistaCtrl', ['$scope', '$log', function($scope, $log){
  $log.log('Hola');
}]);

//Este controlador aun no esta escrito
app.controller('perfilPromotorCtrl', ['$scope', '$log', function($scope, $log){
  $log.log('Hola');
}]);

//Este controlador aun no esta escrito
app.controller('informacionPerfilCtrl', ['$scope', '$log', function($scope, $log){
  $log.log('Hola');
}]);

//Este controlador aun no esta escrito
app.controller('configuracionesCtrl', ['$scope', function($scope){
  $scope.validar = function(){
    alert('Hola ' + $scope.email + '!');
  };
}]);

//Este controlador aun no esta escrito, es necesario agregar funciones para login con vinculacion
app.controller('loginCtrl', ['$scope', function($scope){
  $scope.validar = function(){
    alert('Hola ' + $scope.email + '!');
  };
}]);
'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:subirObraCtrl
 * @description
 * # subirObraCtrl
 * Controller of the mozArtApp
 */

app.controller('subirObraCtrl', ['$scope', 'validateFile', function($scope, validateFile){
  $scope.maxeti = 30;
  $scope.archivo = {
    name: ''
  };
  $scope.portada = {
    name: ''
  };

  var archivoImagen = true;
  var archivoValido = false;
  var portadaValida = false;

  $scope.mostrarTexto1 = function(){
    return $scope.archivo.name != '';
  };
  $scope.mostrarTexto2 = function(){
    return $scope.portada.name != '';
  };
  $scope.mostrarMensaje1 = function(){
    return !(archivoValido || $scope.archivo.name == '');
  };
  $scope.mostrarMensaje2 = function(){
    return !(portadaValida || $scope.portada.name == '');
  };
  $scope.mostrarBoton2 = function(){
    return !(archivoImagen || !archivoValido);
  };

  $scope.$on('archive', function (event, args) {
    $scope.$apply(function () {
      $scope.archivo = args.file;
      var formato = validateFile.getExtension($scope.archivo);
      archivoImagen = validateFile.isAnImage(formato);
      if(archivoImagen){
        archivoValido = true;
        portadaValida = true;
      }
      else{
        archivoValido = validateFile.validateFormat(formato);
        portadaValida = false;
      }
    });
  });
  $scope.$on('cover', function (event, args) {
    $scope.$apply(function () {
      $scope.portada = args.file;
      var formato = validateFile.getExtension($scope.portada);
      portadaValida = validateFile.isAnImage(formato);
    });
  });
  $scope.validar = function(){
    return !(!archivoValido || !portadaValida || $scope.workform.$invalid);
  };
}]);
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
    $http({
      method: 'GET',
      url: 'http://localhost:8000/api/works'
    })
    .success(function(data, status, headers, config) {
      fnOK(data);
    })
    .error(function(data, status, headers, config) {
      fnError(data,status);
    });
  };
}]);
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
'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.service:validateFile
 * @description
 * # validateFile
 * Service of the mozArtApp
 */

app.service('validateFile', function(){
  this.getExtension = function(fileObject){
    var divisions = fileObject.name.split('.');
    var fileExtension = divisions[divisions.length -1];
    return fileExtension;
  };
  this.validateFormat = function(fileExtension){
    var validFormats = ['pdf', 'mp3', 'aac', 'wma', 'mp4', 'mpeg', 'avi', '3gp'];
    for(var i = 0; i < validFormats.length; i++){
      if(fileExtension == validFormats[i]){
        return true;
      }
    }
    return false;
  };
  this.isAnImage = function(fileExtension){
    var imageFormats = ['png', 'gif', 'jpg', 'jpeg', 'bmp', 'tiff'];
    for(var i = 0; i < imageFormats.length; i++){
      if(fileExtension == imageFormats[i]){
        return true;
      }
    }
    return false;
  };
});'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.service:validateAge
 * @description
 * # validateAge
 * Service of the mozArtApp
 */

app.service('validateAge', function(){
  this.current_date = new Date();
  this.current_year = parseInt(this.current_date.getYear()) + 1900;
  this.current_month = parseInt(this.current_date.getMonth()) + 1;
  this.current_day = parseInt(this.current_date.getDate());
  this.validDate = function(day, monthName, year){
    var month;
    if(isNaN(monthName)){
      month = this.getMonthNumber(monthName);
    }
    else{
      month = monthName;
    }
    var newDate = new Date(year, month, '0');
    if(!((day-0) > (newDate.getDate()-0))){
      return this.validAge(day, month, year);
    }
    else{
      return 'La fecha que introduciste no es valida.';
    }
  };
  this.validAge = function(day, month, year){
    var datesDifference = this.current_year - year;
    if(this.current_month < month){
      datesDifference--;
    }
    if((month === this.current_month) && (this.current_day < day)){
      datesDifference--;
    }
    if(datesDifference > 1900){
      datesDifference -= 1900;
    }
    if(datesDifference >= 18){
      return 'Ok';
    }
    else{
      return 'Lo sentimos, debes ser mayor de edad';
    }
  }
  this.getMonthNumber = function(monthName){
    if(monthName === 'Enero'){
      return 1;
    }
    else if(monthName === 'Febrero'){
      return 2;
    }
    else if(monthName === 'Marzo'){
      return 3;
    }
    else if(monthName === 'Abril'){
      return 4;
    }
    else if(monthName === 'Mayo'){
      return 5;
    }
    else if(monthName === 'Junio'){
      return 6;
    }
    else if(monthName === 'Julio'){
      return 7;
    }
    else if(monthName === 'Agosto'){
      return 8;
    }
    else if(monthName === 'Septiembre'){
      return 9;
    }
    else if(monthName === 'Octubre'){
      return 10;
    }
    else if(monthName === 'Noviembre'){
      return 11;
    }
    else if(monthName === 'Diciembre'){
      return 1;
    }
    else{
      return 0;
    }
  };
});

