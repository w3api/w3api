---
title: MBeanServer.getClassLoaderFor()
permalink: /Java/MBeanServer/getClassLoaderFor/
date: 2021-01-11
key: Java.M.MBeanServer
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServer.metodos valor="getClassLoaderFor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ClassLoader getClassLoaderFor(ObjectName mbeanName) throws InstanceNotFoundException
~~~

## Parámetros
* **ObjectName mbeanName**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName mbeanName" %}

## Excepciones
[InstanceNotFoundException](/Java/InstanceNotFoundException/)

## Clase Padre
[MBeanServer](/Java/MBeanServer/)

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
