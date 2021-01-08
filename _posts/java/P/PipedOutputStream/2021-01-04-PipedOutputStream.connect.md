---
title: PipedOutputStream.connect()
permalink: Java/PipedOutputStream/connect
date: 2021-01-04
key: JavaJava.P.PipedOutputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PipedOutputStream.metodos valor="connect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void connect(PipedInputStream snk) throws IOException
~~~

## Parámetros
* **PipedInputStream snk**,  {% include w3api/param_description.html metodo=_data parametro="PipedInputStream snk" %}

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
{%- for _ldc in site.data.Java.P.PipedOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
