---
title: MBeanTrustPermission.MBeanTrustPermission()
permalink: Java/MBeanTrustPermission/MBeanTrustPermission
date: 2021-01-11
key: JavaJava.M.MBeanTrustPermission
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanTrustPermission.constructores valor="MBeanTrustPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MBeanTrustPermission(String name)
public MBeanTrustPermission(String name, String actions)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MBeanTrustPermission](/Java/MBeanTrustPermission/)

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
