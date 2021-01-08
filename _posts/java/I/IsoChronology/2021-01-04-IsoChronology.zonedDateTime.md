---
title: IsoChronology.zonedDateTime()
permalink: Java/IsoChronology/zonedDateTime
date: 2021-01-04
key: JavaJava.I.IsoChronology
category: java
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
* **Instant instant**,  {% include w3api/param_description.html metodo=_data parametro="Instant instant" %}
* **TemporalAccessor temporal**,  {% include w3api/param_description.html metodo=_data parametro="TemporalAccessor temporal" %}
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
