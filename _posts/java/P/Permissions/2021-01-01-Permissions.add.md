---
title: Permissions.add()
permalink: /Java/Permissions/add/
date: 2021-01-11
key: Java.P.Permissions
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Permissions.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void add(Permission permission)
~~~

## Parámetros
* **Permission permission**,  {% include w3api/param_description.html metodo=_dato parametro="Permission permission" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[Permissions](/Java/Permissions/)

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
