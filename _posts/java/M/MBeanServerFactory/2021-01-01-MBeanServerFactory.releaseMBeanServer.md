---
title: MBeanServerFactory.releaseMBeanServer()
permalink: Java/MBeanServerFactory/releaseMBeanServer
date: 2021-01-11
key: JavaJava.M.MBeanServerFactory
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerFactory.metodos valor="releaseMBeanServer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void releaseMBeanServer(MBeanServer mbeanServer)
~~~

## Parámetros
* **MBeanServer mbeanServer**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanServer mbeanServer" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
