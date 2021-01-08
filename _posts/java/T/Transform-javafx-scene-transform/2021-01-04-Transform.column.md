---
title: Transform.column()
permalink: Java/Transform-javafx-scene-transform/column
date: 2021-01-04
key: JavaJava.T.Transform-javafx-scene-transform
category: java
tags: ['java se', 'javafx.scene.transform', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Transform-javafx-scene-transform.metodos valor="column" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double[] column(MatrixType type, int column)
public double[] column(MatrixType type, int column, double[] array)
~~~

## Parámetros
* **MatrixType type**,  {% include w3api/param_description.html metodo=_data parametro="MatrixType type" %}
* **int column**,  {% include w3api/param_description.html metodo=_data parametro="int column" %}
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
