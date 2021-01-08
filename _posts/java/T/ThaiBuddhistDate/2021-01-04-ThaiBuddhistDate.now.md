---
title: ThaiBuddhistDate.now()
permalink: Java/ThaiBuddhistDate/now
date: 2021-01-04
key: JavaJava.T.ThaiBuddhistDate
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThaiBuddhistDate.metodos valor="now" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ThaiBuddhistDate now()
public static ThaiBuddhistDate now(Clock clock)
public static ThaiBuddhistDate now(ZoneId zone)
~~~

## Parámetros
* **Clock clock**,  {% include w3api/param_description.html metodo=_data parametro="Clock clock" %}
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_data parametro="ZoneId zone" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[ThaiBuddhistDate](/Java/ThaiBuddhistDate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThaiBuddhistDate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
