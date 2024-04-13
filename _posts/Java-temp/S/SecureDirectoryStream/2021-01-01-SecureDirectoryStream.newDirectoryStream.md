---
title: SecureDirectoryStream.newDirectoryStream()
permalink: /Java/SecureDirectoryStream/newDirectoryStream/
date: 2021-01-11
key: Java.S.SecureDirectoryStream
category: Java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureDirectoryStream.metodos valor="newDirectoryStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SecureDirectoryStream<T> newDirectoryStream(T path, LinkOption... options) throws IOException
~~~

## Parámetros
* **LinkOption... options**,  {% include w3api/param_description.html metodo=_dato parametro="LinkOption... options" %}
* **T path**,  {% include w3api/param_description.html metodo=_dato parametro="T path" %}

## Excepciones
[ClosedDirectoryStreamException](/Java/ClosedDirectoryStreamException/), [SecurityException](/Java/SecurityException/), [NotDirectoryException](/Java/NotDirectoryException/), [IOException](/Java/IOException/)

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
