---
title: LocalDate.withDayOfMonth()
permalink: /Java/LocalDate/withDayOfMonth/
date: 2021-01-11
key: Java.L.LocalDate
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDate.metodos valor="withDayOfMonth" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDate withDayOfMonth(int dayOfMonth)
~~~

## Parámetros
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_dato parametro="int dayOfMonth" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[LocalDate](/Java/LocalDate/)

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
