---
title: AttachPermission.AttachPermission()
permalink: Java/AttachPermission/AttachPermission
date: 2021-01-04
key: JavaJava.A.AttachPermission
category: java
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
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_data parametro="String actions" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AttachPermission](/Java/AttachPermission/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AttachPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
