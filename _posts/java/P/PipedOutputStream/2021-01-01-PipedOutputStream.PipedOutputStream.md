---
title: PipedOutputStream.PipedOutputStream()
permalink: Java/PipedOutputStream/PipedOutputStream
date: 2021-01-11
key: JavaJava.P.PipedOutputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PipedOutputStream.constructores valor="PipedOutputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PipedOutputStream()
public PipedOutputStream(PipedInputStream snk) throws IOException
~~~

## Parámetros
* **PipedInputStream snk**,  {% include w3api/param_description.html metodo=_dato parametro="PipedInputStream snk" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[PipedOutputStream](/Java/PipedOutputStream/)

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
