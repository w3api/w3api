---
title: MBeanServerConnection.setAttributes()
permalink: /Java/MBeanServerConnection/setAttributes/
date: 2021-01-11
key: Java.M.MBeanServerConnection
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerConnection.metodos valor="setAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
AttributeList setAttributes(ObjectName name, AttributeList attributes) throws InstanceNotFoundException, ReflectionException, IOException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **AttributeList attributes**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeList attributes" %}

## Excepciones
[ReflectionException](/Java/ReflectionException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/), [IOException](/Java/IOException/)

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
