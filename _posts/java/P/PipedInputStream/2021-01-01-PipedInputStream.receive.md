---
title: PipedInputStream.receive()
permalink: Java/PipedInputStream/receive
date: 2021-01-11
key: JavaJava.P.PipedInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PipedInputStream.metodos valor="receive" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void receive(int b) throws IOException
~~~

## Parámetros
* **int b**,  {% include w3api/param_description.html metodo=_dato parametro="int b" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[PipedInputStream](/Java/PipedInputStream/)

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
