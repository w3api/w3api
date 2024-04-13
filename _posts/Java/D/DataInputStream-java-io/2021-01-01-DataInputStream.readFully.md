---
title: DataInputStream.readFully()
permalink: /Java/DataInputStream-java-io/readFully/
date: 2021-01-11
key: Java.D.DataInputStream-java-io
category: Java
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
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] b" %}

## Excepciones
[IOException](/Java/IOException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [EOFException](/Java/EOFException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DataInputStream](/Java/DataInputStream-java-io/)

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
