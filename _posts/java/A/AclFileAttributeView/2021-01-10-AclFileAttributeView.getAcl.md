---
title: AclFileAttributeView.getAcl()
permalink: Java/AclFileAttributeView/getAcl
date: 2021-01-10
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
[IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[AclFileAttributeView](/Java/AclFileAttributeView/)

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
