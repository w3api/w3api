---
title: Transform.row()
permalink: Java/Transform-javafx-scene-transform/row
date: 2021-01-04
key: JavaJava.T.Transform-javafx-scene-transform
category: java
tags: ['java se', 'javafx.scene.transform', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Transform-javafx-scene-transform.metodos valor="row" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double[] row(MatrixType type, int row)
public double[] row(MatrixType type, int row, double[] array)
~~~

## Parámetros
* **MatrixType type**,  {% include w3api/param_description.html metodo=_data parametro="MatrixType type" %}
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}
* **double[] array**,  {% include w3api/param_description.html metodo=_data parametro="double[] array" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Transform](/Java/Transform-javafx-scene-transform/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.Transform-javafx-scene-transform.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
