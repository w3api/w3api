---
title: ZipInputStream.ZipInputStream()
permalink: Java/ZipInputStream/ZipInputStream
date: 2021-01-04
key: JavaJava.Z.ZipInputStream
category: java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZipInputStream.constructores valor="ZipInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ZipInputStream(InputStream in)
public ZipInputStream(InputStream in, Charset charset)
~~~

## Parámetros
* **Charset charset**,  {% include w3api/param_description.html metodo=_data parametro="Charset charset" %}
* **InputStream in**,  {% include w3api/param_description.html metodo=_data parametro="InputStream in" %}

## Clase Padre
[ZipInputStream](/Java/ZipInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.Z.ZipInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
