---
title: SecureDirectoryStream.newDirectoryStream()
permalink: Java/SecureDirectoryStream/newDirectoryStream
date: 2021-01-04
key: JavaJava.S.SecureDirectoryStream
category: java
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
* **T path**,  {% include w3api/param_description.html metodo=_data parametro="T path" %}
* **LinkOption... options**,  {% include w3api/param_description.html metodo=_data parametro="LinkOption... options" %}

## Excepciones
[IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [NotDirectoryException](/Java/NotDirectoryException/), [ClosedDirectoryStreamException](/Java/ClosedDirectoryStreamException/)

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
