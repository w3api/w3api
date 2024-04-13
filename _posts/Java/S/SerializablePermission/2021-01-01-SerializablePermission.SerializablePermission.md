---
title: SerializablePermission.SerializablePermission()
permalink: /Java/SerializablePermission/SerializablePermission/
date: 2021-01-11
key: Java.S.SerializablePermission
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerializablePermission.constructores valor="SerializablePermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SerializablePermission(String name)
public SerializablePermission(String name, String actions)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SerializablePermission](/Java/SerializablePermission/)

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
