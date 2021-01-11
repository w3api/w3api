---
title: SecureDirectoryStream.deleteFile()
permalink: Java/SecureDirectoryStream/deleteFile
date: 2021-01-11
key: JavaJava.S.SecureDirectoryStream
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureDirectoryStream.metodos valor="deleteFile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void deleteFile(T path) throws IOException
~~~

## Parámetros
* **T path**,  {% include w3api/param_description.html metodo=_dato parametro="T path" %}

## Excepciones
[ClosedDirectoryStreamException](/Java/ClosedDirectoryStreamException/), [IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [NoSuchFileException](/Java/NoSuchFileException/)

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
