---
title: ChronoZonedDateTime.format()
permalink: Java/ChronoZonedDateTime/format
date: 2021-01-04
key: JavaJava.C.ChronoZonedDateTime
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoZonedDateTime.metodos valor="format" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default String format(DateTimeFormatter formatter)
~~~

## Parámetros
* **DateTimeFormatter formatter**,  {% include w3api/param_description.html metodo=_data parametro="DateTimeFormatter formatter" %}

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
