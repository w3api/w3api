---
title: ZonedDateTime.of()
permalink: Java/ZonedDateTime/of
date: 2021-01-04
key: JavaJava.Z.ZonedDateTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZonedDateTime.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ZonedDateTime of(int year, int month, int dayOfMonth, int hour, int minute, int second, int nanoOfSecond, ZoneId zone)
public static ZonedDateTime of(LocalDate date, LocalTime time, ZoneId zone)
public static ZonedDateTime of(LocalDateTime localDateTime, ZoneId zone)
~~~

## Parámetros
* **LocalTime time**,  {% include w3api/param_description.html metodo=_data parametro="LocalTime time" %}
* **int minute**,  {% include w3api/param_description.html metodo=_data parametro="int minute" %}
* **int year**,  {% include w3api/param_description.html metodo=_data parametro="int year" %}
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_data parametro="ZoneId zone" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}
* **int nanoOfSecond**,  {% include w3api/param_description.html metodo=_data parametro="int nanoOfSecond" %}
* **LocalDateTime localDateTime**,  {% include w3api/param_description.html metodo=_data parametro="LocalDateTime localDateTime" %}
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_data parametro="int dayOfMonth" %}
* **int hour**,  {% include w3api/param_description.html metodo=_data parametro="int hour" %}
* **LocalDate date**,  {% include w3api/param_description.html metodo=_data parametro="LocalDate date" %}
* **int second**,  {% include w3api/param_description.html metodo=_data parametro="int second" %}

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
{%- for _ldc in site.data.Java.Z.ZonedDateTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
