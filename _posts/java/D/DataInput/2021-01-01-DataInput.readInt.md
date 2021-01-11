---
title: DataInput.readInt()
permalink: Java/DataInput/readInt
date: 2021-01-11
key: JavaJava.D.DataInput
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataInput.metodos valor="readInt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int readInt() throws IOException
~~~

## Excepciones
[EOFException](/Java/EOFException/), [IOException](/Java/IOException/)

## Clase Padre
[DataInput](/Java/DataInput/)

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