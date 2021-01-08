---
title: Formatter.format()
permalink: Java/Formatter-java-util/format
date: 2021-01-04
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
* **String format**,  {% include w3api/param_description.html metodo=_data parametro="String format" %}
* **Locale l**,  {% include w3api/param_description.html metodo=_data parametro="Locale l" %}
* **Object... args**,  {% include w3api/param_description.html metodo=_data parametro="Object... args" %}

## Excepciones
[IllegalFormatException](/Java/IllegalFormatException/), [FormatterClosedException](/Java/FormatterClosedException/)

## Clase Padre
[Formatter](/Java/Formatter-java-util/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.Formatter-java-util.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
