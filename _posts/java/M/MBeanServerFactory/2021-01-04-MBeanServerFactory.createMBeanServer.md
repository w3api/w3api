---
title: MBeanServerFactory.createMBeanServer()
permalink: Java/MBeanServerFactory/createMBeanServer
date: 2021-01-04
key: JavaJava.M.MBeanServerFactory
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerFactory.metodos valor="createMBeanServer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MBeanServer createMBeanServer()
public static MBeanServer createMBeanServer(String domain)
~~~

## Parámetros
* **String domain**,  {% include w3api/param_description.html metodo=_data parametro="String domain" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [ClassCastException](/Java/ClassCastException/), [JMRuntimeException](/Java/JMRuntimeException/)

## Clase Padre
[MBeanServerFactory](/Java/MBeanServerFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanServerFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
