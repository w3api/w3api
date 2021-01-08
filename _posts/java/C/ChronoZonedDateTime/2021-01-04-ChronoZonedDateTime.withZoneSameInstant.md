---
title: ChronoZonedDateTime.withZoneSameInstant()
permalink: Java/ChronoZonedDateTime/withZoneSameInstant
date: 2021-01-04
key: JavaJava.C.ChronoZonedDateTime
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoZonedDateTime.metodos valor="withZoneSameInstant" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ChronoZonedDateTime<D> withZoneSameInstant(ZoneId zone)
~~~

## Parámetros
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_data parametro="ZoneId zone" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[ChronoZonedDateTime](/Java/ChronoZonedDateTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ChronoZonedDateTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
