---
title: FileSystem.newWatchService()
permalink: Java/FileSystem/newWatchService
date: 2021-01-11
key: JavaJava.F.FileSystem
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystem.metodos valor="newWatchService" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract WatchService newWatchService() throws IOException
~~~

## Excepciones
[IOException](/Java/IOException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[FileSystem](/Java/FileSystem/)

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