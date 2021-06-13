---
title: UserDefinedFileAttributeView.size()
permalink: /Java/UserDefinedFileAttributeView/size/
date: 2021-01-11
key: Java.U.UserDefinedFileAttributeView
category: Java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UserDefinedFileAttributeView.metodos valor="size" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int size(String name) throws IOException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [ArithmeticException](/Java/ArithmeticException/), [IOException](/Java/IOException/)

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
