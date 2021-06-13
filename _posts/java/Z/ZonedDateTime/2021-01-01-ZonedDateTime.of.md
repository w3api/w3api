---
title: ZonedDateTime.of()
permalink: /Java/ZonedDateTime/of/
date: 2021-01-11
key: Java.Z.ZonedDateTime
category: Java
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
* **LocalDate date**,  {% include w3api/param_description.html metodo=_dato parametro="LocalDate date" %}
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneId zone" %}
* **int month**,  {% include w3api/param_description.html metodo=_dato parametro="int month" %}
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_dato parametro="int dayOfMonth" %}
* **LocalTime time**,  {% include w3api/param_description.html metodo=_dato parametro="LocalTime time" %}
* **int minute**,  {% include w3api/param_description.html metodo=_dato parametro="int minute" %}
* **int second**,  {% include w3api/param_description.html metodo=_dato parametro="int second" %}
* **int nanoOfSecond**,  {% include w3api/param_description.html metodo=_dato parametro="int nanoOfSecond" %}
* **LocalDateTime localDateTime**,  {% include w3api/param_description.html metodo=_dato parametro="LocalDateTime localDateTime" %}
* **int year**,  {% include w3api/param_description.html metodo=_dato parametro="int year" %}
* **int hour**,  {% include w3api/param_description.html metodo=_dato parametro="int hour" %}

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
