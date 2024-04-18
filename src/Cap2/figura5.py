import matplotlib.pyplot as plt

# Datos de ejemplo
ciudades = ['ALMERIA', 'CADIZ', 'CORDOBA', 'GRANADA', 'HUELVA', 'JAEN', 'MALAGA', 'SEVILLA', 'ANDALUCIA', 'HUESCA', 'TERUEL', 'ZARAGOZA', 'ARAGON', 'PRINCIPADO DE ASTURIAS', 'ILLES BALEARS', 'PALMAS LAS', 'STA. CRUZ DE TENERIFE', 'CANARIAS', 'CANTABRIA', 'ALBACETE', 'CIUDAD REAL', 'CUENCA', 'GUADALAJARA', 'TOLEDO', 'CASTILLA-LA MANCHA', 'AVILA', 'BURGOS', 'LEON', 'PALENCIA', 'SALAMANCA', 'SEGOVIA', 'SORIA', 'VALLADOLID', 'ZAMORA', 'CASTILLA Y LEON', 'BARCELONA', 'GIRONA', 'LLEIDA', 'TARRAGONA', 'CATALUÑA', 'ALICANTE/ALACANT', 'CASTELLON/CASTELLO', 'VALENCIA', 'COM. VALENCIANA', 'BADAJOZ', 'CACERES', 'EXTREMADURA', 'CORUÑA A', 'LUGO', 'OURENSE', 'PONTEVEDRA', 'GALICIA', 'COM. DE MADRID', 'REGION DE MURCIA', 'COM. FORAL DE NAVARRA', 'ARABA/ALAVA', 'BIZKAIA', 'GIPUZKOA', 'PAIS VASCO', 'LA RIOJA', 'CEUTA', 'MELILLA', 'TOTAL NACIONAL']
menores_25 = [140742, 5902, 3658, 4028, 2105, 2682, 6702, 8872, 37053, 519, 305, 2721, 3545, 2849, 3488, 3664, 3183, 6847, 1504, 1782, 2816, 641, 716, 3164, 9119, 541, 789, 1431, 481, 1108, 388, 211, 1581, 539, 7064, 1644, 811, 2008, 15227, 5591, 1802, 7790, 15183, 3959, 2094, 6053, 1805, 499, 583, 1846, 15299, 543, 673, 2007, 1011, 585, 843, 543, 140742]
de_25_a_29 = [133626, 246, 3892, 4090, 1840, 3045, 6427, 8831, 36921, 432, 329, 2532, 3293, 2593, 3515, 3658, 3065, 6723, 1328, 1661, 2874, 636, 636, 3070, 8820, 487, 725, 1184, 479, 975, 298, 165, 1459, 404, 6176, 1441, 806, 1986, 13666, 5016, 1761, 6716, 13493, 3853, 1869, 472, 1783, 475, 520, 1618, 13940, 878, 661, 2084, 1053, 544, 878, 602, 133626]
de_30_a_44 = [133083, 7279, 3457, 4291, 2103, 2723, 6291, 8952, 37273, 367, 211, 1950, 2528, 3020, 2401, 4265, 3724, 7989, 1671, 1552, 2299, 553, 553, 2259, 7259, 502, 759, 1363, 459, 1024, 302, 171, 1328, 527, 6435, 1270, 800, 1666, 13654, 5061, 2017, 6511, 12812, 3222, 1829, 655, 2610, 655, 730, 3132, 17358, 1303, 631, 2828, 1218, 557, 912, 387, 133083]
mayores_45 = [176985, 51164, 51164, 17467, 6459, 6439, 20324, 27687, 111813, 1187, 338, 6524, 8430, 11652, 7085, 14230, 13715, 27945, 5946, 4122, 5973, 1552, 2063, 7296, 21006, 1443, 2356, 4488, 1183, 2748, 929, 468, 4255, 1539, 19409, 40773, 5582, 6585, 56275, 18408, 4660, 22602, 45670, 7937, 4575, 12512, 10103, 2467, 2549, 10240, 25359, 2187, 3049, 11391, 4652, 2192, 1698, 1071, 176985]

longitud_minima = min(len(menores_25), len(de_25_a_29), len(de_30_a_44), len(mayores_45), len(ciudades))

edades_totales = [menores_25[i] + de_25_a_29[i] + de_30_a_44[i] + mayores_45[i] for i in range(longitud_minima)]
plt.figure(figsize=(10, 6))

plt.hist(edades_totales, bins=10, color='blue', alpha=0.7)

plt.xlabel('Total de Edades')
plt.ylabel('Frecuencia')
plt.title('Histograma de Distribución de Edades por Ciudad')

plt.show()