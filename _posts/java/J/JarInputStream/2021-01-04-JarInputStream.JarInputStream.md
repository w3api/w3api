---
title: JarInputStream.JarInputStream()
permalink: Java/JarInputStream/JarInputStream
date: 2021-01-04
key: JavaJava.J.JarInputStream
category: java
tags: ['java se', 'java.util.jar', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JarInputStream.constructores valor="JarInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JarInputStream(InputStream in) throws IOException
public JarInputStream(InputStream in, boolean verify) throws IOException
~~~

## Parámetros
* **boolean verify**,  {% include w3api/param_description.html metodo=_data parametro="boolean verify" %}
* **InputStream in**,  {% include w3api/param_description.html metodo=_data parametro="InputStream in" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[JarInputStream](/Java/JarInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JarInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
