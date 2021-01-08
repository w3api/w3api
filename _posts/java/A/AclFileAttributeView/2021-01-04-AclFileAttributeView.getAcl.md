---
title: AclFileAttributeView.getAcl()
permalink: Java/AclFileAttributeView/getAcl
date: 2021-01-04
key: JavaJava.A.AclFileAttributeView
category: java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AclFileAttributeView.metodos valor="getAcl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
List<AclEntry> getAcl() throws IOException
~~~

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

## Clase Padre
[AclFileAttributeView](/Java/AclFileAttributeView/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AclFileAttributeView.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
