---
title: MBeanServerConnection.setAttributes()
permalink: Java/MBeanServerConnection/setAttributes
date: 2021-01-04
key: JavaJava.M.MBeanServerConnection
category: java
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
* **AttributeList attributes**,  {% include w3api/param_description.html metodo=_data parametro="AttributeList attributes" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName name" %}

## Excepciones
[InstanceNotFoundException](/Java/InstanceNotFoundException/), [ReflectionException](/Java/ReflectionException/), [IOException](/Java/IOException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[MBeanServerConnection](/Java/MBeanServerConnection/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanServerConnection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
