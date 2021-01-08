---
title: JarInputStream.getNextEntry()
permalink: Java/JarInputStream/getNextEntry
date: 2021-01-04
key: JavaJava.J.JarInputStream
category: java
tags: ['java se', 'java.util.jar', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JarInputStream.metodos valor="getNextEntry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ZipEntry getNextEntry() throws IOException
~~~

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/), [ZipException](/Java/ZipException/)

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
