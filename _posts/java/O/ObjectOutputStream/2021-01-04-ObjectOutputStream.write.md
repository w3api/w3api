---
title: ObjectOutputStream.write()
permalink: Java/ObjectOutputStream/write
date: 2021-01-04
key: JavaJava.O.ObjectOutputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectOutputStream.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void write(byte[] buf) throws IOException
public void write(byte[] buf, int off, int len) throws IOException
public void write(int val) throws IOException
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **byte[] buf**,  {% include w3api/param_description.html metodo=_data parametro="byte[] buf" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **int val**,  {% include w3api/param_description.html metodo=_data parametro="int val" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[ObjectOutputStream](/Java/ObjectOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
