---
title: JarInputStream.read()
permalink: /Java/JarInputStream/read/
date: 2021-01-11
key: Java.J.JarInputStream
category: Java
tags: ['java se', 'java.util.jar', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JarInputStream.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int read(byte[] b, int off, int len) throws IOException
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] b" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [ZipException](/Java/ZipException/)

## Clase Padre
[JarInputStream](/Java/JarInputStream/)

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
