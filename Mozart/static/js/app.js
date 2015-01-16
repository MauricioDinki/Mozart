var app = angular.module('mozArtApp', ['ngTagsInput']);
//Importar ngRoute en un futuro
app.config(['$interpolateProvider', function($interpolateProvider){
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
}]);
/* Bloques run y config que n oserá utilizado hasta solucionar inconveniente con rutas
app.config(['$routeProvider', function($routeProvider) {
	$routeProvider
		.when('/', {
			templateUrl: 'views/bienvenida.html',
			controller: 'cargarObrasCtrl',
			title: 'Bienvenido a '
		})
		.when('/explorar/:categoria?', {
			templateUrl: 'views/principal.html',
			controller: 'cargarObrasCtrl',
			title: 'Explorar - '
		})
		.when('/promotores/:inicial?', {
			templateUrl: 'views/promotores.html',
			controller: 'cargarPromotoresCtrl',
			title: 'Promotores - '
		})
		.when('/login', {
			templateUrl: 'views/login.html',
			controller: 'loginCtrl',
			title: 'Log in - '
		})
		.when('/registro/promotor', {
			templateUrl: 'views/registropromotor.html',
			controller: 'formularioRegistroCtrl',
			title: 'Registro de promotor - '
		})
		.when('/registro/artista', {
			templateUrl: 'views/registroArtista.html',
			controller: 'formularioRegistroCtrl',
			title: 'Registro de artista - '
		})
		.when('/artista/:numero', {
			templateUrl: 'views/perfilArtista.html',
			controller: 'perfilArtistaCtrl',
			title: 'Perfil de Artista - '
		})
		.when('/artista/:numero/obras/:categoria?', {
			templateUrl: 'views/perfilobras.html',
			controller: 'perfilArtistaCtrl',
			title: 'Obras de Artista - '
		})
		.when('/artista/:numero/carpetas', {
			templateUrl: 'views/perfilcarpetas.html',
			controller: 'perfilArtistaCtrl',
			title: 'Carpetas de Artista - '
		})
		.when('/obra/:numero', {
			templateUrl: 'views/obra.html',
			controller: 'obrasCtrl',
			title: 'Obra - '
		})
		.when('/promotor/:numero', {
			templateUrl: 'views/perfilPromotor.html',
			controller: 'perfilPromotorCtrl',
			title: 'Perfil de promotor - '
		}).when('/crear', {
			templateUrl: 'views/subirobra.html',
			controller: 'subirObraCtrl',
			title: 'Subir obra - '
		}).when('/panel', {
			redirectTo: '/panel/informacion'
		}).when('/panel/informacion', {
			templateUrl: 'views/panelusuario.html',
			controller: 'editarInformacionCtrl',
			title: 'Editar informacion - '
		}).when('/panel/cuenta', {
			templateUrl: 'views/configuraciones.html',
			controller: 'configuracionesCtrl',
			title: 'Configurar cuenta - '
		}).when('/panel/estadisticas', {
			templateUrl: 'views/panelestadisticas.html',
			controller: 'configuracionesCtrl',
			title: 'Mis estadísticas - '
		}).when('/panel/obras', {
			templateUrl: 'views/panelobras.html',
			controller: 'cargarObrasCtrl',
			title: 'Mis obras - '
		}).when('/panel/mensajes', {
			templateUrl: 'views/panelnodisponible.html',
			controller: 'configuracionesCtrl',
			title: 'Mensajes privados - '
		}).when('/panel/notificaciones', {
			templateUrl: 'views/panelnodisponible.html',
			controller: 'configuracionesCtrl',
			title: 'Notificaciones - '
		}).when('/panel/listas', {
			templateUrl: 'views/panelnodisponible.html',
			controller: 'configuracionesCtrl',
			title: 'Mis listas - '
		}).when('/panel/boletines', {
			templateUrl: 'views/panelnodisponible.html',
			controller: 'configuracionesCtrl',
			title: 'Mis boletínes - '
		}).when('/panel/eventos', {
			templateUrl: 'views/panelnodisponible.html',
			controller: 'configuracionesCtrl',
			title: 'Mis eventos - '
		}).when('/panel/carpetas', {
			templateUrl: 'views/panelnodisponible.html',
			controller: 'configuracionesCtrl',
			title: 'Mis carpetas - '
		}).when('/error', {
	        		templateUrl: 'views/error404.html',
	        		controller: 'errorCtrl',
	        		title: 'Error - '
		})
		.otherwise({
	        		redirectTo: '/error'
	  	});

}]);

app.run(['$location', '$rootScope', function($location, $rootScope) {
	$rootScope.$on('$routeChangeSuccess', function (event, current, previous) {
		$rootScope.title = current.$$route.title;
		window.scrollTo(0,0);
	});
}]);
*/
