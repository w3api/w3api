---
title: RowFilter.regexFilter()
permalink: /Java/RowFilter/regexFilter/
date: 2021-01-11
key: Java.R.RowFilter
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowFilter.metodos valor="regexFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <M,I> RowFilter<M,I> regexFilter(String regex, int... indices)
~~~

## Parámetros
* **int... indices**,  {% include w3api/param_description.html metodo=_dato parametro="int... indices" %}
* **String regex**,  {% include w3api/param_description.html metodo=_dato parametro="String regex" %}

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
