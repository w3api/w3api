---
title: SecureDirectoryStream.move()
permalink: /Java/SecureDirectoryStream/move/
date: 2021-01-11
key: Java.S.SecureDirectoryStream
category: Java
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
* **T targetpath**,  {% include w3api/param_description.html metodo=_dato parametro="T targetpath" %}
* **SecureDirectoryStream&lt;T&gt; targetdir**,  {% include w3api/param_description.html metodo=_dato parametro="SecureDirectoryStream<T> targetdir" %}
* **T srcpath**,  {% include w3api/param_description.html metodo=_dato parametro="T srcpath" %}

## Excepciones
[FileAlreadyExistsException](/Java/FileAlreadyExistsException/), [IOException](/Java/IOException/), [ClosedDirectoryStreamException](/Java/ClosedDirectoryStreamException/), [SecurityException](/Java/SecurityException/), [AtomicMoveNotSupportedException](/Java/AtomicMoveNotSupportedException/)

## Clase Padre
[SecureDirectoryStream](/Java/SecureDirectoryStream/)

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
