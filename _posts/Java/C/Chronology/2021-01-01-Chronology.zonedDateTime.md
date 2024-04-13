---
title: Chronology.zonedDateTime()
permalink: /Java/Chronology/zonedDateTime/
date: 2021-01-11
key: Java.C.Chronology
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Chronology.metodos valor="zonedDateTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default ChronoZonedDateTime<? extends ChronoLocalDate> zonedDateTime(Instant instant, ZoneId zone)
default ChronoZonedDateTime<? extends ChronoLocalDate> zonedDateTime(TemporalAccessor temporal)
~~~

## Parámetros
* **TemporalAccessor temporal**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAccessor temporal" %}
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneId zone" %}
* **Instant instant**,  {% include w3api/param_description.html metodo=_dato parametro="Instant instant" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[Chronology](/Java/Chronology/)

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
