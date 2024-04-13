---
title: MessageFormat.parse()
permalink: /Java/MessageFormat/parse/
date: 2021-01-11
key: Java.M.MessageFormat
category: Java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageFormat.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object[] parse(String source) throws ParseException
public Object[] parse(String source, ParsePosition pos)
~~~

## Parámetros
* **String source**,  {% include w3api/param_description.html metodo=_dato parametro="String source" %}
* **ParsePosition pos**,  {% include w3api/param_description.html metodo=_dato parametro="ParsePosition pos" %}

## Excepciones
[ParseException](/Java/ParseException/), [NullPointerException](/Java/NullPointerException/)

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
