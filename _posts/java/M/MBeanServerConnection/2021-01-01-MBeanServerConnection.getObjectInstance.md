---
title: MBeanServerConnection.getObjectInstance()
permalink: /Java/MBeanServerConnection/getObjectInstance/
date: 2021-01-11
key: Java.M.MBeanServerConnection
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerConnection.metodos valor="getObjectInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ObjectInstance getObjectInstance(ObjectName name) throws InstanceNotFoundException, IOException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}

## Excepciones
[InstanceNotFoundException](/Java/InstanceNotFoundException/), [IOException](/Java/IOException/)

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
