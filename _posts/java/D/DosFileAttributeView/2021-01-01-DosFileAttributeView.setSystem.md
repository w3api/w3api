---
title: DosFileAttributeView.setSystem()
permalink: /Java/DosFileAttributeView/setSystem/
date: 2021-01-11
key: Java.D.DosFileAttributeView
category: Java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DosFileAttributeView.metodos valor="setSystem" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setSystem(boolean value) throws IOException
~~~

## Parámetros
* **boolean value**,  {% include w3api/param_description.html metodo=_dato parametro="boolean value" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

## Clase Padre
[DosFileAttributeView](/Java/DosFileAttributeView/)

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
