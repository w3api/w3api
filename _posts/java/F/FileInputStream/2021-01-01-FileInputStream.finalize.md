---
title: FileInputStream.finalize()
permalink: Java/FileInputStream/finalize
date: 2021-01-11
key: JavaJava.F.FileInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileInputStream.metodos valor="finalize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="9", forRemoval=true) protected void finalize() throws IOException
~~~

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[FileInputStream](/Java/FileInputStream/)

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
