---
title: MBeanServer.getAttributes()
permalink: /Java/MBeanServer/getAttributes/
date: 2021-01-11
key: Java.M.MBeanServer
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanServer.metodos valor="getAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
AttributeList getAttributes(ObjectName name, String[] attributes) throws InstanceNotFoundException, ReflectionException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **String[] attributes**,  {% include w3api/param_description.html metodo=_dato parametro="String[] attributes" %}

## Excepciones
[ReflectionException](/Java/ReflectionException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[MBeanServer](/Java/MBeanServer/)

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
