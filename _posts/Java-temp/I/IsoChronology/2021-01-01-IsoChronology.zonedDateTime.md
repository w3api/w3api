---
title: IsoChronology.zonedDateTime()
permalink: /Java/IsoChronology/zonedDateTime/
date: 2021-01-11
key: Java.I.IsoChronology
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IsoChronology.metodos valor="zonedDateTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ZonedDateTime zonedDateTime(Instant instant, ZoneId zone)
public ZonedDateTime zonedDateTime(TemporalAccessor temporal)
~~~

## Parámetros
* **TemporalAccessor temporal**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAccessor temporal" %}
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneId zone" %}
* **Instant instant**,  {% include w3api/param_description.html metodo=_dato parametro="Instant instant" %}

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
