---
title: PipedInputStream.connect()
permalink: /Java/PipedInputStream/connect/
date: 2021-01-11
key: Java.P.PipedInputStream
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PipedInputStream.metodos valor="connect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void connect(PipedOutputStream src) throws IOException
~~~

## Parámetros
* **PipedOutputStream src**,  {% include w3api/param_description.html metodo=_dato parametro="PipedOutputStream src" %}

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
