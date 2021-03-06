---
title: JarOutputStream.putNextEntry()
permalink: /Java/JarOutputStream/putNextEntry/
date: 2021-01-11
key: Java.J.JarOutputStream
category: Java
tags: ['java se', 'java.util.jar', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JarOutputStream.metodos valor="putNextEntry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void putNextEntry(ZipEntry ze) throws IOException
~~~

## Parámetros
* **ZipEntry ze**,  {% include w3api/param_description.html metodo=_dato parametro="ZipEntry ze" %}

## Excepciones
[IOException](/Java/IOException/), [ZipException](/Java/ZipException/)

## Clase Padre
[JarOutputStream](/Java/JarOutputStream/)

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
