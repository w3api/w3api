---
title: SecureDirectoryStream.move()
permalink: Java/SecureDirectoryStream/move
date: 2021-01-04
key: JavaJava.S.SecureDirectoryStream
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureDirectoryStream.metodos valor="move" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void move(T srcpath, SecureDirectoryStream<T> targetdir, T targetpath) throws IOException
~~~

## Parámetros
* **T targetpath**,  {% include w3api/param_description.html metodo=_data parametro="T targetpath" %}
* **T srcpath**,  {% include w3api/param_description.html metodo=_data parametro="T srcpath" %}
* **SecureDirectoryStream&lt;T&gt; targetdir**,  {% include w3api/param_description.html metodo=_data parametro="SecureDirectoryStream<T> targetdir" %}

## Excepciones
[ClosedDirectoryStreamException](/Java/ClosedDirectoryStreamException/), [SecurityException](/Java/SecurityException/), [AtomicMoveNotSupportedException](/Java/AtomicMoveNotSupportedException/), [FileAlreadyExistsException](/Java/FileAlreadyExistsException/), [IOException](/Java/IOException/)

## Clase Padre
[SecureDirectoryStream](/Java/SecureDirectoryStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecureDirectoryStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
