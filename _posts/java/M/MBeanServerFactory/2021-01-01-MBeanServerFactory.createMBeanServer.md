---
title: MBeanServerFactory.createMBeanServer()
permalink: Java/MBeanServerFactory/createMBeanServer
date: 2021-01-11
key: JavaJava.M.MBeanServerFactory
category: Java
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
* **String domain**,  {% include w3api/param_description.html metodo=_dato parametro="String domain" %}

## Excepciones
[JMRuntimeException](/Java/JMRuntimeException/), [SecurityException](/Java/SecurityException/), [ClassCastException](/Java/ClassCastException/)

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
