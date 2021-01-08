---
title: ArrayChangeListener.onChanged()
permalink: Java/ArrayChangeListener/onChanged
date: 2021-01-04
key: JavaJava.A.ArrayChangeListener
category: java
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
* **boolean sizeChanged**,  {% include w3api/param_description.html metodo=_data parametro="boolean sizeChanged" %}
* **int from**,  {% include w3api/param_description.html metodo=_data parametro="int from" %}
* **T observableArray**,  {% include w3api/param_description.html metodo=_data parametro="T observableArray" %}
* **int to**,  {% include w3api/param_description.html metodo=_data parametro="int to" %}

## Clase Padre
[ArrayChangeListener](/Java/ArrayChangeListener/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.ArrayChangeListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
