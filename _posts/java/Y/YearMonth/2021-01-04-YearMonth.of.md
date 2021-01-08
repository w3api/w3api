---
title: YearMonth.of()
permalink: Java/YearMonth/of
date: 2021-01-04
key: JavaJava.Y.YearMonth
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Y.YearMonth.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static YearMonth of(int year, int month)
public static YearMonth of(int year, Month month)
~~~

## Parámetros
* **int year**,  {% include w3api/param_description.html metodo=_data parametro="int year" %}
* **Month month**,  {% include w3api/param_description.html metodo=_data parametro="Month month" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}

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
{%- for _ldc in site.data.Java.Y.YearMonth.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
