---
title: FileStore.getBlockSize()
permalink: /Java/FileStore/getBlockSize/
date: 2021-01-11
key: Java.F.FileStore
category: Java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileStore.metodos valor="getBlockSize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long getBlockSize() throws IOException
~~~

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IOException](/Java/IOException/)

## Clase Padre
[FileStore](/Java/FileStore/)

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
