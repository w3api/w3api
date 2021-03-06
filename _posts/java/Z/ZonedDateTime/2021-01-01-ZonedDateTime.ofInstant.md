---
title: ZonedDateTime.ofInstant()
permalink: /Java/ZonedDateTime/ofInstant/
date: 2021-01-11
key: Java.Z.ZonedDateTime
category: Java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZonedDateTime.metodos valor="ofInstant" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ZonedDateTime ofInstant(Instant instant, ZoneId zone)
public static ZonedDateTime ofInstant(LocalDateTime localDateTime, ZoneOffset offset, ZoneId zone)
~~~

## Parámetros
* **ZoneOffset offset**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset offset" %}
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneId zone" %}
* **Instant instant**,  {% include w3api/param_description.html metodo=_dato parametro="Instant instant" %}
* **LocalDateTime localDateTime**,  {% include w3api/param_description.html metodo=_dato parametro="LocalDateTime localDateTime" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[ZonedDateTime](/Java/ZonedDateTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
