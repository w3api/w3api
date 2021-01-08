---
title: PushbackReader.PushbackReader()
permalink: Java/PushbackReader/PushbackReader
date: 2021-01-04
key: JavaJava.P.PushbackReader
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PushbackReader.constructores valor="PushbackReader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PushbackReader(Reader in)
public PushbackReader(Reader in, int size)
~~~

## Parámetros
* **Reader in**,  {% include w3api/param_description.html metodo=_data parametro="Reader in" %}
* **int size**,  {% include w3api/param_description.html metodo=_data parametro="int size" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PushbackReader](/Java/PushbackReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PushbackReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
