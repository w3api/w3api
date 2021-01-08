---
title: SimpleJavaFileObject.openWriter()
permalink: Java/SimpleJavaFileObject/openWriter
date: 2021-01-04
key: JavaJava.S.SimpleJavaFileObject
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleJavaFileObject.metodos valor="openWriter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Writer openWriter() throws IOException
~~~

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

## Clase Padre
[SimpleJavaFileObject](/Java/SimpleJavaFileObject/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleJavaFileObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
