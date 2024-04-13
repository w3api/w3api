---
title: FileContents.getRandomAccessFile()
permalink: /Java/FileContents/getRandomAccessFile/
date: 2021-01-11
key: Java.F.FileContents
category: Java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileContents.metodos valor="getRandomAccessFile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
JNLPRandomAccessFile getRandomAccessFile(String mode) throws IOException
~~~

## Parámetros
* **String mode**,  {% include w3api/param_description.html metodo=_dato parametro="String mode" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[FileContents](/Java/FileContents/)

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
