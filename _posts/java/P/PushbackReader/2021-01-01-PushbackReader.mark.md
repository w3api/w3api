---
title: PushbackReader.mark()
permalink: /Java/PushbackReader/mark/
date: 2021-01-11
key: Java.P.PushbackReader
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PushbackReader.metodos valor="mark" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void mark(int readAheadLimit) throws IOException
~~~

## Parámetros
* **int readAheadLimit**,  {% include w3api/param_description.html metodo=_dato parametro="int readAheadLimit" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[PushbackReader](/Java/PushbackReader/)

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
