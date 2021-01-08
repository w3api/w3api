---
title: DateStringConverter.DateStringConverter()
permalink: Java/DateStringConverter/DateStringConverter
date: 2021-01-04
key: JavaJava.D.DateStringConverter
category: java
tags: ['java se', 'javafx.util.converter', 'javafx.base', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateStringConverter.constructores valor="DateStringConverter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DateStringConverter()
public DateStringConverter(int dateStyle)
public DateStringConverter(String pattern)
public DateStringConverter(DateFormat dateFormat)
public DateStringConverter(Locale locale)
public DateStringConverter(Locale locale, int dateStyle)
public DateStringConverter(Locale locale, String pattern)
~~~

## Parámetros
* **String pattern**,  {% include w3api/param_description.html metodo=_data parametro="String pattern" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_data parametro="Locale locale" %}
* **DateFormat dateFormat**,  {% include w3api/param_description.html metodo=_data parametro="DateFormat dateFormat" %}
* **int dateStyle**,  {% include w3api/param_description.html metodo=_data parametro="int dateStyle" %}

## Clase Padre
[DateStringConverter](/Java/DateStringConverter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DateStringConverter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
