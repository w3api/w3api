---
title: DateFormat.getDateTimeInstance()
permalink: Java/DateFormat/getDateTimeInstance
date: 2021-01-11
key: JavaJava.D.DateFormat
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateFormat.metodos valor="getDateTimeInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static DateFormat getDateTimeInstance()
static DateFormat getDateTimeInstance(int dateStyle, int timeStyle)
static DateFormat getDateTimeInstance(int dateStyle, int timeStyle, Locale aLocale)
~~~

## Parámetros
* **Locale aLocale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale aLocale" %}
* **int dateStyle**,  {% include w3api/param_description.html metodo=_dato parametro="int dateStyle" %}
* **int timeStyle**,  {% include w3api/param_description.html metodo=_dato parametro="int timeStyle" %}

## Clase Padre
[DateFormat](/Java/DateFormat/)

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
