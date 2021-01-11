---
title: LocalDate.atTime()
permalink: Java/LocalDate/atTime
date: 2021-01-11
key: JavaJava.L.LocalDate
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDate.metodos valor="atTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDateTime atTime(int hour, int minute)
public LocalDateTime atTime(int hour, int minute, int second)
public LocalDateTime atTime(int hour, int minute, int second, int nanoOfSecond)
public LocalDateTime atTime(LocalTime time)
public OffsetDateTime atTime(OffsetTime time)
~~~

## Parámetros
* **OffsetTime time**,  {% include w3api/param_description.html metodo=_dato parametro="OffsetTime time" %}
* **int second**,  {% include w3api/param_description.html metodo=_dato parametro="int second" %}
* **int minute**,  {% include w3api/param_description.html metodo=_dato parametro="int minute" %}
* **int nanoOfSecond**,  {% include w3api/param_description.html metodo=_dato parametro="int nanoOfSecond" %}
* **LocalTime time**,  {% include w3api/param_description.html metodo=_dato parametro="LocalTime time" %}
* **int hour**,  {% include w3api/param_description.html metodo=_dato parametro="int hour" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[LocalDate](/Java/LocalDate/)

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
