---
title: AttachPermission.AttachPermission()
permalink: /Java/AttachPermission/AttachPermission/
date: 2021-01-11
key: Java.A.AttachPermission
category: Java
tags: ['java se', 'com.sun.tools.attach', 'jdk.attach', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttachPermission.constructores valor="AttachPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AttachPermission(String name)
public AttachPermission(String name, String actions)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AttachPermission](/Java/AttachPermission/)

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
