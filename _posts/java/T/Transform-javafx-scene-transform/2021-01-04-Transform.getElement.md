---
title: Transform.getElement()
permalink: Java/Transform-javafx-scene-transform/getElement
date: 2021-01-04
key: JavaJava.T.Transform-javafx-scene-transform
category: java
tags: ['java se', 'javafx.scene.transform', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Transform-javafx-scene-transform.metodos valor="getElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double getElement(MatrixType type, int row, int column)
~~~

## Parámetros
* **int column**,  {% include w3api/param_description.html metodo=_data parametro="int column" %}
* **MatrixType type**,  {% include w3api/param_description.html metodo=_data parametro="MatrixType type" %}
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}

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
