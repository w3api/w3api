---
title: Formatter.format()
permalink: Java/Formatter-java-util/format
date: 2021-01-11
key: JavaJava.F.Formatter-java-util
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.Formatter-java-util.metodos valor="format" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Formatter format(String format, Object... args)
public Formatter format(Locale l, String format, Object... args)
~~~

## Parámetros
* **Locale l**,  {% include w3api/param_description.html metodo=_dato parametro="Locale l" %}
* **String format**,  {% include w3api/param_description.html metodo=_dato parametro="String format" %}
* **Object... args**,  {% include w3api/param_description.html metodo=_dato parametro="Object... args" %}

## Excepciones
[FormatterClosedException](/Java/FormatterClosedException/), [IllegalFormatException](/Java/IllegalFormatException/)

## Clase Padre
[Formatter](/Java/Formatter-java-util/)

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
