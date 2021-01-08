---
title: MessageFormat.format()
permalink: Java/MessageFormat/format
date: 2021-01-04
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
* **Object... arguments**,  {% include w3api/param_description.html metodo=_data parametro="Object... arguments" %}
* **FieldPosition pos**,  {% include w3api/param_description.html metodo=_data parametro="FieldPosition pos" %}
* **StringBuffer result**,  {% include w3api/param_description.html metodo=_data parametro="StringBuffer result" %}
* **Object arguments**,  {% include w3api/param_description.html metodo=_data parametro="Object arguments" %}
* **String pattern**,  {% include w3api/param_description.html metodo=_data parametro="String pattern" %}
* **Object[] arguments**,  {% include w3api/param_description.html metodo=_data parametro="Object[] arguments" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MessageFormat](/Java/MessageFormat/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MessageFormat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
