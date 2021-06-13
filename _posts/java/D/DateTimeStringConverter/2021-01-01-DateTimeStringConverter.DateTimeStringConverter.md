---
title: DateTimeStringConverter.DateTimeStringConverter()
permalink: /Java/DateTimeStringConverter/DateTimeStringConverter/
date: 2021-01-11
key: Java.D.DateTimeStringConverter
category: Java
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
* **int dateStyle**,  {% include w3api/param_description.html metodo=_dato parametro="int dateStyle" %}
* **int timeStyle**,  {% include w3api/param_description.html metodo=_dato parametro="int timeStyle" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}
* **String pattern**,  {% include w3api/param_description.html metodo=_dato parametro="String pattern" %}
* **DateFormat dateFormat**,  {% include w3api/param_description.html metodo=_dato parametro="DateFormat dateFormat" %}

## Clase Padre
[DateTimeStringConverter](/Java/DateTimeStringConverter/)

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
