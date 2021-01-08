---
title: PosixFilePermissions.fromString()
permalink: Java/PosixFilePermissions/fromString
date: 2021-01-04
key: JavaJava.P.PosixFilePermissions
category: java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PosixFilePermissions.metodos valor="fromString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Set<PosixFilePermission> fromString(String perms)
~~~

## Parámetros
* **String perms**,  {% include w3api/param_description.html metodo=_data parametro="String perms" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PosixFilePermissions](/Java/PosixFilePermissions/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PosixFilePermissions.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
