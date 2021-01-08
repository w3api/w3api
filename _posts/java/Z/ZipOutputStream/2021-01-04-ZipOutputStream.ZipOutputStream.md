---
title: ZipOutputStream.ZipOutputStream()
permalink: Java/ZipOutputStream/ZipOutputStream
date: 2021-01-04
key: JavaJava.Z.ZipOutputStream
category: java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZipOutputStream.constructores valor="ZipOutputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ZipOutputStream(OutputStream out)
public ZipOutputStream(OutputStream out, Charset charset)
~~~

## Parámetros
* **Charset charset**,  {% include w3api/param_description.html metodo=_data parametro="Charset charset" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream out" %}

## Clase Padre
[ZipOutputStream](/Java/ZipOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.Z.ZipOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
