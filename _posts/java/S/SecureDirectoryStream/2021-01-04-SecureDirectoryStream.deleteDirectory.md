---
title: SecureDirectoryStream.deleteDirectory()
permalink: Java/SecureDirectoryStream/deleteDirectory
date: 2021-01-04
key: JavaJava.S.SecureDirectoryStream
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureDirectoryStream.metodos valor="deleteDirectory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void deleteDirectory(T path) throws IOException
~~~

## Parámetros
* **T path**,  {% include w3api/param_description.html metodo=_data parametro="T path" %}

## Excepciones
[ClosedDirectoryStreamException](/Java/ClosedDirectoryStreamException/), [SecurityException](/Java/SecurityException/), [DirectoryNotEmptyException](/Java/DirectoryNotEmptyException/), [NoSuchFileException](/Java/NoSuchFileException/), [IOException](/Java/IOException/)

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
