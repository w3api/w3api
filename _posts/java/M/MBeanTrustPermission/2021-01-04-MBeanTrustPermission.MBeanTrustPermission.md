---
title: MBeanTrustPermission.MBeanTrustPermission()
permalink: Java/MBeanTrustPermission/MBeanTrustPermission
date: 2021-01-04
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
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_data parametro="String actions" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MBeanTrustPermission](/Java/MBeanTrustPermission/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanTrustPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
