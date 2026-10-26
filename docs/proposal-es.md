# Propuesta de proyecto

**Estado:** Borrador.

**Fecha:** 28 de octubre de 2026.

## Título

Aprendizaje de representaciones armónicas mediante redes neuronales sobre grafos basadas en el Tonnetz: predicción de acordes y explicabilidad

## Contexto y motivación

El Tonnetz organiza las relaciones armónicas entre notas y acordes mediante una estructura que puede representarse como un grafo [1]. Esta estructura permite incorporar conocimiento musical al aprendizaje automático.

## Objetivo

El proyecto evaluará qué aporta el Tonnetz a la predicción del siguiente acorde de un fragmento musical y estudiará la calidad de las explicaciones del modelo.

## Metodología propuesta

Se trabajará con datos que describan las notas e indiquen el acorde de cada momento. El conjunto de datos y los acordes incluidos están por concretar; se revisarán la fiabilidad de la información y la licencia de los datos.

Una red neuronal sobre grafos (GNN) procesará las notas de cada momento sobre un grafo fijo del Tonnetz, sin distinguir octavas ni inversiones. Una GRU, un modelo de secuencias, utilizará esas representaciones en orden para predecir el siguiente acorde. No se indicará al modelo la tonalidad de la pieza.

La comparación incluirá una GRU sin procesamiento de grafos y una variante del modelo propuesto sin intercambio de información entre nodos. Todos recibirán las mismas características musicales y se entrenarán en condiciones comparables. Las piezas de evaluación serán distintas de las utilizadas para entrenar.

## Evaluación

Se considerará un acierto que coincidan la nota fundamental y el tipo de acorde con la referencia. Se medirán la proporción de aciertos, el acierto entre las tres primeras opciones y la pérdida logarítmica. La coincidencia entre las notas de ambos acordes servirá como diagnóstico adicional de los errores.

Las explicaciones se evaluarán según su fidelidad al comportamiento del modelo, su estabilidad ante cambios leves y su complejidad, entendida como el número de elementos destacados. GraphFramEx y Quantus servirán como referencia [2, 3].

## Resultados esperados

Se entregará código reproducible para preparar los datos, entrenar y evaluar los modelos, junto con un informe de resultados y visualizaciones de las explicaciones.

## Referencias

[1] Catanzaro, M. J. *Generalized Tonnetze*. Journal of Mathematics and Music, 2011. arXiv:1612.03519.

[2] Amara, K. et al. *GraphFramEx: Towards Systematic Evaluation of Explainability Methods for Graph Neural Networks*. Learning on Graphs, 2022. arXiv:2206.09677.

[3] Hedström, A. et al. *Quantus: An Explainable AI Toolkit for Responsible Evaluation of Neural Network Explanations and Beyond*. Journal of Machine Learning Research, 24, 2023. arXiv:2202.06861.
