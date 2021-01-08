---
title: OffsetDateTime.of()
permalink: Java/OffsetDateTime/of
date: 2021-01-04
key: JavaJava.O.OffsetDateTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OffsetDateTime.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static OffsetDateTime of(int year, int month, int dayOfMonth, int hour, int minute, int second, int nanoOfSecond, ZoneOffset offset)
public static OffsetDateTime of(LocalDate date, LocalTime time, ZoneOffset offset)
public static OffsetDateTime of(LocalDateTime dateTime, ZoneOffset offset)
~~~

## Parámetros
* **LocalTime time**,  {% include w3api/param_description.html metodo=_data parametro="LocalTime time" %}
* **LocalDateTime dateTime**,  {% include w3api/param_description.html metodo=_data parametro="LocalDateTime dateTime" %}
* **int minute**,  {% include w3api/param_description.html metodo=_data parametro="int minute" %}
* **int year**,  {% include w3api/param_description.html metodo=_data parametro="int year" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}
* **ZoneOffset offset**,  {% include w3api/param_description.html metodo=_data parametro="ZoneOffset offset" %}
* **int nanoOfSecond**,  {% include w3api/param_description.html metodo=_data parametro="int nanoOfSecond" %}
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_data parametro="int dayOfMonth" %}
* **int hour**,  {% include w3api/param_description.html metodo=_data parametro="int hour" %}
* **LocalDate date**,  {% include w3api/param_description.html metodo=_data parametro="LocalDate date" %}
* **int second**,  {% include w3api/param_description.html metodo=_data parametro="int second" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[OffsetDateTime](/Java/OffsetDateTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OffsetDateTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
