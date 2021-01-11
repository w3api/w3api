---
title: DateFormat.getDateInstance()
permalink: Java/DateFormat/getDateInstance
date: 2021-01-11
key: JavaJava.D.DateFormat
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateFormat.metodos valor="getDateInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static DateFormat getDateInstance()
static DateFormat getDateInstance(int style)
static DateFormat getDateInstance(int style, Locale aLocale)
~~~

## Parámetros
* **Locale aLocale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale aLocale" %}
* **int style**,  {% include w3api/param_description.html metodo=_dato parametro="int style" %}

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
