---
title: FileOwnerAttributeView.setOwner()
permalink: Java/FileOwnerAttributeView/setOwner
date: 2021-01-04
key: JavaJava.F.FileOwnerAttributeView
category: java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileOwnerAttributeView.metodos valor="setOwner" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setOwner(UserPrincipal owner) throws IOException
~~~

## Parámetros
* **UserPrincipal owner**,  {% include w3api/param_description.html metodo=_data parametro="UserPrincipal owner" %}

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
