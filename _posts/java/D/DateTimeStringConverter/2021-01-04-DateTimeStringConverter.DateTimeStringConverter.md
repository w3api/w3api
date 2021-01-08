---
title: DateTimeStringConverter.DateTimeStringConverter()
permalink: Java/DateTimeStringConverter/DateTimeStringConverter
date: 2021-01-04
key: JavaJava.D.DateTimeStringConverter
category: java
tags: ['java se', 'javafx.util.converter', 'javafx.base', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeStringConverter.constructores valor="DateTimeStringConverter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DateTimeStringConverter()
public DateTimeStringConverter(int dateStyle, int timeStyle)
public DateTimeStringConverter(String pattern)
public DateTimeStringConverter(DateFormat dateFormat)
public DateTimeStringConverter(Locale locale)
public DateTimeStringConverter(Locale locale, int dateStyle, int timeStyle)
public DateTimeStringConverter(Locale locale, String pattern)
~~~

## Parámetros
* **DateFormat dateFormat**,  {% include w3api/param_description.html metodo=_data parametro="DateFormat dateFormat" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_data parametro="Locale locale" %}
* **int timeStyle**,  {% include w3api/param_description.html metodo=_data parametro="int timeStyle" %}
* **String pattern**,  {% include w3api/param_description.html metodo=_data parametro="String pattern" %}
* **int dateStyle**,  {% include w3api/param_description.html metodo=_data parametro="int dateStyle" %}

## Clase Padre
[DateTimeStringConverter](/Java/DateTimeStringConverter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DateTimeStringConverter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
