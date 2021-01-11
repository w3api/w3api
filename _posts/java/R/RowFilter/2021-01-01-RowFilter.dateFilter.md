---
title: RowFilter.dateFilter()
permalink: Java/RowFilter/dateFilter
date: 2021-01-11
key: JavaJava.R.RowFilter
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowFilter.metodos valor="dateFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <M,I> RowFilter<M,I> dateFilter(RowFilter.ComparisonType type, Date date, int... indices)
~~~

## Parámetros
* **RowFilter.ComparisonType type**,  {% include w3api/param_description.html metodo=_dato parametro="RowFilter.ComparisonType type" %}
* **Date date**,  {% include w3api/param_description.html metodo=_dato parametro="Date date" %}
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
