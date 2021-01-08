---
title: PosixFileAttributeView.setGroup()
permalink: Java/PosixFileAttributeView/setGroup
date: 2021-01-04
key: JavaJava.P.PosixFileAttributeView
category: java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PosixFileAttributeView.metodos valor="setGroup" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setGroup(GroupPrincipal group) throws IOException
~~~

## Parámetros
* **GroupPrincipal group**,  {% include w3api/param_description.html metodo=_data parametro="GroupPrincipal group" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

## Clase Padre
[PosixFileAttributeView](/Java/PosixFileAttributeView/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PosixFileAttributeView.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
