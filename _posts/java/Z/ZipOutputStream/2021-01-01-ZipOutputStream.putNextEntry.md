---
title: ZipOutputStream.putNextEntry()
permalink: Java/ZipOutputStream/putNextEntry
date: 2021-01-11
key: JavaJava.Z.ZipOutputStream
category: java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZipOutputStream.metodos valor="putNextEntry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void putNextEntry(ZipEntry e) throws IOException
~~~

## Parámetros
* **ZipEntry e**,  {% include w3api/param_description.html metodo=_dato parametro="ZipEntry e" %}

## Excepciones
[IOException](/Java/IOException/), [ZipException](/Java/ZipException/)

## Clase Padre
[ZipOutputStream](/Java/ZipOutputStream/)

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
