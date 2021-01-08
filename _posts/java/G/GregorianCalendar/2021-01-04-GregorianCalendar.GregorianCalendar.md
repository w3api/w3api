---
title: GregorianCalendar.GregorianCalendar()
permalink: Java/GregorianCalendar/GregorianCalendar
date: 2021-01-04
key: JavaJava.G.GregorianCalendar
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GregorianCalendar.constructores valor="GregorianCalendar" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GregorianCalendar()
public GregorianCalendar(int year, int month, int dayOfMonth)
public GregorianCalendar(int year, int month, int dayOfMonth, int hourOfDay, int minute)
public GregorianCalendar(int year, int month, int dayOfMonth, int hourOfDay, int minute, int second)
public GregorianCalendar(Locale aLocale)
public GregorianCalendar(TimeZone zone)
public GregorianCalendar(TimeZone zone, Locale aLocale)
~~~

## Parámetros
* **Locale aLocale**,  {% include w3api/param_description.html metodo=_data parametro="Locale aLocale" %}
* **int minute**,  {% include w3api/param_description.html metodo=_data parametro="int minute" %}
* **int year**,  {% include w3api/param_description.html metodo=_data parametro="int year" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}
* **TimeZone zone**,  {% include w3api/param_description.html metodo=_data parametro="TimeZone zone" %}
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_data parametro="int dayOfMonth" %}
* **int hourOfDay**,  {% include w3api/param_description.html metodo=_data parametro="int hourOfDay" %}
* **int second**,  {% include w3api/param_description.html metodo=_data parametro="int second" %}

## Clase Padre
[GregorianCalendar](/Java/GregorianCalendar/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GregorianCalendar.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
