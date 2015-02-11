'use strict';

/**
 * @ngdoc overview
 * @name mozArtApp
 * @description
 * # mozArtApp
 *
 * Main module of the application.
 */
var app = angular.module('mozArtApp', ['ngTagsInput', 'angularFileUpload', 'ng.django.forms']);

app.config(['$interpolateProvider', '$httpProvider', function($interpolateProvider, $httpProvider){
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
}]);
app.directive('fileUpload', [function () {
	return {
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
app.controller('formularioRegistroCtrl', ['$scope', function($scope){
  $scope.acepto = false;
  $scope.fechaValida = true;
  $scope.mayorEdad = true;
  $scope.nicknameValido = true;
  $scope.nicknamePrueba = 'holi crayholi';
  $scope.emailValido = true;
  $scope.emailPrueba = 'aaa@aaa.com';
  $scope.fecha_actual = new Date();
  $scope.this_year = parseInt($scope.fecha_actual.getYear()) + 1900;
  $scope.validarFecha = function(){
    var date = new Date($scope.year,$scope.mes, '0');
    var this_month = parseInt($scope.fecha_actual.getMonth() + 1);
    var this_day = parseInt($scope.fecha_actual.getDate());
    var resta_fechas = $scope.this_year - $scope.year;
    if(($scope.dia-0)>(date.getDate()-0)){
      $scope.fechaValida = false;
    }
    else{
      $scope.fechaValida = true;
    }
    if(this_month < $scope.mes){
      resta_fechas--;
    }
    if(($scope.mes == this_month) && (this_day < $scope.dia)){
      resta_fechas--;
    }
    if(resta_fechas > 1900){
      resta_fechas -= 1900;
    }
    if(resta_fechas >= 18){
      $scope.mayorEdad = true;
    }
    else{
      $scope.mayorEdad = false;
    }
  };
  $scope.verificarNickname = function(){
    if($scope.nickname == $scope.nicknamePrueba){
      $scope.nicknameValido = false;
    }
    else{
      $scope.nicknameValido = true;
    }
  };
  $scope.verificarEmail = function(){
    if($scope.email == $scope.emailPrueba){
      $scope.emailValido = false;
    }
    else{
      $scope.emailValido = true;
    }
  };
  $scope.validar = function(){
    return !(!$scope.fechaValida || !$scope.mayorEdad || !$scope.emailValido || !$scope.nicknameValido || $scope.registro.$invalid);
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

//Aun falta agregar la peticion ajax para mostrar barra de progreso
app.controller('subirObraCtrl', ['$scope', function($scope){
  $scope.maxeti = 30;
  $scope.archivo = {
    name: ''
  };
  $scope.portada = {
    name: ''
  };
  $scope.formatoArchivo = '';
  $scope.formatoPortada = '';
  $scope.archivoImagen = true;
  $scope.archivoValido = false;
  $scope.portadaValida = false;

  $scope.$on('archivoPrincipal', function (event, args) {
    $scope.$apply(function () {
      $scope.archivo = args.file;
      divisiones = $scope.archivo.name.split('.');
      $scope.formatoArchivo = divisiones[divisiones.length - 1];
      $scope.archivoValido = $scope.verificarFormato();
    });
  });
  $scope.$on('archivoPortada', function (event, args) {
    $scope.$apply(function () {
      $scope.portada = args.file;
      divisiones = $scope.portada.name.split('.');
      $scope.formatoPortada = divisiones[divisiones.length - 1];
      $scope.portadaValida = $scope.verificarImagen($scope.formatoPortada);
    });
  });
  $scope.verificarFormato = function(){
    otrosFormatos = ['pdf', 'mp3', 'aac', 'wma', 'mp4', 'mpeg', 'avi', '3gp'];
    $scope.archivoImagen = $scope.verificarImagen($scope.formatoArchivo);
    if($scope.archivoImagen == true){
      $scope.portadaValida = true;
      return true;
    }
    else{
      $scope.portadaValida = $scope.verificarImagen($scope.formatoPortada);
      for(i = 0; i < otrosFormatos.length; i++){
        if($scope.formatoArchivo == otrosFormatos[i]){
          return true;
        }
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
  $scope.validar = function(){
    return !(!$scope.archivoValido || !$scope.portadaValida || $scope.subirobra.$invalid);
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
