---
title: IsoChronology.dateNow()
permalink: Java/IsoChronology/dateNow
date: 2021-01-04
key: JavaJava.I.IsoChronology
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IsoChronology.metodos valor="dateNow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDate dateNow()
public LocalDate dateNow(Clock clock)
public LocalDate dateNow(ZoneId zone)
~~~

## Parámetros
* **Clock clock**,  {% include w3api/param_description.html metodo=_data parametro="Clock clock" %}
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_data parametro="ZoneId zone" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[IsoChronology](/Java/IsoChronology/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IsoChronology.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
