---
title: CheckedOutputStream.write()
permalink: Java/CheckedOutputStream/write
date: 2021-01-04
key: JavaJava.C.CheckedOutputStream
category: java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CheckedOutputStream.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void write(byte[] b, int off, int len) throws IOException
public void write(int b) throws IOException
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_data parametro="byte[] b" %}
* **int b**,  {% include w3api/param_description.html metodo=_data parametro="int b" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[CheckedOutputStream](/Java/CheckedOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CheckedOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
