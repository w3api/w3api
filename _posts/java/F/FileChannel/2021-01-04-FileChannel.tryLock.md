---
title: FileChannel.tryLock()
permalink: Java/FileChannel/tryLock
date: 2021-01-04
key: JavaJava.F.FileChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileChannel.metodos valor="tryLock" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final FileLock tryLock() throws IOException
public abstract FileLock tryLock(long position, long size, boolean shared) throws IOException
~~~

## Parámetros
* **long position**,  {% include w3api/param_description.html metodo=_data parametro="long position" %}
* **boolean shared**,  {% include w3api/param_description.html metodo=_data parametro="boolean shared" %}
* **long size**,  {% include w3api/param_description.html metodo=_data parametro="long size" %}

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [OverlappingFileLockException](/Java/OverlappingFileLockException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[FileChannel](/Java/FileChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
