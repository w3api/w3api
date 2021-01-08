---
title: FileChannel.force()
permalink: Java/FileChannel/force
date: 2021-01-04
key: JavaJava.F.FileChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileChannel.metodos valor="force" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void force(boolean metaData) throws IOException
~~~

## Parámetros
* **boolean metaData**,  {% include w3api/param_description.html metodo=_data parametro="boolean metaData" %}

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

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
