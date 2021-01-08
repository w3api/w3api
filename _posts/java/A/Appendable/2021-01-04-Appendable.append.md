---
title: Appendable.append()
permalink: Java/Appendable/append
date: 2021-01-04
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
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **CharSequence csq**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence csq" %}
* **int end**,  {% include w3api/param_description.html metodo=_data parametro="int end" %}
* **char c**,  {% include w3api/param_description.html metodo=_data parametro="char c" %}

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
{%- for _ldc in site.data.Java.A.Appendable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
