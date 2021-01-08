---
title: ChronoLocalDateTime.atZone()
permalink: Java/ChronoLocalDateTime/atZone
date: 2021-01-04
key: JavaJava.C.ChronoLocalDateTime
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoLocalDateTime.metodos valor="atZone" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ChronoZonedDateTime<D> atZone(ZoneId zone)
~~~

## Parámetros
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_data parametro="ZoneId zone" %}

## Clase Padre
[ChronoLocalDateTime](/Java/ChronoLocalDateTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ChronoLocalDateTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
