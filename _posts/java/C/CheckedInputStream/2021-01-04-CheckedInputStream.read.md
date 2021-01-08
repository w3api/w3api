---
title: CheckedInputStream.read()
permalink: Java/CheckedInputStream/read
date: 2021-01-04
key: JavaJava.C.CheckedInputStream
category: java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CheckedInputStream.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int read() throws IOException
public int read(byte[] buf, int off, int len) throws IOException
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **byte[] buf**,  {% include w3api/param_description.html metodo=_data parametro="byte[] buf" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[CheckedInputStream](/Java/CheckedInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CheckedInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
