---
title: LocalDate.ofEpochDay()
permalink: /Java/LocalDate/ofEpochDay/
date: 2021-01-11
key: Java.L.LocalDate
category: Java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDate.metodos valor="ofEpochDay" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static LocalDate ofEpochDay(long epochDay)
~~~

## Parámetros
* **long epochDay**,  {% include w3api/param_description.html metodo=_dato parametro="long epochDay" %}

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
