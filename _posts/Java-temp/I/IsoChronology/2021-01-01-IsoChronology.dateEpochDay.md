---
title: IsoChronology.dateEpochDay()
permalink: /Java/IsoChronology/dateEpochDay/
date: 2021-01-11
key: Java.I.IsoChronology
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IsoChronology.metodos valor="dateEpochDay" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDate dateEpochDay(long epochDay)
~~~

## Parámetros
* **long epochDay**,  {% include w3api/param_description.html metodo=_dato parametro="long epochDay" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[IsoChronology](/Java/IsoChronology/)

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
