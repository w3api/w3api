---
title: JNLPRandomAccessFile.readFully()
permalink: Java/JNLPRandomAccessFile/readFully
date: 2021-01-04
key: JavaJava.J.JNLPRandomAccessFile
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JNLPRandomAccessFile.metodos valor="readFully" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void readFully(byte[] b) throws IOException
void readFully(byte[] b, int off, int len) throws IOException
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_data parametro="byte[] b" %}

## Excepciones
[EOFException](/Java/EOFException/), [IOException](/Java/IOException/)

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
