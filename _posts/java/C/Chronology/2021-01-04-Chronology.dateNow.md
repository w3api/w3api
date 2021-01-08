---
title: Chronology.dateNow()
permalink: Java/Chronology/dateNow
date: 2021-01-04
key: JavaJava.C.Chronology
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Chronology.metodos valor="dateNow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default ChronoLocalDate dateNow()
default ChronoLocalDate dateNow(Clock clock)
default ChronoLocalDate dateNow(ZoneId zone)
~~~

## Parámetros
* **Clock clock**,  {% include w3api/param_description.html metodo=_data parametro="Clock clock" %}
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_data parametro="ZoneId zone" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[Chronology](/Java/Chronology/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Chronology.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
