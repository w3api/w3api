---
title: JarOutputStream.JarOutputStream()
permalink: Java/JarOutputStream/JarOutputStream
date: 2021-01-04
key: JavaJava.J.JarOutputStream
category: java
tags: ['java se', 'java.util.jar', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JarOutputStream.constructores valor="JarOutputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JarOutputStream(OutputStream out) throws IOException
public JarOutputStream(OutputStream out, Manifest man) throws IOException
~~~

## Parámetros
* **Manifest man**,  {% include w3api/param_description.html metodo=_data parametro="Manifest man" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream out" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[JarOutputStream](/Java/JarOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JarOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
