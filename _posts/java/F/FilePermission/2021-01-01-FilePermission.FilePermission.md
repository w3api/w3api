---
title: FilePermission.FilePermission()
permalink: Java/FilePermission/FilePermission
date: 2021-01-11
key: JavaJava.F.FilePermission
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FilePermission.constructores valor="FilePermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FilePermission(String path, String actions)
~~~

## Parámetros
* **String path**,  {% include w3api/param_description.html metodo=_dato parametro="String path" %}
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[FilePermission](/Java/FilePermission/)

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
