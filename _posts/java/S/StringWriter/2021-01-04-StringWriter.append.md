---
title: StringWriter.append()
permalink: Java/StringWriter/append
date: 2021-01-04
key: JavaJava.S.StringWriter
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringWriter.metodos valor="append" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StringWriter append(char c)
public StringWriter append(CharSequence csq)
public StringWriter append(CharSequence csq, int start, int end)
~~~

## Parámetros
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **CharSequence csq**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence csq" %}
* **int end**,  {% include w3api/param_description.html metodo=_data parametro="int end" %}
* **char c**,  {% include w3api/param_description.html metodo=_data parametro="char c" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[StringWriter](/Java/StringWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StringWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
