---
title: MBeanServerFactory.findMBeanServer()
permalink: Java/MBeanServerFactory/findMBeanServer
date: 2021-01-11
key: JavaJava.M.MBeanServerFactory
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerFactory.metodos valor="findMBeanServer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ArrayList<MBeanServer> findMBeanServer(String agentId)
~~~

## Parámetros
* **String agentId**,  {% include w3api/param_description.html metodo=_dato parametro="String agentId" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

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
