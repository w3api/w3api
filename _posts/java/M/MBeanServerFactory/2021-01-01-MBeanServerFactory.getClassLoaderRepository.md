---
title: MBeanServerFactory.getClassLoaderRepository()
permalink: Java/MBeanServerFactory/getClassLoaderRepository
date: 2021-01-11
key: JavaJava.M.MBeanServerFactory
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerFactory.metodos valor="getClassLoaderRepository" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ClassLoaderRepository getClassLoaderRepository(MBeanServer server)
~~~

## Parámetros
* **MBeanServer server**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanServer server" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MBeanServerFactory](/Java/MBeanServerFactory/)

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
