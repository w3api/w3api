---
title: MBeanServerPermission.MBeanServerPermission()
permalink: Java/MBeanServerPermission/MBeanServerPermission
date: 2021-01-04
key: JavaJava.M.MBeanServerPermission
category: java
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
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_data parametro="String actions" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MBeanServerPermission](/Java/MBeanServerPermission/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanServerPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
