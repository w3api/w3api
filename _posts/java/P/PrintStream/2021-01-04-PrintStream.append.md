---
title: PrintStream.append()
permalink: Java/PrintStream/append
date: 2021-01-04
key: JavaJava.P.PrintStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintStream.metodos valor="append" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PrintStream append(char c)
public PrintStream append(CharSequence csq)
public PrintStream append(CharSequence csq, int start, int end)
~~~

## Parámetros
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **CharSequence csq**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence csq" %}
* **int end**,  {% include w3api/param_description.html metodo=_data parametro="int end" %}
* **char c**,  {% include w3api/param_description.html metodo=_data parametro="char c" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[PrintStream](/Java/PrintStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrintStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
