---
title: JarURLConnection.getJarFile()
permalink: /Java/JarURLConnection/getJarFile/
date: 2021-01-11
key: Java.J.JarURLConnection
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JarURLConnection.metodos valor="getJarFile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract JarFile getJarFile() throws IOException
~~~

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[JarURLConnection](/Java/JarURLConnection/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
