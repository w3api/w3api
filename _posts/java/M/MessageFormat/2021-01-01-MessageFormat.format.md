---
title: MessageFormat.format()
permalink: Java/MessageFormat/format
date: 2021-01-11
key: JavaJava.M.MessageFormat
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageFormat.metodos valor="format" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final StringBuffer format(Object[] arguments, StringBuffer result, FieldPosition pos)
public final StringBuffer format(Object arguments, StringBuffer result, FieldPosition pos)
public static String format(String pattern, Object... arguments)
~~~

## Parámetros
* **Object... arguments**,  {% include w3api/param_description.html metodo=_dato parametro="Object... arguments" %}
* **StringBuffer result**,  {% include w3api/param_description.html metodo=_dato parametro="StringBuffer result" %}
* **Object arguments**,  {% include w3api/param_description.html metodo=_dato parametro="Object arguments" %}
* **Object[] arguments**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] arguments" %}
* **String pattern**,  {% include w3api/param_description.html metodo=_dato parametro="String pattern" %}
* **FieldPosition pos**,  {% include w3api/param_description.html metodo=_dato parametro="FieldPosition pos" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MessageFormat](/Java/MessageFormat/)

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
