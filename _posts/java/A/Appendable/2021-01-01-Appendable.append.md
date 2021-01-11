---
title: Appendable.append()
permalink: Java/Appendable/append
date: 2021-01-11
key: JavaJava.A.Appendable
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Appendable.metodos valor="append" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Appendable append(char c) throws IOException
Appendable append(CharSequence csq) throws IOException
Appendable append(CharSequence csq, int start, int end) throws IOException
~~~

## Parámetros
* **int end**,  {% include w3api/param_description.html metodo=_dato parametro="int end" %}
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **CharSequence csq**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence csq" %}
* **char c**,  {% include w3api/param_description.html metodo=_dato parametro="char c" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IOException](/Java/IOException/)

## Clase Padre
[Appendable](/Java/Appendable/)

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
