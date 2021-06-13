---
title: MBeanServerConnection.getMBeanInfo()
permalink: Java/MBeanServerConnection/getMBeanInfo
date: 2021-01-11
key: JavaJava.M.MBeanServerConnection
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerConnection.metodos valor="getMBeanInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
MBeanInfo getMBeanInfo(ObjectName name) throws InstanceNotFoundException, IntrospectionException, ReflectionException, IOException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}

## Excepciones
[ReflectionException](/Java/ReflectionException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [IntrospectionException](/Java/IntrospectionException/), [IOException](/Java/IOException/)

## Clase Padre
[MBeanServerConnection](/Java/MBeanServerConnection/)

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
