---
title: RowFilter.numberFilter()
permalink: Java/RowFilter/numberFilter
date: 2021-01-11
key: JavaJava.R.RowFilter
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowFilter.metodos valor="numberFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <M,I> RowFilter<M,I> numberFilter(RowFilter.ComparisonType type, Number number, int... indices)
~~~

## Parámetros
* **RowFilter.ComparisonType type**,  {% include w3api/param_description.html metodo=_dato parametro="RowFilter.ComparisonType type" %}
* **Number number**,  {% include w3api/param_description.html metodo=_dato parametro="Number number" %}
* **int... indices**,  {% include w3api/param_description.html metodo=_dato parametro="int... indices" %}

## Clase Padre
[RowFilter](/Java/RowFilter/)

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
