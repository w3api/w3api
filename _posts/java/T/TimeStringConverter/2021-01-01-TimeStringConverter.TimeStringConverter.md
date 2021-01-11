---
title: TimeStringConverter.TimeStringConverter()
permalink: Java/TimeStringConverter/TimeStringConverter
date: 2021-01-11
key: JavaJava.T.TimeStringConverter
category: java
tags: ['java se', 'javafx.util.converter', 'javafx.base', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TimeStringConverter.constructores valor="TimeStringConverter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TimeStringConverter()
public TimeStringConverter(int timeStyle)
public TimeStringConverter(String pattern)
public TimeStringConverter(DateFormat dateFormat)
public TimeStringConverter(Locale locale)
public TimeStringConverter(Locale locale, int timeStyle)
public TimeStringConverter(Locale locale, String pattern)
~~~

## Parámetros
* **DateFormat dateFormat**,  {% include w3api/param_description.html metodo=_dato parametro="DateFormat dateFormat" %}
* **int timeStyle**,  {% include w3api/param_description.html metodo=_dato parametro="int timeStyle" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}
* **String pattern**,  {% include w3api/param_description.html metodo=_dato parametro="String pattern" %}

## Clase Padre
[TimeStringConverter](/Java/TimeStringConverter/)

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
