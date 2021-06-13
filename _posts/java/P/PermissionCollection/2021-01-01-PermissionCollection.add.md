---
title: PermissionCollection.add()
permalink: /Java/PermissionCollection/add/
date: 2021-01-11
key: Java.P.PermissionCollection
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PermissionCollection.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void add(Permission permission)
~~~

## Parámetros
* **Permission permission**,  {% include w3api/param_description.html metodo=_dato parametro="Permission permission" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PermissionCollection](/Java/PermissionCollection/)

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
