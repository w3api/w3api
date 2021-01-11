---
title: Transform.toArray()
permalink: Java/Transform-javafx-scene-transform/toArray
date: 2021-01-11
key: JavaJava.T.Transform-javafx-scene-transform
category: java
tags: ['java se', 'javafx.scene.transform', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Transform-javafx-scene-transform.metodos valor="toArray" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double[] toArray(MatrixType type)
public double[] toArray(MatrixType type, double[] array)
~~~

## Parámetros
* **MatrixType type**,  {% include w3api/param_description.html metodo=_dato parametro="MatrixType type" %}
* **double[] array**,  {% include w3api/param_description.html metodo=_dato parametro="double[] array" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Transform](/Java/Transform-javafx-scene-transform/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
