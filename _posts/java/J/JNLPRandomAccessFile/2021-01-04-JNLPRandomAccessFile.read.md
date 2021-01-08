---
title: JNLPRandomAccessFile.read()
permalink: Java/JNLPRandomAccessFile/read
date: 2021-01-04
key: JavaJava.J.JNLPRandomAccessFile
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JNLPRandomAccessFile.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int read() throws IOException
int read(byte[] b) throws IOException
int read(byte[] b, int off, int len) throws IOException
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_data parametro="byte[] b" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[JNLPRandomAccessFile](/Java/JNLPRandomAccessFile/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JNLPRandomAccessFile.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
