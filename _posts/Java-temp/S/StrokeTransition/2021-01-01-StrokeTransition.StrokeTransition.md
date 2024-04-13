---
title: StrokeTransition.StrokeTransition()
permalink: /Java/StrokeTransition/StrokeTransition/
date: 2021-01-11
key: Java.S.StrokeTransition
category: Java
tags: ['java se', 'javafx.animation', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StrokeTransition.constructores valor="StrokeTransition" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StrokeTransition()
public StrokeTransition(Duration duration)
public StrokeTransition(Duration duration, Color fromValue, Color toValue)
public StrokeTransition(Duration duration, Shape shape)
public StrokeTransition(Duration duration, Shape shape, Color fromValue, Color toValue)
~~~

## Parámetros
* **Shape shape**,  {% include w3api/param_description.html metodo=_dato parametro="Shape shape" %}
* **Color toValue**,  {% include w3api/param_description.html metodo=_dato parametro="Color toValue" %}
* **Duration duration**,  {% include w3api/param_description.html metodo=_dato parametro="Duration duration" %}
* **Color fromValue**,  {% include w3api/param_description.html metodo=_dato parametro="Color fromValue" %}

## Clase Padre
[StrokeTransition](/Java/StrokeTransition/)

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
