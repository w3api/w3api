---
title: MBeanServerInvocationHandler.MBeanServerInvocationHandler()
permalink: Java/MBeanServerInvocationHandler/MBeanServerInvocationHandler
date: 2021-01-11
key: JavaJava.M.MBeanServerInvocationHandler
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerInvocationHandler.constructores valor="MBeanServerInvocationHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MBeanServerInvocationHandler(MBeanServerConnection connection, ObjectName objectName)
public MBeanServerInvocationHandler(MBeanServerConnection connection, ObjectName objectName, boolean isMXBean)
~~~

## Parámetros
* **boolean isMXBean**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isMXBean" %}
* **MBeanServerConnection connection**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanServerConnection connection" %}
* **ObjectName objectName**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName objectName" %}

## Clase Padre
[MBeanServerInvocationHandler](/Java/MBeanServerInvocationHandler/)

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
