---
title: YearMonth.withMonth()
permalink: /Java/YearMonth/withMonth/
date: 2021-01-11
key: Java.Y.YearMonth
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Y.YearMonth.metodos valor="withMonth" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public YearMonth withMonth(int month)
~~~

## Parámetros
* **int month**,  {% include w3api/param_description.html metodo=_dato parametro="int month" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[YearMonth](/Java/YearMonth/)

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
