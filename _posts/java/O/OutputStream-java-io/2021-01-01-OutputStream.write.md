---
title: OutputStream.write()
permalink: Java/OutputStream-java-io/write
date: 2021-01-11
key: JavaJava.O.OutputStream-java-io
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OutputStream-java-io.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void write(byte[] b) throws IOException
public void write(byte[] b, int off, int len) throws IOException
public abstract void write(int b) throws IOException
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}
* **int b**,  {% include w3api/param_description.html metodo=_dato parametro="int b" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] b" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[OutputStream](/Java/OutputStream-java-io/)

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
