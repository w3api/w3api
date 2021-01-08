---
title: LocalDate.of()
permalink: Java/LocalDate/of
date: 2021-01-04
key: JavaJava.L.LocalDate
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDate.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static LocalDate of(int year, int month, int dayOfMonth)
public static LocalDate of(int year, Month month, int dayOfMonth)
~~~

## Parámetros
* **int year**,  {% include w3api/param_description.html metodo=_data parametro="int year" %}
* **Month month**,  {% include w3api/param_description.html metodo=_data parametro="Month month" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_data parametro="int dayOfMonth" %}

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
{%- for _ldc in site.data.Java.L.LocalDate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
