---
title: UserDefinedFileAttributeView.read()
permalink: /Java/UserDefinedFileAttributeView/read/
date: 2021-01-11
key: Java.U.UserDefinedFileAttributeView
category: Java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UserDefinedFileAttributeView.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int read(String name, ByteBuffer dst) throws IOException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **ByteBuffer dst**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer dst" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[UserDefinedFileAttributeView](/Java/UserDefinedFileAttributeView/)

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
