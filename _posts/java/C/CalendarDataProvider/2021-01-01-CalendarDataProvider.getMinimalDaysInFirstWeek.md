---
title: CalendarDataProvider.getMinimalDaysInFirstWeek()
permalink: /Java/CalendarDataProvider/getMinimalDaysInFirstWeek/
date: 2021-01-11
key: Java.C.CalendarDataProvider
category: Java
tags: ['java se', 'java.util.spi', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CalendarDataProvider.metodos valor="getMinimalDaysInFirstWeek" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int getMinimalDaysInFirstWeek(Locale locale)
~~~

## Parámetros
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CalendarDataProvider](/Java/CalendarDataProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
