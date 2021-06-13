---
title: LocalDateTime.of()
permalink: /Java/LocalDateTime/of/
date: 2021-01-11
key: Java.L.LocalDateTime
category: Java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDateTime.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static LocalDateTime of(int year, int month, int dayOfMonth, int hour, int minute)
public static LocalDateTime of(int year, int month, int dayOfMonth, int hour, int minute, int second)
public static LocalDateTime of(int year, int month, int dayOfMonth, int hour, int minute, int second, int nanoOfSecond)
public static LocalDateTime of(int year, Month month, int dayOfMonth, int hour, int minute)
public static LocalDateTime of(int year, Month month, int dayOfMonth, int hour, int minute, int second)
public static LocalDateTime of(int year, Month month, int dayOfMonth, int hour, int minute, int second, int nanoOfSecond)
public static LocalDateTime of(LocalDate date, LocalTime time)
~~~

## Parámetros
* **Month month**,  {% include w3api/param_description.html metodo=_dato parametro="Month month" %}
* **LocalDate date**,  {% include w3api/param_description.html metodo=_dato parametro="LocalDate date" %}
* **int month**,  {% include w3api/param_description.html metodo=_dato parametro="int month" %}
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_dato parametro="int dayOfMonth" %}
* **LocalTime time**,  {% include w3api/param_description.html metodo=_dato parametro="LocalTime time" %}
* **int minute**,  {% include w3api/param_description.html metodo=_dato parametro="int minute" %}
* **int second**,  {% include w3api/param_description.html metodo=_dato parametro="int second" %}
* **int nanoOfSecond**,  {% include w3api/param_description.html metodo=_dato parametro="int nanoOfSecond" %}
* **int year**,  {% include w3api/param_description.html metodo=_dato parametro="int year" %}
* **int hour**,  {% include w3api/param_description.html metodo=_dato parametro="int hour" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[LocalDateTime](/Java/LocalDateTime/)

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
