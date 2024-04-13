---
title: MBeanServerPermission.MBeanServerPermission()
permalink: /Java/MBeanServerPermission/MBeanServerPermission/
date: 2021-01-11
key: Java.M.MBeanServerPermission
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerPermission.constructores valor="MBeanServerPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MBeanServerPermission(String name)
public MBeanServerPermission(String name, String actions)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MBeanServerPermission](/Java/MBeanServerPermission/)

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
