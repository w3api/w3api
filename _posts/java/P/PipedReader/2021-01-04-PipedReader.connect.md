---
title: PipedReader.connect()
permalink: Java/PipedReader/connect
date: 2021-01-04
key: JavaJava.P.PipedReader
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PipedReader.metodos valor="connect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void connect(PipedWriter src) throws IOException
~~~

## Parámetros
* **PipedWriter src**,  {% include w3api/param_description.html metodo=_data parametro="PipedWriter src" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[PipedReader](/Java/PipedReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PipedReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
