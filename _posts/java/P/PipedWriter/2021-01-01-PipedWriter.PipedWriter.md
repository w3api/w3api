---
title: PipedWriter.PipedWriter()
permalink: /Java/PipedWriter/PipedWriter/
date: 2021-01-11
key: Java.P.PipedWriter
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PipedWriter.constructores valor="PipedWriter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PipedWriter()
public PipedWriter(PipedReader snk) throws IOException
~~~

## Parámetros
* **PipedReader snk**,  {% include w3api/param_description.html metodo=_dato parametro="PipedReader snk" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[PipedWriter](/Java/PipedWriter/)

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
