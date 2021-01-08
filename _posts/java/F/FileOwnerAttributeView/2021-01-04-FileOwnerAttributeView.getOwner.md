---
title: FileOwnerAttributeView.getOwner()
permalink: Java/FileOwnerAttributeView/getOwner
date: 2021-01-04
key: JavaJava.F.FileOwnerAttributeView
category: java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileOwnerAttributeView.metodos valor="getOwner" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
UserPrincipal getOwner() throws IOException
~~~

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

## Clase Padre
[FileOwnerAttributeView](/Java/FileOwnerAttributeView/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileOwnerAttributeView.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
