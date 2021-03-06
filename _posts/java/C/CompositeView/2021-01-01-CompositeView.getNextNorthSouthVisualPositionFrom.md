---
title: CompositeView.getNextNorthSouthVisualPositionFrom()
permalink: /Java/CompositeView/getNextNorthSouthVisualPositionFrom/
date: 2021-01-11
key: Java.C.CompositeView
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompositeView.metodos valor="getNextNorthSouthVisualPositionFrom" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected int getNextNorthSouthVisualPositionFrom(int pos, Position.Bias b, Shape a, int direction, Position.Bias[] biasRet) throws BadLocationException
~~~

## Parámetros
* **Shape a**,  {% include w3api/param_description.html metodo=_dato parametro="Shape a" %}
* **Position.Bias[] biasRet**,  {% include w3api/param_description.html metodo=_dato parametro="Position.Bias[] biasRet" %}
* **int direction**,  {% include w3api/param_description.html metodo=_dato parametro="int direction" %}
* **int pos**,  {% include w3api/param_description.html metodo=_dato parametro="int pos" %}
* **Position.Bias b**,  {% include w3api/param_description.html metodo=_dato parametro="Position.Bias b" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CompositeView](/Java/CompositeView/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
