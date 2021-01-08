---
title: ZipInputStream.getNextEntry()
permalink: Java/ZipInputStream/getNextEntry
date: 2021-01-04
key: JavaJava.Z.ZipInputStream
category: java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZipInputStream.metodos valor="getNextEntry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ZipEntry getNextEntry() throws IOException
~~~

## Excepciones
[IOException](/Java/IOException/), [ZipException](/Java/ZipException/)

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
