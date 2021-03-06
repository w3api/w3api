---
title: FileOwnerAttributeView.setOwner()
permalink: /Java/FileOwnerAttributeView/setOwner/
date: 2021-01-11
key: Java.F.FileOwnerAttributeView
category: Java
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
* **UserPrincipal owner**,  {% include w3api/param_description.html metodo=_dato parametro="UserPrincipal owner" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
