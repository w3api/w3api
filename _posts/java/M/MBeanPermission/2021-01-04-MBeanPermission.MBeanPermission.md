---
title: MBeanPermission.MBeanPermission()
permalink: Java/MBeanPermission/MBeanPermission
date: 2021-01-04
key: JavaJava.M.MBeanPermission
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanPermission.constructores valor="MBeanPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MBeanPermission(String name, String actions)
public MBeanPermission(String className, String member, ObjectName objectName, String actions)
~~~

## Parámetros
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **ObjectName objectName**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName objectName" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_data parametro="String actions" %}
* **String member**,  {% include w3api/param_description.html metodo=_data parametro="String member" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MBeanPermission](/Java/MBeanPermission/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
