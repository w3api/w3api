---
title: MBeanServerConnection.setAttribute()
permalink: Java/MBeanServerConnection/setAttribute
date: 2021-01-11
key: JavaJava.M.MBeanServerConnection
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServerConnection.metodos valor="setAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setAttribute(ObjectName name, Attribute attribute) throws InstanceNotFoundException, AttributeNotFoundException, InvalidAttributeValueException, MBeanException, ReflectionException, IOException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **Attribute attribute**,  {% include w3api/param_description.html metodo=_dato parametro="Attribute attribute" %}

## Excepciones
[InvalidAttributeValueException](/Java/InvalidAttributeValueException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/), [IOException](/Java/IOException/), [ReflectionException](/Java/ReflectionException/), [AttributeNotFoundException](/Java/AttributeNotFoundException/), [MBeanException](/Java/MBeanException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/)

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
