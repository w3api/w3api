---
title: CipherOutputStream.write()
permalink: Java/CipherOutputStream/write
date: 2021-01-04
key: JavaJava.C.CipherOutputStream
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CipherOutputStream.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void write(byte[] b) throws IOException
public void write(byte[] b, int off, int len) throws IOException
public void write(int b) throws IOException
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_data parametro="byte[] b" %}
* **int b**,  {% include w3api/param_description.html metodo=_data parametro="int b" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[CipherOutputStream](/Java/CipherOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CipherOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
