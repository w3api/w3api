---
title: ArrayChangeListener.onChanged()
permalink: /Java/ArrayChangeListener/onChanged/
date: 2021-01-11
key: Java.A.ArrayChangeListener
category: Java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ArrayChangeListener.metodos valor="onChanged" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void onChanged(T observableArray, boolean sizeChanged, int from, int to)
~~~

## Parámetros
* **boolean sizeChanged**,  {% include w3api/param_description.html metodo=_dato parametro="boolean sizeChanged" %}
* **int from**,  {% include w3api/param_description.html metodo=_dato parametro="int from" %}
* **T observableArray**,  {% include w3api/param_description.html metodo=_dato parametro="T observableArray" %}
* **int to**,  {% include w3api/param_description.html metodo=_dato parametro="int to" %}

## Clase Padre
[ArrayChangeListener](/Java/ArrayChangeListener/)

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
