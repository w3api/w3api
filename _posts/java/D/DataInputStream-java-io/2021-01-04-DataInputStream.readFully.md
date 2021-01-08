---
title: DataInputStream.readFully()
permalink: Java/DataInputStream-java-io/readFully
date: 2021-01-04
key: JavaJava.D.DataInputStream-java-io
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataInputStream-java-io.metodos valor="readFully" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void readFully(byte[] b) throws IOException
public final void readFully(byte[] b, int off, int len) throws IOException
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_data parametro="byte[] b" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [EOFException](/Java/EOFException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[DataInputStream](/Java/DataInputStream-java-io/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataInputStream-java-io.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
